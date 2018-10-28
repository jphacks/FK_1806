import json
import numpy as np
import os
import time
import pyaudio
import wave
from datetime import datetime
import matplotlib.pyplot as plt
import urllib.request
import urllib.parse
import concurrent.futures
import asyncio
import winsound

def listenSNAP_withMike():
    data = stream.read(chunk)
    x = np.fft.fft(np.frombuffer(data, dtype="int16") / 32768.0)
    amp = np.abs(x)

    # 周波数分布に偏りが少なく、高周波域の総和が高く、最大値が低音でない音→スナップ音に近い音を抽出
    if (amp<=noize_threshold).all() and amp[450:512].sum()>snap_threshold and amp[0:512].argmax()>maxamp_threshold:
        print('snapped!')
        winsound.Beep(500, 500)

        return True

# number 1 => ByeBye
# number 2 => HandUp
# number 3 => Safe
async def recognizingGesture(keypoint, old_keypoint, number):
    global delta_time, standard_of_distance   # mainの方で使うから

    delta_pixel = keypoint - old_keypoint
    delta_time = frame_time - old_frame_time
    delta_pixel_standardized = delta_pixel / standard_of_distance
    pixel_per_second = delta_pixel_standardized / delta_time

    outliers = 50   # 外れ値

    # ByeBye
    if number == 1:
        threshold_byebyeSpeed = 20
        howlong_byebye_interval = 1
        global byebye_time   # mainのとこで定義してるやつ

        # Safeとの誤検出が多くなったため、左手の情報も考慮する
        delta_pixel_left = l_wrist - old_l_wrist
        delta_pixel_left_standardized = delta_pixel_left / standard_of_distance
        pixel_per_second_left = delta_pixel_left_standardized / delta_time

        byebye_time += delta_time

        if byebye_time >= -1 and np.abs(pixel_per_second_left[0]) <= 5:
            # 右手首が右ひじより上にあって、内側(左側)へある程度の速度(x軸)で振った後
            # 一定時間以内に外側(右側)にある程度の速度(x軸)で振る
            if (r_elbow[1] - keypoint[1]) >= 0 and pixel_per_second[0] >= threshold_byebyeSpeed and np.abs(pixel_per_second[0]) <= outliers:
                byebye_time = -1
            if byebye_time < 0 and (r_elbow[1] - keypoint[1]) >= 0 and pixel_per_second[0] <= -threshold_byebyeSpeed and np.abs(pixel_per_second[0]) <= outliers:
                byebye_time = -(howlong_byebye_interval+1)
                print('Bye Bye!')
                await get(number)

    # HandUp
    elif number == 2:
        threshold_handupSpeed = 30
        global hand_down   # 右手首が右ひじよりも下にあるか否か

        # 右ひじより右手首が下の状態から、ある程度の速さ(y軸)で右手首が右ひじより上になる
        if (r_elbow[1] - keypoint[1]) < 0:
            hand_down = True
        if hand_down == True and (r_elbow[1] - keypoint[1]) >= 0 and -pixel_per_second[1] >= threshold_handupSpeed and np.abs(pixel_per_second[1]) <= outliers:
            hand_down = False
            print("HandUp!")
            await get(number)

    # Safe
    elif number == 3:
        # 左手用
        delta_pixel_left = l_wrist - old_l_wrist
        delta_pixel_left_standardized = delta_pixel_left / standard_of_distance
        pixel_per_second_left = delta_pixel_left_standardized / delta_time

        threshold_safeSpeed = 20
        howlong_safe_interval = 1
        global safe_interval

        safe_interval += delta_time

        # 直前にsafeの判定がない
        if safe_interval >= 0 :
            # 両手をある程度の速度(x軸)で広げた時
            if pixel_per_second[0] <= -threshold_safeSpeed and pixel_per_second_left[0] >= threshold_safeSpeed and np.abs(pixel_per_second[1]) <= outliers:
                safe_interval = -howlong_safe_interval
                print('Safe!')
                await get(number)

async def get(gesture_number):
    params = {
        "number": gesture_number
    }
    p = urllib.parse.urlencode(params)
    url = "http://fullfill.sakura.ne.jp/JPHACKS2018/server.php?" + p

    with urllib.request.urlopen(url) as res:
        html = res.read().decode("utf-8")
        print(html)

# ------------------------------------------------------------------------

