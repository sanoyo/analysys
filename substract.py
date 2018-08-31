# https://algorithm.joho.info/programming/python/opencv-background-subtraction-py/
# -*- coding: utf-8 -*-
import cv2
import numpy as np

def main():
    i = 0      # カウント変数
    th = 50    # 差分画像の閾値
    cap = cv2.VideoCapture("sample.MOV")

    # 最初のフレームを背景画像に設定
    # bg = cv2.imread('test.png')
    # bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)

    while(cap.isOpened()):
        ret,frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 切り取った画像と同じ高さ、幅を指定
        gray = gray[300:800,400:1100]
        ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
        # ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

        num_b = np.count_nonzero(thresh)
        num_w = (thresh.size) - num_b
        print(num_w)

        # 差分の絶対値を計算
        # 現在のフレーム ー 背景
        # mask = cv2.absdiff(gray, bg)

        # 差分画像を二値化してマスク画像を算出
        # mask[mask < th] = 0
        # mask[mask >= th] = 255

        cv2.imshow("Th", thresh)

        # i += 1    # カウントを1増やす

        # 背景画像の更新（一定間隔）
        # if(i > 3000):
        #     ret, bg = cap.read()
        #     bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)
        #     i = 0 # カウント変数の初期化

        # qキーが押されたら途中終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
