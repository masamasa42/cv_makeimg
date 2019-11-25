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
    cv2.putText(imageArray, tmp, (x+gap*0+1,y+gap*1+5),cv2.FONT_HERSHEY_PLAIN, 0.5, color_font , 1, cv2.LINE_AA)

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
    cv2.putText(imageArray, tmp, (x, y+barsize*4+10),cv2.FONT_HERSHEY_PLAIN, 0.75, color_font , 1, cv2.LINE_AA)

    #=====
    xoffset = x+barsize*2
    yoffset = y+barsize*2
    pixsize = 6
    tmp = str(pixsize) + "*" + str(pixsize)
    cv2.putText(imageArray, tmp, (xoffset, yoffset +barsize*2+10), cv2.FONT_HERSHEY_PLAIN, 0.6, color_font , 1, cv2.LINE_AA)
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
    pixsize = 5
    tmp = str(pixsize) + "*" + str(pixsize)
    cv2.putText(imageArray, tmp, (xoffset, yoffset +barsize*2+10), cv2.FONT_HERSHEY_PLAIN, 0.6, color_font , 1, cv2.LINE_AA)
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
    pixsize = 4
    tmp = str(pixsize) + "*" + str(pixsize)
    cv2.putText(imageArray, tmp, (xoffset, yoffset +barsize*2+10), cv2.FONT_HERSHEY_PLAIN, 0.6, color_font , 1, cv2.LINE_AA)
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
    pixsize = 3
    tmp = str(pixsize) + "*" + str(pixsize)
    cv2.putText(imageArray, tmp, (xoffset, yoffset +barsize*2+10), cv2.FONT_HERSHEY_PLAIN, 0.6, color_font , 1, cv2.LINE_AA)
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
    xoffset = x+barsize*6
    yoffset = y+barsize*2
    pixsize = 2
    tmp = str(pixsize) + "*" + str(pixsize)
    cv2.putText(imageArray, tmp, (xoffset, yoffset +barsize*2+10), cv2.FONT_HERSHEY_PLAIN, 0.6, color_font , 1, cv2.LINE_AA)
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
    xoffset = x+barsize*7
    yoffset = y+barsize*2
    pixsize = 1
    tmp = str(pixsize) + "*" + str(pixsize)
    cv2.putText(imageArray, tmp, (xoffset, yoffset +barsize*2+10), cv2.FONT_HERSHEY_PLAIN, 0.6, color_font , 1, cv2.LINE_AA)
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
color_a=[209, 156, 0] #Cyan CMYK（参考値） | C100 M10 Y10 K0
color_b=[140, 0, 236] #Magenta CMYK（参考値） | C5 M100 Y45 K0
color_c=[0, 241, 255] #Yellow CMYK（参考値） | C0 M0 Y100 K0
color_d=[255,255,255]
func(imageArray,0,0,color_a,color_b,color_c,color_d)

#CMYW ganma correct#パラメータ手動調整
color_a=[232, 206, 128] #Cyan
color_b=[198, 128, 246] #Magenta
color_c=[128, 248, 255] #Yellow
color_d=[255,255,255]
#a,b,c 底上げ2
color_a=[255, 255, 192]
color_b=[255, 192, 255]
color_c=[192, 255, 255]
color_d=[255,255,255]
func(imageArray,0,300,color_a,color_b,color_c,color_d)

#a,b,c 底上げ
color_a=[255, 255, 128]
color_b=[255, 128, 255]
color_c=[128, 255, 255]
color_d=[255,255,255]
#a,b,c 底上げ3
color_a=[255, 255, 224]
color_b=[255, 224, 255]
color_c=[224, 255, 255]
color_d=[255,255,255]
func(imageArray,400,0,color_a,color_b,color_c,color_d)

color_a=[255, 255, 0]
color_b=[255, 0, 255]
color_c=[0, 255, 255]
color_d=[255,255,255]
func(imageArray,400,300,color_a,color_b,color_c,color_d)
print("===")

#a,b,cの輝度を統一
#color_a=[255, 245, 0]
#color_b=[244, 0, 253]
#color_c=[0, 241, 255]
#color_d=[255,255,255]



cv2.imwrite("sample.bmp", imageArray)

