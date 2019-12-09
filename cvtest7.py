# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:40:32 2019

@author: manakamura
"""
import cv2
import numpy as np
import os

def func_makeimg(imageArray,x,y,color_a,color_b,color_c,color_d,color_at,color_bt,color_ct):
    #global imageArray
    #print(x)
    #print(y)
    tmp = "BGR:"
    cv2.putText(imageArray, tmp, (x+gap*0+1,y+gap*1+6),cv2.FONT_HERSHEY_PLAIN, 0.5, color_font , 1, cv2.LINE_AA)

    tmp="trans_c_w:"+str(color_at[0])+" trans_c_k:"+str(color_at[1])
    cv2.putText(imageArray, tmp, (x+gap*0+1,y+gap*1+26),cv2.FONT_HERSHEY_PLAIN, 0.6, [0,0,0] , 1, cv2.LINE_AA)
    tmp="trans_m_w:"+str(color_bt[0])+" trans_m_k:"+str(color_bt[1])
    cv2.putText(imageArray, tmp, (x+gap*0+1,y+gap*1+36),cv2.FONT_HERSHEY_PLAIN, 0.6, [0,0,0] , 1, cv2.LINE_AA)
    tmp="trans_y_w:"+str(color_ct[0])+" trans_y_k:"+str(color_ct[1])
    cv2.putText(imageArray, tmp, (x+gap*0+1,y+gap*1+46),cv2.FONT_HERSHEY_PLAIN, 0.6, [0,0,0] , 1, cv2.LINE_AA)
    
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
    cv2.putText(imageArray, tmp, (xoffset, yoffset +barsize*2+10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, color_font , 1, cv2.LINE_AA)
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
    cv2.putText(imageArray, tmp, (xoffset, yoffset +barsize*2+10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, color_font , 1, cv2.LINE_AA)
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
    cv2.putText(imageArray, tmp, (xoffset, yoffset +barsize*2+10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, color_font , 1, cv2.LINE_AA)
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
    cv2.putText(imageArray, tmp, (xoffset, yoffset +barsize*2+10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, color_font , 1, cv2.LINE_AA)
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
    
    
def func_stripe(imageArray,x,y,color_a,color_b,color_c,color_d,color_at,color_bt,color_ct,color_num):
    tmp = "BGR:"
    cv2.putText(imageArray, tmp, (x+gap*0+1,y+gap*1+6),cv2.FONT_HERSHEY_PLAIN, 0.5, color_font , 1, cv2.LINE_AA)

    tmp="trans_c_w:"+str(color_at[0])+" trans_c_k:"+str(color_at[1])
    cv2.putText(imageArray, tmp, (x+gap*0+1,y+gap*1+26),cv2.FONT_HERSHEY_PLAIN, 0.6, [0,0,0] , 1, cv2.LINE_AA)
    tmp="trans_m_w:"+str(color_bt[0])+" trans_m_k:"+str(color_bt[1])
    cv2.putText(imageArray, tmp, (x+gap*0+1,y+gap*1+36),cv2.FONT_HERSHEY_PLAIN, 0.6, [0,0,0] , 1, cv2.LINE_AA)
    tmp="trans_y_w:"+str(color_ct[0])+" trans_y_k:"+str(color_ct[1])
    cv2.putText(imageArray, tmp, (x+gap*0+1,y+gap*1+46),cv2.FONT_HERSHEY_PLAIN, 0.6, [0,0,0] , 1, cv2.LINE_AA)
    
    if(color_num<3):
        color_num = 3
    if(color_num>4):
        color_num = 4

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
    xbarsize=barsize//2
    for h in range(y+barsize*2, y+barsize*4):
        for w in range(x+xbarsize*0, x+xbarsize*1):
            imageArray[h, w] = color_a
    for h in range(y+barsize*2, y+barsize*4):
        for w in range(x+xbarsize*1, x+xbarsize*2):
            imageArray[h, w] = color_b
    for h in range(y+barsize*2, y+barsize*4):
        for w in range(x+xbarsize*2, x+xbarsize*3):
            imageArray[h, w] = color_c
    for h in range(y+barsize*2, y+barsize*4):
        for w in range(x+xbarsize*3, x+xbarsize*4):
            imageArray[h, w] = color_d
    tmp = str(barsize*2) + "*" + str(xbarsize)
    cv2.putText(imageArray, tmp, (x, y+barsize*4+10),cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, color_font , 1, cv2.LINE_AA)
    
    #=====
    xoffset = x+barsize*2
    yoffset = y+barsize*2
    pixsize = 4
    tmp = str(barsize*2) + "*" + str(pixsize)
    cv2.putText(imageArray, tmp, (xoffset, yoffset +barsize*2+10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, color_font , 1, cv2.LINE_AA)
    lim = barsize//pixsize
    for k in range(0,lim,color_num):
        for h in range(yoffset, yoffset+barsize*2):
            for w in range(xoffset+k*pixsize, xoffset+k*pixsize+pixsize):
                imageArray[h, w] = color_a
        for h in range(yoffset, yoffset+barsize*2):
            for w in range(xoffset+k*pixsize+1*pixsize, xoffset+k*pixsize+2*pixsize):
                imageArray[h, w] = color_b
        for h in range(yoffset, yoffset+barsize*2):
            for w in range(xoffset+k*pixsize+2*pixsize, xoffset+k*pixsize+3*pixsize):
                imageArray[h, w] = color_c
        if(color_num==4):
            for h in range(yoffset, yoffset+barsize*2):
                for w in range(xoffset+k*pixsize+3*pixsize, xoffset+k*pixsize+4*pixsize):
                    imageArray[h, w] = color_d
    #=====
    #=====
    xoffset = x+barsize*3
    yoffset = y+barsize*2
    pixsize = 3
    tmp = str(barsize*2) + "*" + str(pixsize)
    cv2.putText(imageArray, tmp, (xoffset, yoffset +barsize*2+10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, color_font , 1, cv2.LINE_AA)
    lim = barsize//pixsize
    for k in range(0,lim,color_num):
        for h in range(yoffset, yoffset+barsize*2):
            for w in range(xoffset+k*pixsize, xoffset+k*pixsize+pixsize):
                imageArray[h, w] = color_a
        for h in range(yoffset, yoffset+barsize*2):
            for w in range(xoffset+k*pixsize+1*pixsize, xoffset+k*pixsize+2*pixsize):
                imageArray[h, w] = color_b
        for h in range(yoffset, yoffset+barsize*2):
            for w in range(xoffset+k*pixsize+2*pixsize, xoffset+k*pixsize+3*pixsize):
                imageArray[h, w] = color_c
        if(color_num==4):
            for h in range(yoffset, yoffset+barsize*2):
                for w in range(xoffset+k*pixsize+3*pixsize, xoffset+k*pixsize+4*pixsize):
                    imageArray[h, w] = color_d
    #=====
    #=====
    xoffset = x+barsize*4
    yoffset = y+barsize*2
    pixsize = 2
    tmp = str(barsize*2) + "*" + str(pixsize)
    cv2.putText(imageArray, tmp, (xoffset, yoffset +barsize*2+10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, color_font , 1, cv2.LINE_AA)
    lim = barsize//pixsize
    for k in range(0,lim,color_num):
        for h in range(yoffset, yoffset+barsize*2):
            for w in range(xoffset+k*pixsize, xoffset+k*pixsize+pixsize):
                imageArray[h, w] = color_a
        for h in range(yoffset, yoffset+barsize*2):
            for w in range(xoffset+k*pixsize+1*pixsize, xoffset+k*pixsize+2*pixsize):
                imageArray[h, w] = color_b
        for h in range(yoffset, yoffset+barsize*2):
            for w in range(xoffset+k*pixsize+2*pixsize, xoffset+k*pixsize+3*pixsize):
                imageArray[h, w] = color_c
        if(color_num==4):
            for h in range(yoffset, yoffset+barsize*2):
                for w in range(xoffset+k*pixsize+3*pixsize, xoffset+k*pixsize+4*pixsize):
                    imageArray[h, w] = color_d
    #=====
    #=====
    xoffset = x+barsize*5
    yoffset = y+barsize*2
    pixsize = 1
    tmp = str(barsize*2) + "*" + str(pixsize)
    cv2.putText(imageArray, tmp, (xoffset, yoffset +barsize*2+10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, color_font , 1, cv2.LINE_AA)
    lim = barsize//pixsize
    for k in range(0,lim,color_num):
        for h in range(yoffset, yoffset+barsize*2):
            for w in range(xoffset+k*pixsize, xoffset+k*pixsize+pixsize):
                imageArray[h, w] = color_a
        for h in range(yoffset, yoffset+barsize*2):
            for w in range(xoffset+k*pixsize+1*pixsize, xoffset+k*pixsize+2*pixsize):
                imageArray[h, w] = color_b
        for h in range(yoffset, yoffset+barsize*2):
            for w in range(xoffset+k*pixsize+2*pixsize, xoffset+k*pixsize+3*pixsize):
                imageArray[h, w] = color_c
        if(color_num==4):
            for h in range(yoffset, yoffset+barsize*2):
                for w in range(xoffset+k*pixsize+3*pixsize, xoffset+k*pixsize+4*pixsize):
                    imageArray[h, w] = color_d
    #=====
    

def func_mosaic(imageArray,x,y,color_a_in,color_b_in,color_c_in,color_d,color_at,color_bt,color_ct,color_num,flg):
    color_a=[[0],[0],[0]]
    color_b=[[0],[0],[0]]
    color_c=[[0],[0],[0]]
    for i in range(0,3):
        if(flg!=0):
            color_a[i]=color_a_in[i]*(100-color_at[0])//100 + 255*color_at[0]//100
        else:
            color_a[i]=color_a_in[i]
        if(flg!=1):
            color_b[i]=color_b_in[i]*(100-color_bt[0])//100 + 255*color_bt[0]//100
        else:
            color_b[i]=color_b_in[i]
        if(flg!=2):
            color_c[i]=color_c_in[i]*(100-color_ct[0])//100 + 255*color_ct[0]//100
        else:
            color_c[i]=color_c_in[i]
    tmp = "BGR:"
    cv2.putText(imageArray, tmp, (x+gap*0+1,y+gap*1+6),cv2.FONT_HERSHEY_PLAIN, 0.5, color_font , 1, cv2.LINE_AA)

    tmp="trans_c_w:"+str(color_at[0])+" trans_c_k:"+str(color_at[1])
    cv2.putText(imageArray, tmp, (x+gap*0+1,y+gap*1+26),cv2.FONT_HERSHEY_PLAIN, 0.6, [0,0,0] , 1, cv2.LINE_AA)
    tmp="trans_m_w:"+str(color_bt[0])+" trans_m_k:"+str(color_bt[1])
    cv2.putText(imageArray, tmp, (x+gap*0+1,y+gap*1+36),cv2.FONT_HERSHEY_PLAIN, 0.6, [0,0,0] , 1, cv2.LINE_AA)
    tmp="trans_y_w:"+str(color_ct[0])+" trans_y_k:"+str(color_ct[1])
    cv2.putText(imageArray, tmp, (x+gap*0+1,y+gap*1+46),cv2.FONT_HERSHEY_PLAIN, 0.6, [0,0,0] , 1, cv2.LINE_AA)
    
    if(color_num<3):
        color_num = 3
    if(color_num>4):
        color_num = 4
        
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
    xbarsize=barsize//2
    for h in range(y+barsize*2, y+barsize*4):
        for w in range(x+xbarsize*0, x+xbarsize*1):
            imageArray[h, w] = color_a
    for h in range(y+barsize*2, y+barsize*4):
        for w in range(x+xbarsize*1, x+xbarsize*2):
            imageArray[h, w] = color_b
    for h in range(y+barsize*2, y+barsize*4):
        for w in range(x+xbarsize*2, x+xbarsize*3):
            imageArray[h, w] = color_c
    for h in range(y+barsize*2, y+barsize*4):
        for w in range(x+xbarsize*3, x+xbarsize*4):
            imageArray[h, w] = color_d
    tmp = str(barsize*2) + "*" + str(xbarsize)
    cv2.putText(imageArray, tmp, (x, y+barsize*4+10),cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, color_font , 1, cv2.LINE_AA)
    
    #=====
    xoffset = x+barsize*2
    yoffset = y+barsize*2
    pixsize = 4
    tmp = str(pixsize) + "*" + str(pixsize)
    cv2.putText(imageArray, tmp, (xoffset, yoffset +barsize*2+10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, color_font , 1, cv2.LINE_AA)
    lim = barsize//pixsize
    for j in range(0,lim*2,1):
        for k in range(0,lim,1):
            if((j+k)%color_num==0):
                tmp_color = color_a
            if((j+k)%color_num==1):
                tmp_color = color_b
            if((j+k)%color_num==2):
                tmp_color = color_c
            if((j+k)%color_num==3):
                tmp_color = color_d
            for h in range(yoffset+j*pixsize, yoffset+j*pixsize+pixsize):
                for w in range(xoffset+k*pixsize, xoffset+k*pixsize+pixsize):
                    imageArray[h, w] = tmp_color
    #=====
    #=====
    xoffset = x+barsize*3
    yoffset = y+barsize*2
    pixsize = 3
    tmp = str(pixsize) + "*" + str(pixsize)
    cv2.putText(imageArray, tmp, (xoffset, yoffset +barsize*2+10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, color_font , 1, cv2.LINE_AA)
    lim = barsize//pixsize
    for j in range(0,lim*2,1):
        for k in range(0,lim,1):
            if((j+k)%color_num==0):
                tmp_color = color_a
            if((j+k)%color_num==1):
                tmp_color = color_b
            if((j+k)%color_num==2):
                tmp_color = color_c
            if((j+k)%color_num==3):
                tmp_color = color_d
            for h in range(yoffset+j*pixsize, yoffset+j*pixsize+pixsize):
                for w in range(xoffset+k*pixsize, xoffset+k*pixsize+pixsize):
                    imageArray[h, w] = tmp_color
    #=====
    #=====
    xoffset = x+barsize*4
    yoffset = y+barsize*2
    pixsize = 2
    tmp = str(pixsize) + "*" + str(pixsize)
    cv2.putText(imageArray, tmp, (xoffset, yoffset +barsize*2+10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, color_font , 1, cv2.LINE_AA)
    lim = barsize//pixsize
    for j in range(0,lim*2,1):
        for k in range(0,lim,1):
            if((j+k)%color_num==0):
                tmp_color = color_a
            if((j+k)%color_num==1):
                tmp_color = color_b
            if((j+k)%color_num==2):
                tmp_color = color_c
            if((j+k)%color_num==3):
                tmp_color = color_d
            for h in range(yoffset+j*pixsize, yoffset+j*pixsize+pixsize):
                for w in range(xoffset+k*pixsize, xoffset+k*pixsize+pixsize):
                    imageArray[h, w] = tmp_color
    #=====
    #=====
    xoffset = x+barsize*5
    yoffset = y+barsize*2
    pixsize = 1
    tmp = str(pixsize) + "*" + str(pixsize)
    cv2.putText(imageArray, tmp, (xoffset, yoffset +barsize*2+10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, color_font , 1, cv2.LINE_AA)
    lim = barsize//pixsize
    for j in range(0,lim*2,1):
        for k in range(0,lim,1):
            if((j+k)%color_num==0):
                tmp_color = color_a
            if((j+k)%color_num==1):
                tmp_color = color_b
            if((j+k)%color_num==2):
                tmp_color = color_c
            if((j+k)%color_num==3):
                tmp_color = color_d
            for h in range(yoffset+j*pixsize, yoffset+j*pixsize+pixsize):
                for w in range(xoffset+k*pixsize, xoffset+k*pixsize+pixsize):
                    imageArray[h, w] = tmp_color
    #=====


def func_delta(imageArray,x,y,color_a_in,color_b_in,color_c_in,color_d,color_at,color_bt,color_ct,flg):

    color_a=[[0],[0],[0]]
    color_b=[[0],[0],[0]]
    color_c=[[0],[0],[0]]
    for i in range(0,3):
        if(flg!=0):
            color_a[i]=color_a_in[i]*(100-color_at[0])//100 + 255*color_at[0]//100
        else:
            color_a[i]=color_a_in[i]
        if(flg!=1):
            color_b[i]=color_b_in[i]*(100-color_bt[0])//100 + 255*color_bt[0]//100
        else:
            color_b[i]=color_b_in[i]
        if(flg!=2):
            color_c[i]=color_c_in[i]*(100-color_ct[0])//100 + 255*color_ct[0]//100
        else:
            color_c[i]=color_c_in[i]
    tmp = "BGR:"
    cv2.putText(imageArray, tmp, (x+gap*0+1,y+gap*1+6),cv2.FONT_HERSHEY_PLAIN, 0.5, color_font , 1, cv2.LINE_AA)

    tmp="trans_c_w:"+str(color_at[0])+" trans_c_k:"+str(color_at[1])
    cv2.putText(imageArray, tmp, (x+gap*0+1,y+gap*1+26),cv2.FONT_HERSHEY_PLAIN, 0.6, [0,0,0] , 1, cv2.LINE_AA)
    tmp="trans_m_w:"+str(color_bt[0])+" trans_m_k:"+str(color_bt[1])
    cv2.putText(imageArray, tmp, (x+gap*0+1,y+gap*1+36),cv2.FONT_HERSHEY_PLAIN, 0.6, [0,0,0] , 1, cv2.LINE_AA)
    tmp="trans_y_w:"+str(color_ct[0])+" trans_y_k:"+str(color_ct[1])
    cv2.putText(imageArray, tmp, (x+gap*0+1,y+gap*1+46),cv2.FONT_HERSHEY_PLAIN, 0.6, [0,0,0] , 1, cv2.LINE_AA)

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
    xbarsize=barsize//2
    for h in range(y+barsize*2, y+barsize*4):
        for w in range(x+xbarsize*0, x+xbarsize*1):
            imageArray[h, w] = color_a
    for h in range(y+barsize*2, y+barsize*4):
        for w in range(x+xbarsize*1, x+xbarsize*2):
            imageArray[h, w] = color_b
    for h in range(y+barsize*2, y+barsize*4):
        for w in range(x+xbarsize*2, x+xbarsize*3):
            imageArray[h, w] = color_c
    for h in range(y+barsize*2, y+barsize*4):
        for w in range(x+xbarsize*3, x+xbarsize*4):
            imageArray[h, w] = color_d
    tmp = str(barsize*2) + "*" + str(xbarsize)
    cv2.putText(imageArray, tmp, (x, y+barsize*4+10),cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, color_font , 1, cv2.LINE_AA)
    
    #=====
    xoffset = x+barsize*2
    yoffset = y+barsize*2
    pixsize = 6
    pixgap = 3
    tmp = str(pixsize) + "*" + str(pixsize)
    cv2.putText(imageArray, tmp, (xoffset, yoffset +barsize*2+10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, color_font , 1, cv2.LINE_AA)
    lim = barsize//pixsize
    for j in range(0,lim*2,1):
        for k in range(0,lim,1):
            if(j%2==0):
                if((k)%3==0):
                    tmp_color = color_a
                if((k)%3==1):
                    tmp_color = color_b
                if((k)%3==2):
                    tmp_color = color_c
            else:
                if((k)%3==1):
                    tmp_color = color_a
                if((k)%3==2):
                    tmp_color = color_b
                if((k)%3==0):
                    tmp_color = color_c
                
            for h in range(yoffset+j*pixsize, yoffset+j*pixsize+pixsize):
                for w in range(xoffset+k*pixsize+(j%2)*pixgap, xoffset+k*pixsize+pixsize+(j%2)*pixgap):
                    imageArray[h, w] = tmp_color
    #=====
    #=====
    xoffset = x+barsize*3
    yoffset = y+barsize*2
    pixsize = 4
    pixgap = 2
    tmp = str(pixsize) + "*" + str(pixsize)
    cv2.putText(imageArray, tmp, (xoffset, yoffset +barsize*2+10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, color_font , 1, cv2.LINE_AA)
    lim = barsize//pixsize
    for j in range(0,lim*2,1):
        for k in range(0,lim,1):
            if(j%2==0):
                if((k)%3==0):
                    tmp_color = color_a
                if((k)%3==1):
                    tmp_color = color_b
                if((k)%3==2):
                    tmp_color = color_c
            else:
                if((k)%3==1):
                    tmp_color = color_a
                if((k)%3==2):
                    tmp_color = color_b
                if((k)%3==0):
                    tmp_color = color_c
                
            for h in range(yoffset+j*pixsize, yoffset+j*pixsize+pixsize):
                for w in range(xoffset+k*pixsize+(j%2)*pixgap, xoffset+k*pixsize+pixsize+(j%2)*pixgap):
                    imageArray[h, w] = tmp_color
    #=====
    #=====
    xoffset = x+barsize*4
    yoffset = y+barsize*2
    pixsize = 2
    pixgap = 1
    tmp = str(pixsize) + "*" + str(pixsize)
    cv2.putText(imageArray, tmp, (xoffset, yoffset +barsize*2+10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, color_font , 1, cv2.LINE_AA)
    lim = barsize//pixsize
    for j in range(0,lim*2,1):
        for k in range(0,lim,1):
            if(j%2==0):
                if((k)%3==0):
                    tmp_color = color_a
                if((k)%3==1):
                    tmp_color = color_b
                if((k)%3==2):
                    tmp_color = color_c
            else:
                if((k)%3==1):
                    tmp_color = color_a
                if((k)%3==2):
                    tmp_color = color_b
                if((k)%3==0):
                    tmp_color = color_c
                
            for h in range(yoffset+j*pixsize, yoffset+j*pixsize+pixsize):
                for w in range(xoffset+k*pixsize+(j%2)*pixgap, xoffset+k*pixsize+pixsize+(j%2)*pixgap):
                    imageArray[h, w] = tmp_color
    #=====


def makeimg(filename,color_a,color_ak,color_b,color_bk,color_c,color_ck,color_at,color_bt,color_ct):


    imageArray = np.zeros((height, width, 3), np.uint8)
    size = imageArray.shape[:2]
    
    for h in range(height):
        for w in range(width):
            imageArray[h, w] = color_bg
    #cv2.imwrite("blank.bmp", imageArray);
    color_d=(195,201,202)

    print("===begin===")
    func_delta(imageArray,0,0,color_ak,color_b,color_c,color_d,color_at,color_bt,color_ct,0)
    func_delta(imageArray,0,250,color_a,color_bk,color_c,color_d,color_at,color_bt,color_ct,1)
    func_delta(imageArray,400,0,color_a,color_b,color_ck,color_d,color_at,color_bt,color_ct,2)
    func_delta(imageArray,400,250,color_a,color_b,color_c,color_d,color_at,color_bt,color_ct,3)
    #func_mosaic(imageArray,0,0,color_ak,color_b,color_c,color_d,color_at,color_bt,color_ct,3,0)
    #func_mosaic(imageArray,0,300,color_a,color_bk,color_c,color_d,color_at,color_bt,color_ct,3,1)
    #func_mosaic(imageArray,400,0,color_a,color_b,color_ck,color_d,color_at,color_bt,color_ct,3,2)
    #func_mosaic(imageArray,400,300,color_a,color_b,color_c,color_d,color_at,color_bt,color_ct,3,3)

    #func_makeimg(imageArray,0,0,color_a,color_bk,color_c,color_d,color_at,color_bt,color_ct)
    #func_makeimg(imageArray,0,300,color_a,color_bk,color_c,color_d,color_at,color_bt,color_ct)
    #func_makeimg(imageArray,400,0,color_a,color_b,color_ck,color_d,color_at,color_bt,color_ct)
    #func_makeimg(imageArray,400,300,color_a,color_b,color_c,color_d,color_at,color_bt,color_ct)
    #func_stripe(imageArray,0,0,color_ak,color_b,color_c,color_d,color_at,color_bt,color_ct,3)
    #func_stripe(imageArray,0,300,color_a,color_bk,color_c,color_d,color_at,color_bt,color_ct,3)
    #func_stripe(imageArray,400,0,color_a,color_b,color_ck,color_d,color_at,color_bt,color_ct,3)
    #func_stripe(imageArray,400,300,color_a,color_b,color_c,color_d,color_at,color_bt,color_ct,3)
    #func_stripe(imageArray,0,0,color_ak,color_b,color_c,color_d,color_at,color_bt,color_ct,4)
    #func_stripe(imageArray,0,300,color_a,color_bk,color_c,color_d,color_at,color_bt,color_ct,4)
    #func_stripe(imageArray,400,0,color_a,color_b,color_ck,color_d,color_at,color_bt,color_ct,4)
    #func_stripe(imageArray,400,300,color_a,color_b,color_c,color_d,color_at,color_bt,color_ct,4)
    #func_mosaic(imageArray,0,0,color_ak,color_b,color_c,color_d,color_at,color_bt,color_ct,4)
    #func_mosaic(imageArray,0,300,color_a,color_bk,color_c,color_d,color_at,color_bt,color_ct,4)
    #func_mosaic(imageArray,400,0,color_a,color_b,color_ck,color_d,color_at,color_bt,color_ct,4)
    #func_mosaic(imageArray,400,300,color_a,color_b,color_c,color_d,color_at,color_bt,color_ct,4)
    #func_delta(imageArray,0,0,color_ak,color_b,color_c,color_d,color_at,color_bt,color_ct)
    #func_delta(imageArray,0,300,color_a,color_bk,color_c,color_d,color_at,color_bt,color_ct)
    #func_delta(imageArray,400,0,color_a,color_b,color_ck,color_d,color_at,color_bt,color_ct)
    #func_delta(imageArray,400,300,color_a,color_b,color_c,color_d,color_at,color_bt,color_ct)

    tmp="filename:"+filename
    print(filename)
    cv2.putText(imageArray, tmp, (1,500),cv2.FONT_HERSHEY_PLAIN, 0.6, [0,0,0] , 1, cv2.LINE_AA)
    
    cv2.imwrite(filename, imageArray)
    print("=== end ===")

color_bg = [255,255,255]
color_font = [0,0,0]
width=800
height=600
gap = width//16
offset = height//4
barsize = width//16
pixsize = barsize
#色指定はそれぞれbgr順

#ファイルからデータ読み込み
if(os.path.exists('./cvtest_data.txt')):
    fileobj = open('./cvtest_data.txt')
    data = fileobj.read()
    fileobj.close()
#    print(data)
#    print(data[3])#3mojime 0から開始
#    print(lines[1])#2行目
    lines = data.split('\n') # 改行で区切る(改行文字そのものは戻り値のデータには含まれない)

    tmp = lines[0].split(',')
    color_a_num,color_b_num,color_c_num = list(map(lambda a: int(a), tmp))

    color_a=[]
    color_an=[]
    color_ak=[]
    color_at=[]
    color_b=[]
    color_bn=[]
    color_bk=[]
    color_bt=[]
    color_c=[]
    color_cn=[]
    color_ck=[]
    color_ct=[]
    for i in range(1,color_a_num+1):
        tmp = lines[i].split(',')
        tmpn=0
        tmp_c1=[0,0,0]
        tmp_c2=[0,0,0]
        tmp_ct=[0,0]
        tmpn,tmp_c1[2],tmp_c1[1],tmp_c1[0],tmp_c2[2],tmp_c2[1],tmp_c2[0],tmp_ct[0],tmp_ct[1]= list(map(lambda a: int(a), tmp))
        color_an.append(tmpn)
        color_a.append(tmp_c1)
        color_ak.append(tmp_c2)
        color_at.append(tmp_ct)
    for i in range(color_a_num+1,color_a_num+1+color_b_num):
        tmp = lines[i].split(',')
        tmpn=0
        tmp_c1=[0,0,0]
        tmp_c2=[0,0,0]
        tmp_ct=[0,0]
        tmpn,tmp_c1[2],tmp_c1[1],tmp_c1[0],tmp_c2[2],tmp_c2[1],tmp_c2[0],tmp_ct[0],tmp_ct[1]= list(map(lambda a: int(a), tmp))
        color_bn.append(tmpn)
        color_b.append(tmp_c1)
        color_bk.append(tmp_c2)
        color_bt.append(tmp_ct)
    for i in range(color_a_num+1+color_b_num,color_a_num+1+color_b_num+color_c_num):
        tmp = lines[i].split(',')
        tmpn=0
        tmp_c1=[0,0,0]
        tmp_c2=[0,0,0]
        tmp_ct=[0,0]
        tmpn,tmp_c1[2],tmp_c1[1],tmp_c1[0],tmp_c2[2],tmp_c2[1],tmp_c2[0],tmp_ct[0],tmp_ct[1]= list(map(lambda a: int(a), tmp))
        color_cn.append(tmpn)
        color_c.append(tmp_c1)
        color_ck.append(tmp_c2)
        color_ct.append(tmp_ct)

    test_str="color_a_num:"+str(color_a_num)+" color_b_num:"+str(color_b_num)+" color_c_num:"+str(color_c_num)
    print(test_str)
    print("data:")
    print(color_an)
    print(color_a)
    print(color_ak)
    print(color_bn)
    print(color_b)
    print(color_bk)
    print(color_cn)
    print(color_c)
    print(color_ck)
else:
    #test用 CMYそれぞれ2色づつ設定
    color_a_num=2
    color_an=[1,3]
    color_a=[[198,196,180],
    [160,119,36]]
    color_ak=[[130,124,109],
    [111,70,0]]
    color_at=[0,0]
    
    color_b_num=2
    color_bn=[18,17]
    color_b=[[110,117,206],
    [145,80,195]]
    color_bk=[[83,84,147],
    [105,56,136]]
    color_bt=[0,0]
    
    color_c_num=2
    color_cn=[46,40]
    color_c=[[54,188,197],
    [0,161,203]]
    color_ck=[[36,122,125],
    [0,118,149]]
    color_ct=[0,0]
    
#color_d=[255, 255, 255]

for i in range(0,color_a_num):
    for j in range(0,color_b_num):
        for k in range(0,color_c_num):
            #filename="sample.bmp"
            filename="img_delta_c"+str(color_an[i]).rjust(3, '0')+"_m"+str(color_bn[j]).rjust(3, '0')+"_y"+str(color_cn[k]).rjust(3, '0')+".bmp"
            makeimg(filename,color_a[i],color_ak[i],color_b[j],color_bk[j],color_c[k],color_ck[k],color_at[i],color_bt[j],color_ct[k])
