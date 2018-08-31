# https://qiita.com/yori1029/items/a0ddd25c9571b28f3e1c
import cv2

if __name__ == '__main__':
    im = cv2.imread('test3.png',0)
    #新しい配列に入力画像の一部を代入
    # dst = im[738:1028,563:1079]
    dst = im[400:700,500:1100]
    #書き出し
    cv2.imwrite('test_result_ori3.png',dst)
