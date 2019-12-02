# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 16:08:32 2019

@author: manakamura
"""
#複数の色スクエアを描画した画像を作成する

import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

color_bg = [255,255,255]
color_font = [0,0,0]
#color_font_n = [255,255,255]

#CMYW [B,G,R]の並び 配色は https://ironodata.info/irononamae/list.php を参考
width=800
height=600

imageArray = np.zeros((height, width, 3), np.uint8)
size = imageArray.shape[:2]

###背景色
for h in range(height):
    for w in range(width):
        imageArray[h, w] = color_bg
cv2.imwrite("blank.bmp", imageArray);


def func_color_rgb(imageArray,x,y,gap,color_a):
    #color_a:rgbの順
    for h in range(y, y+gap):
        for w in range(x, x+gap):
            imageArray[h, w] = [color_a[2],color_a[1],color_a[0]]
    
    tmp=str(color_a[2])+","+str(color_a[1])+","+str(color_a[0])
    cv2.putText(imageArray, tmp, (x+1,y+gap-1),cv2.FONT_HERSHEY_PLAIN, 0.6, [(color_a[2]+128)%255,(color_a[1]+128)%255,(color_a[0]+128)%255] , 1, cv2.LINE_AA)

def func_color_bgr(imageArray,x,y,gap,color_a):
    #color_a:bgrの順
    for h in range(y, y+gap):
        for w in range(x, x+gap):
            imageArray[h, w] = color_a
    
    tmp=str(color_a[0])+","+str(color_a[1])+","+str(color_a[2])
    cv2.putText(imageArray, tmp, (x+1,y+gap-1),cv2.FONT_HERSHEY_PLAIN, 0.6, [(color_a[0]+128)%255,(color_a[1]+128)%255,(color_a[2]+128)%255] , 1, cv2.LINE_AA)

def func_text(imageArray,x,y,gap,str_a):
    tmp=str_a
    cv2.putText(imageArray, tmp, (x+1,y+gap-1),cv2.FONT_HERSHEY_PLAIN, 0.6, [(color_a[0]+128)%255,(color_a[1]+128)%255,(color_a[2]+128)%255] , 1, cv2.LINE_AA)
    

    
print("===")
# 128 160 192 224 256
#M調整
color_w=[255,255,255]
color_k=[0,0,0]

color_a=[255, 255, 160]
color_b=[255, 160, 255]
color_c=[160, 255, 255]
color_d=[255, 255, 255]

tmp = "BGR:"
cv2.putText(imageArray, tmp, (0,0),cv2.FONT_HERSHEY_PLAIN, 0.5, color_font , 1, cv2.LINE_AA)

#pix=50
pix=64
ilim=1 #x座標 (縦方向に並べて出力していく)
jlim=7

text_tmp=["none",
"B-1(C)",
"B-3(C)",
"No.46(Y)",
"No.40(Y)",
"N0.18(M)",
"N0.17(M)"]

color_tmp=[[230,233,232],
[181,202,211],
[39,134,186],
[221,211,63],
[232,185,0],
[231,133,130],
[221,92,172]]
#rgb
#color_tmp=[[0,0,0],[255,255,255],[255,255,255],[128,255,255],[255,128,255],[255,255,128],[0,0,0]]
        
for i in range(0,ilim):
    for j in range(0,jlim):
        print(color_tmp[jlim*i+j])
        func_color_rgb(imageArray,(i+1)*pix,j*pix,pix,color_tmp[jlim*i+j])
        func_text(imageArray,i*pix,j*pix,pix,text_tmp[jlim*i+j])

color_tmp=[[7,7,7],
[9,11,15],
[0,4,11],
[14,15,5],
[20,17,1],
[12,6,7],
[34,17,19]]
for i in range(0,ilim):
    for j in range(0,jlim):
        print(color_tmp[jlim*i+j])
        func_color_rgb(imageArray,(i+2)*pix,j*pix,pix,color_tmp[jlim*i+j])

color_tmp=[[202,201,195],
[180,196,198],
[36,119,160],
[197,188,54],
[203,161,0],
[206,117,110],
[195,80,145]]
for i in range(0,ilim):
    for j in range(0,jlim):
        print(color_tmp[jlim*i+j])
        func_color_rgb(imageArray,(i+4)*pix,j*pix,pix,color_tmp[jlim*i+j])
        func_text(imageArray,i*pix,j*pix,pix,text_tmp[jlim*i+j])

color_tmp=[[148,154,154],
[109,124,130],
[0,70,111],
[125,122,36],
[149,118,0],
[147,84,83],
[136,56,105]]
for i in range(0,ilim):
    for j in range(0,jlim):
        print(color_tmp[jlim*i+j])
        func_color_rgb(imageArray,(i+5)*pix,j*pix,pix,color_tmp[jlim*i+j])
        func_text(imageArray,i*pix,j*pix,pix,text_tmp[jlim*i+j])

#cv2.putText(imageArray, "hoge1", ((i+1)*pix,7*pix+30),cv2.FONT_HERSHEY_PLAIN, 0.5, [0,0,0] , 1, cv2.LINE_AA)
#cv2.putText(imageArray, "hoge2", ((i+2)*pix,7*pix+30),cv2.FONT_HERSHEY_PLAIN, 0.5, [0,0,0] , 1, cv2.LINE_AA)
#cv2.putText(imageArray, "hoge3", ((i+4)*pix,7*pix+30),cv2.FONT_HERSHEY_PLAIN, 0.5, [0,0,0] , 1, cv2.LINE_AA)
#cv2.putText(imageArray, "hoge4", ((i+5)*pix,7*pix+30),cv2.FONT_HERSHEY_PLAIN, 0.5, [0,0,0] , 1, cv2.LINE_AA)

#fontpath ='C:\Windows\Fonts\HGRPP1.TTC' # Windows10 だと C:\Windows\Fonts\ 以下にフォントがあります。
fontpath ='C:\Windows\Fonts\HGRGM.TTC'
font = ImageFont.truetype(fontpath, 12) #
img_pil = Image.fromarray(imageArray) #配列の各値を8bit(1byte)整数型(0～255)をPIL Imageに変換。
draw = ImageDraw.Draw(img_pil) # drawインスタンスを生成

draw.text((1*pix+2,7*pix+8), "パネル白", font = font , fill = (0,0,0) ) # drawにテキストを記載 fill:色 BGRA (RGB)
draw.text((2*pix+2,7*pix+8), "パネル黒", font = font , fill = (0,0,0) ) # drawにテキストを記載 fill:色 BGRA (RGB)
draw.text((4*pix+2,7*pix+8), "シート白", font = font , fill = (0,0,0) ) # drawにテキストを記載 fill:色 BGRA (RGB)
draw.text((5*pix+2,7*pix+8), "シート黒", font = font , fill = (0,0,0) ) # drawにテキストを記載 fill:色 BGRA (RGB)
imageArray = np.array(img_pil) # PIL を配列に変換



#stripe 各色テスト
print("===")

cv2.imwrite("sample.bmp", imageArray)


