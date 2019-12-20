# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:09:16 2019

@author: manakamura
"""
import cv2

background = cv2.imread("000.bmp")
foreground = cv2.imread("001.bmp")
imgMask  = cv2.imread("mask.bmp",cv2.IMREAD_GRAYSCALE)

height, width, color = background.shape # 幅・高さ・色を取得
for y in range(0, height):
	for x in range(0, width):
		if (imgMask[y][x]!=0):
			background[y][x] = foreground[y][x]
            
#background[imgMask==0] = [128, 128, 128]
#h, w = foreground.shape[:2]  # 前景画像の大きさ
#x, y = 100, 200  # 背景画像の座標上で前景画像を貼り付ける位置
#roi = background[y : y + h, x : x + w, :]
#result = np.where(np.expand_dims(mask == 255, -1), foreground, roi)

#cv2.imshow(result)
cv2.imwrite("002.bmp",background)