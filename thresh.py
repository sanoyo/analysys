import cv2
import numpy as np

def main():
    # 入力画像の読み込み
    img = cv2.imread("test2.png")
    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # 方法2 （OpenCVで実装）
    ret, th2 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    # 結果を出力
    cv2.imwrite("th3.png", th2)

if __name__ == "__main__":
    main()