if __name__ == "__main__":
    # listenSNAP_withMike で使用する変数
    chunk = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 2
    noize_threshold = 50
    snap_threshold = 2.5
    maxamp_threshold = 25
    p = pyaudio.PyAudio()
    stream = p.open(format = FORMAT,
        channels = CHANNELS,
        rate = RATE,
        input = True,
        frames_per_buffer = chunk
    )

    # 初期化ゾーン
    frame = 0   # 実行のループをフレーム数に合わせる
    one_time = 0
    snapped = False
    delta_time = 0
    snap_interval = 4

    interval_of_recognizingGesture = 0
    standard_of_distance = 0
    byebye_time = 0
    #swinging_time = 0
    hand_down = False
    safe_interval = 0

    while True:
        frame_time = time.time()   # ループに入った瞬間の時刻を取得

        # JSONファイルの前の数字は12桁
        index = "{0:012d}".format(frame)
        path = os.path.dirname(os.path.abspath(__file__)) + '/outputs/ByeByetest/'
        path2JSONfile = path + index + '_keypoints.json'

        if snapped == False:   # 処理時間軽減のため
            if listenSNAP_withMike():
                snapped = True

        # jsonのロード
        try:
            with open(path2JSONfile, 'r') as f:
                data = json.load(f)
        except:
            continue

        # たまに"people"が検出されない時があるっぽい
        if not data['people']:
            print('"people" cannot find at', index)
            frame += 1
            continue

        kp2d = np.array(data['people'][0]['pose_keypoints_2d']).reshape((25,3))   # keypointsの取得
        kp2d[np.where(kp2d[:,2] == 0)] = (0,0,0)   # 信頼度が0の場合x座標，y座標も0にする

        kp2d = kp2d[:, 0:2]   # 信頼度は省いておく
        #print(kp2d)

        nose       = kp2d[0]
        l_eye      = kp2d[16]
        r_eye      = kp2d[15]
        l_ear      = kp2d[18]
        r_ear      = kp2d[17]
        neck       = kp2d[1]
        l_shoulder = kp2d[5]
        r_shoulder = kp2d[2]
        l_elbow    = kp2d[6]
        r_elbow    = kp2d[3]
        l_wrist    = kp2d[7]
        r_wrist    = kp2d[4]
        mid_hip    = kp2d[8]
        l_hip      = kp2d[12]
        r_hip      = kp2d[9]
        l_knee     = kp2d[13]
        r_knee     = kp2d[10]
        l_ankle    = kp2d[14]
        r_ankle    = kp2d[11]
        l_heel     = kp2d[21]
        r_heel     = kp2d[24]
        l_bigtoe   = kp2d[19]
        r_bigtoe   = kp2d[22]
        l_smalltoe = kp2d[20]
        r_smalltoe = kp2d[23]

        if snapped == True:
        #if snapped == False or snapped == True:
            if frame != 0:   # 偏差が必要なので2フレーム目から処理を行う
                if nose[0] != 0:   # 鼻が検出されている時
                    if r_eye[0] != 0:     # 右目が検出されていたら鼻と右目との距離を距離（ピクセル）の基準とする
                        standard_of_distance = np.abs(nose - r_eye)
                    elif l_eye[0] != 0:   # 右目が検出されていない時は鼻と左目との距離を距離（ピクセル）の基準とする
                        standard_of_distance = np.abs(nose - l_eye)
                else:
                    frame += 1 # JSONを更新するために必要
                    continue

                #recognizingGesture(r_wrist, old_r_wrist, 1)   # ByeBye
                #recognizingGesture(r_wrist, old_r_wrist, 2)   # HandUp
                #recognizingGesture(r_wrist, old_r_wrist, 3)   # Safe

                loop = asyncio.get_event_loop()
                loop.run_until_complete(recognizingGesture(r_wrist, old_r_wrist, 1))   # ByeBye
                loop.run_until_complete(recognizingGesture(r_wrist, old_r_wrist, 2))   # HandUp
                loop.run_until_complete(recognizingGesture(r_wrist, old_r_wrist, 3))   # Safe

                # スナップ音が検知されてから2秒間の間ジェスチャを認識させる
                interval_of_recognizingGesture += delta_time
                print('recognizing gesture...')

        else:
            interval_of_recognizingGesture = 0

        if interval_of_recognizingGesture > snap_interval:
            snapped = False
            print('finish recognizing')

        old_nose       = nose
        old_l_eye      = l_eye
        old_r_eye      = r_eye
        old_l_ear      = l_ear
        old_r_ear      = r_ear
        old_neck       = neck
        old_l_shoulder = l_shoulder
        old_r_shoulder = r_shoulder
        old_l_elbow    = l_elbow
        old_r_elbow    = r_elbow
        old_l_wrist    = l_wrist
        old_r_wrist    = r_wrist
        old_mid_hip    = mid_hip
        old_l_hip      = l_hip
        old_r_hip      = r_hip
        old_l_knee     = l_knee
        old_r_knee     = r_knee
        old_l_ankle    = l_ankle
        old_r_ankle    = r_ankle
        old_l_heel     = l_heel
        old_r_heel     = r_heel
        old_l_bigtoe   = l_bigtoe
        old_r_bigtoe   = r_bigtoe
        old_l_smalltoe = l_smalltoe
        old_r_smalltoe = r_smalltoe

        old_frame_time = frame_time   # 次フレームまでに現在のフレームを記憶させる

        frame += 1
