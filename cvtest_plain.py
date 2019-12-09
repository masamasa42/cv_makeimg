# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:52:42 2019

@author: manakamura
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:40:32 2019

@author: manakamura
"""
import cv2
import numpy as np

def func_makeimg(imageArray,x,y,color_a,color_b,color_c,color_at,color_bt,color_ct):
    tmp = "BGR:"
    cv2.putText(imageArray, tmp, (x+gap*0+1,y+gap*0+6),cv2.FONT_HERSHEY_PLAIN, 0.5, color_font , 1, cv2.LINE_AA)

    tmp="trans_c_w:"+str(color_at[0])+" trans_c_k:"+str(color_at[1])
    cv2.putText(imageArray, tmp, (x+gap*0+1,y+gap*0+26),cv2.FONT_HERSHEY_PLAIN, 0.6, [0,0,0] , 1, cv2.LINE_AA)
    tmp="trans_m_w:"+str(color_bt[0])+" trans_m_k:"+str(color_bt[1])
    cv2.putText(imageArray, tmp, (x+gap*0+1,y+gap*0+36),cv2.FONT_HERSHEY_PLAIN, 0.6, [0,0,0] , 1, cv2.LINE_AA)
    tmp="trans_y_w:"+str(color_ct[0])+" trans_y_k:"+str(color_ct[1])
    cv2.putText(imageArray, tmp, (x+gap*0+1,y+gap*0+46),cv2.FONT_HERSHEY_PLAIN, 0.6, [0,0,0] , 1, cv2.LINE_AA)

    #=====
    xoffset = x+barsize*0
    yoffset = y+barsize*1
    pixsize = 2
    pixgap = 3
    lim = barsize//pixsize
    for j in range(0,lim*10,1):
        for k in range(0,lim*10,1):
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

def makeimg(filename,color_a,color_ak,color_b,color_bk,color_c,color_ck,color_at,color_bt,color_ct):


    imageArray = np.zeros((height, width, 3), np.uint8)
    size = imageArray.shape[:2]
    
    for h in range(height):
        for w in range(width):
            imageArray[h, w] = color_bg
    #cv2.imwrite("blank.bmp", imageArray);
    #color_d=(195,201,202)

    print("===begin===")

    func_makeimg(imageArray,0,0,color_a,color_b,color_c,color_at,color_bt,color_ct)

    tmp="filename:"+filename
    print(filename)
    cv2.putText(imageArray, tmp, (1,1120),cv2.FONT_HERSHEY_PLAIN, 0.6, [0,0,0] , 1, cv2.LINE_AA)
    
    cv2.imwrite(filename, imageArray)
    print("=== end ===")

color_bg = [255,255,255]
color_font = [0,0,0]
width=1600
height=1200
gap = width//16
offset = height//4
barsize = width//16
pixsize = barsize
#色指定はそれぞれbgr順

#test用 CMYそれぞれ2色づつ設定
#color_a_num=1
#color_an=[1]
#color_a_in=[[198,196,180]]
#color_ak=[[130,124,109]]
#color_at=[75,0]

#color_b_num=1
#color_bn=[18]
#color_b_in=[[110,117,206]]
#color_bk=[[83,84,147]]
#color_bt=[72,0]

#color_c_num=1
#color_cn=[46]
#color_c_in=[[54,188,197]]
#color_ck=[[36,122,125]]
#color_ct=[84,0]

color_a_num=1
color_an=[2]
color_a_in=[[169,144,106]]
color_ak=[[125,103,72]]
color_at=[57,0]

color_b_num=1
color_bn=[18]
color_b_in=[[110,117,206]]
color_bk=[[83,84,147]]
color_bt=[72,0]

color_c_num=1
color_cn=[44]
color_c_in=[[18,169,178]]
color_ck=[[13,112,115]]
color_ct=[86,0]
    
#color_d=[255, 255, 255]

color_a=[[0],[0],[0]]
color_b=[[0],[0],[0]]
color_c=[[0],[0],[0]]
flg=0
for i in range(0,3):
    if(flg!=1):
        color_a[i]=color_a_in[0][i]*(100-color_at[0])//100 + 255*color_at[0]//100
    else:
        color_a[i]=color_a_in[0][i]
    if(flg!=1):
        color_b[i]=color_b_in[0][i]*(100-color_bt[0])//100 + 255*color_bt[0]//100
    else:
        color_b[i]=color_b_in[0][i]
    if(flg!=1):
        color_c[i]=color_c_in[0][i]*(100-color_ct[0])//100 + 255*color_ct[0]//100
    else:
        color_c[i]=color_c_in[0][i]

filename="img_plain_Xmy_c"+str(color_an[0]).rjust(3, '0')+"_m"+str(color_bn[0]).rjust(3, '0')+"_y"+str(color_cn[0]).rjust(3, '0')+".bmp"
makeimg(filename,color_ak[0],color_ak[0],color_b[0],color_bk[0],color_c[0],color_ck[0],color_at,color_bt,color_ct)

filename="img_plain_cXy_c"+str(color_an[0]).rjust(3, '0')+"_m"+str(color_bn[0]).rjust(3, '0')+"_y"+str(color_cn[0]).rjust(3, '0')+".bmp"
makeimg(filename,color_a[0],color_ak[0],color_bk[0],color_bk[0],color_c[0],color_ck[0],color_at,color_bt,color_ct)

filename="img_plain_cmX_c"+str(color_an[0]).rjust(3, '0')+"_m"+str(color_bn[0]).rjust(3, '0')+"_y"+str(color_cn[0]).rjust(3, '0')+".bmp"
makeimg(filename,color_a[0],color_ak[0],color_b[0],color_bk[0],color_ck[0],color_ck[0],color_at,color_bt,color_ct)

filename="img_plain_XXX_c"+str(color_an[0]).rjust(3, '0')+"_m"+str(color_bn[0]).rjust(3, '0')+"_y"+str(color_cn[0]).rjust(3, '0')+".bmp"
makeimg(filename,color_ak[0],color_ak[0],color_bk[0],color_bk[0],color_ck[0],color_ck[0],color_at,color_bt,color_ct)

filename="img_plain_cmy_c"+str(color_an[0]).rjust(3, '0')+"_m"+str(color_bn[0]).rjust(3, '0')+"_y"+str(color_cn[0]).rjust(3, '0')+".bmp"
makeimg(filename,color_a[0],color_a[0],color_b[0],color_bk[0],color_c[0],color_ck[0],color_at,color_bt,color_ct)
    
    
    
    
    
