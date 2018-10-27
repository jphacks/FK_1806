import json
import numpy as np
import cv2
import os

# 実行のループをフレーム数に合わせる
frame = 0

while True:
    # JSONファイルの前の数字は12桁
    index = "{0:012d}".format(frame)
    path = os.path.dirname(os.path.abspath(__file__)) + '/outputs/test1020/'
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

    print(nose)

    #print(kp2d)

    frame += 1


