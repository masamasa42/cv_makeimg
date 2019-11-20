# -*- coding: utf-8 -*-

import cv2
import numpy as np
 
#TODO 色相談

color_bg = [255,255,255]
color_font = [0,0,0]

#color_bg = [0,0,0]
#color_font = [255,255,255]

#test
#color_a=[128, 64, 32]
#color_b=[64, 32, 128]
#color_c=[32, 128, 64]
#color_d=[32, 32, 32]

#CMYW [B,G,R]の並び 配色は https://ironodata.info/irononamae/list.php を参考
color_a=[209, 156, 0] #Cyan CMYK（参考値） | C100 M10 Y10 K0
color_b=[140, 0, 236] #Magenta CMYK（参考値） | C5 M100 Y45 K0
color_c=[0, 241, 255] #Yellow CMYK（参考値） | C0 M0 Y100 K0
color_d=[255,255,255]

#CMYW ganma correct#パラメータ手動調整
#color_a=[232, 206, 128] #Cyan
#color_b=[198, 128, 246] #Magenta
#color_c=[128, 248, 255] #Yellow
#color_d=[255,255,255]


width=800
height=600

gap = width//16
offset = height//4
barsize = width//8
#barsize = width//12
#barsize = width//16
pixsize = barsize

imageArray = np.zeros((height, width, 3), np.uint8)
size = imageArray.shape[:2]
print(size)

###背景色
for h in range(height):
    for w in range(width):
        imageArray[h, w] = color_bg
cv2.imwrite("blank.bmp", imageArray);


###画像作成
###色サンプル
for h in range(gap*0, gap*1):
    for w in range(gap*0, gap*1):
        imageArray[h, w] = color_a
for h in range(gap*0, gap*1):
    for w in range(gap*1, gap*2):
        imageArray[h, w] = color_b
for h in range(gap*0, gap*1):
    for w in range(gap*2, gap*3):
        imageArray[h, w] = color_c
for h in range(gap*0, gap*1):
    for w in range(gap*3, gap*4):
        imageArray[h, w] = color_d

#####1段目 最大値*最大値
for h in range(offset+barsize*0//2, offset+barsize*1//2):
    for w in range(barsize*0, barsize//2):
        imageArray[h, w] = color_a
for h in range(offset+barsize*1//2, offset+barsize*2//2):
    for w in range(barsize*0, barsize//2):
        imageArray[h, w] = color_b
for h in range(offset+barsize*0//2, offset+barsize*1//2):
    for w in range(barsize//2, barsize):
        imageArray[h, w] = color_c
for h in range(offset+barsize*1//2, offset+barsize*2//2):
    for w in range(barsize//2, barsize):
        imageArray[h, w] = color_d
tmp = str(barsize//2) + "*" + str(barsize//2)
cv2.putText(imageArray, tmp, (0, offset+barsize+20),cv2.FONT_HERSHEY_PLAIN, 1.2, color_font , 1, cv2.LINE_AA)
lim = width//barsize

#####1段目
for i in range (1,lim):
    pixsize = barsize//(i+1)//2
    tmp = str(pixsize) + "*" + str(pixsize)
    cv2.putText(imageArray, tmp, (barsize*i, offset+barsize+20),cv2.FONT_HERSHEY_PLAIN, 1.2, color_font , 1, cv2.LINE_AA)

    for j in range(0,i+1):
        for k in range(0,i+1):
            xoffset = barsize*i+j*pixsize*2
            yoffset = offset+k*pixsize*2
            for h in range(yoffset, yoffset+pixsize):
                for w in range(xoffset, xoffset+pixsize):
                    imageArray[h, w] = color_a
            for h in range(yoffset+pixsize, yoffset+2*pixsize):
                for w in range(xoffset, xoffset+pixsize):
                    imageArray[h, w] = color_b
            for h in range(yoffset, yoffset+pixsize):
                for w in range(xoffset+pixsize, xoffset+2*pixsize):
                    imageArray[h, w] = color_c
            for h in range(yoffset+pixsize, yoffset+2*pixsize):
                for w in range(xoffset+pixsize, xoffset+2*pixsize):
                    imageArray[h, w] = color_d

#####2段目
offset = height//2
for i in range (1,lim):
    pixsize = barsize//(i+1)//4
    tmp = str(pixsize) + "*" + str(pixsize)
    cv2.putText(imageArray, tmp, (barsize*i, offset+barsize+20),cv2.FONT_HERSHEY_PLAIN, 1.2, color_font , 1, cv2.LINE_AA)

    for j in range(0,(i+1)*2):
        for k in range(0,(i+1)*2):
            xoffset = barsize*i+j*pixsize*2
            yoffset = offset+k*pixsize*2
            for h in range(yoffset, yoffset+pixsize):
                for w in range(xoffset, xoffset+pixsize):
                    imageArray[h, w] = color_a
            for h in range(yoffset+pixsize, yoffset+2*pixsize):
                for w in range(xoffset, xoffset+pixsize):
                    imageArray[h, w] = color_b
            for h in range(yoffset, yoffset+pixsize):
                for w in range(xoffset+pixsize, xoffset+2*pixsize):
                    imageArray[h, w] = color_c
            for h in range(yoffset+pixsize, yoffset+2*pixsize):
                for w in range(xoffset+pixsize, xoffset+2*pixsize):
                    imageArray[h, w] = color_d

#####3段目
offset = height*3//4
for i in range (1,lim):
    pixsize = barsize//(i+1)//8
    tmp = str(pixsize) + "*" + str(pixsize)
    cv2.putText(imageArray, tmp, (barsize*i, offset+barsize+20),cv2.FONT_HERSHEY_PLAIN, 1.2, color_font , 1, cv2.LINE_AA)

    for j in range(0,(i+1)*4):
        for k in range(0,(i+1)*4):
            xoffset = barsize*i+j*pixsize*2
            yoffset = offset+k*pixsize*2
            for h in range(yoffset, yoffset+pixsize):
                for w in range(xoffset, xoffset+pixsize):
                    imageArray[h, w] = color_a
            for h in range(yoffset+pixsize, yoffset+2*pixsize):
                for w in range(xoffset, xoffset+pixsize):
                    imageArray[h, w] = color_b
            for h in range(yoffset, yoffset+pixsize):
                for w in range(xoffset+pixsize, xoffset+2*pixsize):
                    imageArray[h, w] = color_c
            for h in range(yoffset+pixsize, yoffset+2*pixsize):
                for w in range(xoffset+pixsize, xoffset+2*pixsize):
                    imageArray[h, w] = color_d

###動作確認
print(1)
#print(imageArray)

###画像出力
cv2.imwrite("sample.bmp", imageArray)