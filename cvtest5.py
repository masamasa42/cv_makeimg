# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 17:25:21 2019

@author: manakamura
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:54:22 2019

@author: manakamura
"""

import cv2
import numpy as np


color_bg = [255,255,255]
color_font = [0,0,0]

#CMYW [B,G,R]の並び 配色は https://ironodata.info/irononamae/list.php を参考
width=800
height=600

gap = width//16
offset = height//4
barsize = width//16
pixsize = barsize

imageArray = np.zeros((height, width, 3), np.uint8)
size = imageArray.shape[:2]

###背景色
for h in range(height):
    for w in range(width):
        imageArray[h, w] = color_bg
cv2.imwrite("blank.bmp", imageArray);


def func(imageArray,x,y,color_a,color_b,color_c,color_d):
    #global imageArray
    #print(x)
    #print(y)
    tmp = "BGR:"
    cv2.putText(imageArray, tmp, (x+gap*0+1,y+gap*1+6),cv2.FONT_HERSHEY_PLAIN, 0.5, color_font , 1, cv2.LINE_AA)

    for h in range(y+gap*0, y+gap*1):
        for w in range(x+gap*0, x+gap*1):
            imageArray[h, w] = color_a
    tmp =str(color_a[0]) + "," + str(color_a[1]) + "," + str(color_a[2])
    cv2.putText(imageArray, tmp, (x+gap*0+1,y+gap*1+15),cv2.FONT_HERSHEY_PLAIN, 0.5, color_font , 1, cv2.LINE_AA)
    for h in range(y+gap*0, y+gap*1):
        for w in range(x+gap*1, x+gap*2):
            imageArray[h, w] = color_b
    tmp =str(color_b[0]) + "," + str(color_b[1]) + "," + str(color_b[2])
    cv2.putText(imageArray, tmp, (x+gap*1,y+gap*1+15),cv2.FONT_HERSHEY_PLAIN, 0.5, color_font , 1, cv2.LINE_AA)
    for h in range(y+gap*0, y+gap*1):
        for w in range(x+gap*2, x+gap*3):
            imageArray[h, w] = color_c
    tmp =str(color_c[0]) + "," + str(color_c[1]) + "," + str(color_c[2])
    cv2.putText(imageArray, tmp, (x+gap*2,y+gap*1+15),cv2.FONT_HERSHEY_PLAIN, 0.5, color_font , 1, cv2.LINE_AA)
    for h in range(y+gap*0, y+gap*1):
        for w in range(x+gap*3, x+gap*4):
            imageArray[h, w] = color_d
    tmp =str(color_d[0]) + "," + str(color_d[1]) + "," + str(color_d[2])
    cv2.putText(imageArray, tmp, (x+gap*3,y+gap*1+15),cv2.FONT_HERSHEY_PLAIN, 0.5, color_font , 1, cv2.LINE_AA)

    #1st block
    for h in range(y+barsize*2, y+barsize*3):
        for w in range(x+barsize*0, x+barsize*1):
            imageArray[h, w] = color_a
    for h in range(y+barsize*3, y+barsize*4):
        for w in range(x+barsize*0, x+barsize*1):
            imageArray[h, w] = color_b
    for h in range(y+barsize*2, y+barsize*3):
        for w in range(x+barsize*1, x+barsize*2):
            imageArray[h, w] = color_c
    for h in range(y+barsize*3, y+barsize*4):
        for w in range(x+barsize*1, x+barsize*2):
            imageArray[h, w] = color_d
    tmp = str(barsize) + "*" + str(barsize)
    cv2.putText(imageArray, tmp, (x, y+barsize*4+10),cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, color_font , 1, cv2.LINE_AA)

    #=====
    xoffset = x+barsize*2
    yoffset = y+barsize*2
    pixsize = 4
    tmp = str(pixsize) + "*" + str(pixsize)
    cv2.putText(imageArray, tmp, (xoffset, yoffset +barsize*2+10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, color_font , 1, cv2.LINE_AA)
    lim = barsize//pixsize
    for j in range(0,lim*2,2):
        for k in range(0,lim,2):
            for h in range(yoffset+j*pixsize, yoffset+j*pixsize+pixsize):
                for w in range(xoffset+k*pixsize, xoffset+k*pixsize+pixsize):
                    imageArray[h, w] = color_a
            for h in range(yoffset+j*pixsize+pixsize, yoffset+j*pixsize+2*pixsize):
                for w in range(xoffset+k*pixsize, xoffset+k*pixsize+pixsize):
                    imageArray[h, w] = color_b
            for h in range(yoffset+j*pixsize, yoffset+j*pixsize+pixsize):
                for w in range(xoffset+k*pixsize+pixsize, xoffset+k*pixsize+2*pixsize):
                    imageArray[h, w] = color_c
            for h in range(yoffset+j*pixsize+pixsize, yoffset+j*pixsize+2*pixsize):
                for w in range(xoffset+k*pixsize+pixsize, xoffset+k*pixsize+2*pixsize):
                    imageArray[h, w] = color_d
    #=====

    #=====
    xoffset = x+barsize*3
    yoffset = y+barsize*2
    pixsize = 3
    tmp = str(pixsize) + "*" + str(pixsize)
    cv2.putText(imageArray, tmp, (xoffset, yoffset +barsize*2+10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, color_font , 1, cv2.LINE_AA)
    lim = barsize//pixsize
    for j in range(0,lim*2,2):
        for k in range(0,lim,2):
            for h in range(yoffset+j*pixsize, yoffset+j*pixsize+pixsize):
                for w in range(xoffset+k*pixsize, xoffset+k*pixsize+pixsize):
                    imageArray[h, w] = color_a
            for h in range(yoffset+j*pixsize+pixsize, yoffset+j*pixsize+2*pixsize):
                for w in range(xoffset+k*pixsize, xoffset+k*pixsize+pixsize):
                    imageArray[h, w] = color_b
            for h in range(yoffset+j*pixsize, yoffset+j*pixsize+pixsize):
                for w in range(xoffset+k*pixsize+pixsize, xoffset+k*pixsize+2*pixsize):
                    imageArray[h, w] = color_c
            for h in range(yoffset+j*pixsize+pixsize, yoffset+j*pixsize+2*pixsize):
                for w in range(xoffset+k*pixsize+pixsize, xoffset+k*pixsize+2*pixsize):
                    imageArray[h, w] = color_d
    #=====

    #=====
    xoffset = x+barsize*4
    yoffset = y+barsize*2
    pixsize = 2
    tmp = str(pixsize) + "*" + str(pixsize)
    cv2.putText(imageArray, tmp, (xoffset, yoffset +barsize*2+10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, color_font , 1, cv2.LINE_AA)
    lim = barsize//pixsize
    for j in range(0,lim*2,2):
        for k in range(0,lim,2):
            for h in range(yoffset+j*pixsize, yoffset+j*pixsize+pixsize):
                for w in range(xoffset+k*pixsize, xoffset+k*pixsize+pixsize):
                    imageArray[h, w] = color_a
            for h in range(yoffset+j*pixsize+pixsize, yoffset+j*pixsize+2*pixsize):
                for w in range(xoffset+k*pixsize, xoffset+k*pixsize+pixsize):
                    imageArray[h, w] = color_b
            for h in range(yoffset+j*pixsize, yoffset+j*pixsize+pixsize):
                for w in range(xoffset+k*pixsize+pixsize, xoffset+k*pixsize+2*pixsize):
                    imageArray[h, w] = color_c
            for h in range(yoffset+j*pixsize+pixsize, yoffset+j*pixsize+2*pixsize):
                for w in range(xoffset+k*pixsize+pixsize, xoffset+k*pixsize+2*pixsize):
                    imageArray[h, w] = color_d
    #=====


    #=====
    xoffset = x+barsize*5
    yoffset = y+barsize*2
    pixsize = 1
    tmp = str(pixsize) + "*" + str(pixsize)
    cv2.putText(imageArray, tmp, (xoffset, yoffset +barsize*2+10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, color_font , 1, cv2.LINE_AA)
    lim = barsize//pixsize
    for j in range(0,lim*2,2):
        for k in range(0,lim,2):
            for h in range(yoffset+j*pixsize, yoffset+j*pixsize+pixsize):
                for w in range(xoffset+k*pixsize, xoffset+k*pixsize+pixsize):
                    imageArray[h, w] = color_a
            for h in range(yoffset+j*pixsize+pixsize, yoffset+j*pixsize+2*pixsize):
                for w in range(xoffset+k*pixsize, xoffset+k*pixsize+pixsize):
                    imageArray[h, w] = color_b
            for h in range(yoffset+j*pixsize, yoffset+j*pixsize+pixsize):
                for w in range(xoffset+k*pixsize+pixsize, xoffset+k*pixsize+2*pixsize):
                    imageArray[h, w] = color_c
            for h in range(yoffset+j*pixsize+pixsize, yoffset+j*pixsize+2*pixsize):
                for w in range(xoffset+k*pixsize+pixsize, xoffset+k*pixsize+2*pixsize):
                    imageArray[h, w] = color_d
    #=====
    
print("===")
color_w=[255,255,255]
color_k=[0,0,0]

# 128 160 192 224 256
#M調整
color_a=[255, 255, 160]
color_b=[255, 160, 255]
color_c=[160, 255, 255]
color_d=[255, 255, 255]
func(imageArray,0,0,color_k,color_b,color_c,color_d)
color_a=[255, 255, 160]
color_b=[255, 160, 255]
color_c=[160, 255, 255]
#color_d=[255,255,255]
func(imageArray,0,300,color_a,color_k,color_c,color_d)
color_a=[255, 255, 160]
color_b=[255, 160, 255]
color_c=[160, 255, 255]
#color_d=[255,255,255]
func(imageArray,400,0,color_a,color_b,color_k,color_d)
color_a=[255, 255, 160]
color_b=[255, 160, 255]
color_c=[160, 255, 255]
#color_d=[255,255,255]
func(imageArray,400,300,color_a,color_b,color_c,color_d)
print("===")

#a,b,cの輝度を統一
#color_a=[255, 245, 0]
#color_b=[244, 0, 253]
#color_c=[0, 241, 255]
#color_d=[255,255,255]

#font確認用
#tmp="123456"
#x=0
#y=0
#cv2.putText(imageArray, tmp, (x+100,y+gap*1+15),cv2.FONT_HERSHEY_SIMPLEX, 0.6, color_font , 1, cv2.LINE_AA)
#cv2.putText(imageArray, tmp, (x+100,y+gap*1+35),cv2.FONT_HERSHEY_PLAIN, 0.6, color_font , 1, cv2.LINE_AA)
#cv2.putText(imageArray, tmp, (x+100,y+gap*1+55),cv2.FONT_HERSHEY_DUPLEX, 0.6, color_font , 1, cv2.LINE_AA)
#cv2.putText(imageArray, tmp, (x+100,y+gap*1+75),cv2.FONT_HERSHEY_COMPLEX, 0.6, color_font , 1, cv2.LINE_AA)
#cv2.putText(imageArray, tmp, (x+100,y+gap*1+95),cv2.FONT_HERSHEY_TRIPLEX, 0.6, color_font , 1, cv2.LINE_AA)
#cv2.putText(imageArray, tmp, (x+100,y+gap*1+115),cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, color_font , 1, cv2.LINE_AA)
#cv2.putText(imageArray, tmp, (x+100,y+gap*1+135),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.6, color_font , 1, cv2.LINE_AA)
#cv2.putText(imageArray, tmp, (x+100,y+gap*1+155),cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 0.6, color_font , 1, cv2.LINE_AA)

cv2.imwrite("sample.bmp", imageArray)

