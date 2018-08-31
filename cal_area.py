import cv2
import numpy as np

img = cv2.imread('test_result_ori3.png',0)
# ret,thresh = cv2.threshold(img,127,255,0)
ret, thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# 黒色画素抽出
num_b = np.count_nonzero(thresh)
# print(num_b)
num_w = (thresh.size) - num_b # 全画素 - 黒色画素
# print(num_w)

if num_w < num_b: # 白色画素が黒色画素を上回る場合
   thresh = cv2.bitwise_not(thresh) # NegaPosi変換
