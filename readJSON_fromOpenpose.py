import json
import numpy as np
import cv2
import os
import time

# 実行のループをフレーム数に合わせる
frame = 0

while True:
    # ループに入った瞬間の時刻を取得
    frameTime = time.time()

    # JSONファイルの前の数字は12桁
    index = "{0:012d}".format(frame)
    path = os.path.dirname(os.path.abspath(__file__)) + '/outputs/test/'
    path2JSONfile = path + index + '_keypoints.json'

    # jsonのロード
    try:
        with open(path2JSONfile, 'r') as f:
            data = json.load(f)
    except:
        continue

    # keypointsの取得
    kp2d = np.array(data['people'][0]['pose_keypoints_2d']).reshape((25,3))

    # 信頼度が0の場合x座標，y座標も0にする
    kp2d[np.where(kp2d[:,2] == 0)] = (0,0,0)

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

    if frame != 0: # 前の座標が0の時（検出されたない時）はループを抜けときたい
        pixPerFrame = r_wrist - old_r_wrist
        pixPerSecond = (r_wrist - old_r_wrist) / (frameTime - old_frameTime)

        print('pix/frame :', pixPerFrame)
        print('pix/second', pixPerSecond)

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

    # 次フレームまでに現在のフレームを記憶させる
    old_frameTime = frameTime

    print('r_wrist :', r_wrist)

    #print(kp2d)

    frame += 1


