# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 10:35:42 2019

@author: manakamura
"""
import cv2
import os
import sys
from tkinter import messagebox

def makeimg(outfilename, tile):
    d_width=800
    d_height=600
    t_height, t_width, t_channels = tile.shape[:3]
    
    h_count=d_height//t_height -1
    w_count=d_width//t_width -1
    if(h_count<1):
        h_count=1
    if(w_count<1):
        w_count=1
    im_v = tile
    for h in range(1,h_count):
        im_v = cv2.vconcat([im_v, tile])
    im_h = im_v
    for w in range(1,w_count):
        im_h = cv2.hconcat([im_h, im_v])
    #print(outfilename)
    #tmp="filename:"+outfilename
    #cv2.putText(imageArray, tmp, (1,1120),cv2.FONT_HERSHEY_PLAIN, 0.6, [0,0,0] , 1, cv2.LINE_AA)
    cv2.imwrite(outfilename, im_h)

#main
filepath="in.bmp"
if(len(sys.argv)==2):
    #1ファイルドロップ実行時 タイル処理を行った画像を出力する
    filepath=sys.argv[1]

    tmp="filepath:"+filepath
    print(tmp)
    if (os.path.exists(filepath)==False):
        messagebox.showerror("program stopped","\"in.bmp\" is not exist")
        quit
        #sys.exit()
    tile = cv2.imread(filepath)
    outfilename = "out"
    outfilename += "_tile"
    outfilename += ".bmp"
    makeimg(outfilename, tile)
elif(len(sys.argv)==4):
    #3ファイルドロップ実行時 delta処理 mosaic処理を行った画像を出力する
    a = cv2.imread(sys.argv[1])
    b = cv2.imread(sys.argv[2])
    c = cv2.imread(sys.argv[3])
    im_v1 = cv2.hconcat([a,b])
    im_v2 = cv2.hconcat([im_v1,c])
    t_height, t_width, t_channels = b.shape[:3]
    d = b[0:t_height,0:t_width//2]
    e = b[0:t_height,t_width//2:t_width]
   
    #delta
    im_v3 = cv2.hconcat([e,c])
    im_v4 = cv2.hconcat([im_v3,a])
    im_v5 = cv2.hconcat([im_v4,d])
    tile = cv2.vconcat([im_v2, im_v5])
    outfilename = "out"
    outfilename += "_delta3"
    outfilename += ".bmp"
    makeimg(outfilename, tile)

    #mosaic
    im_tmp = cv2.hconcat([a,b])
    im_v1 = cv2.hconcat([im_tmp,c])
    im_tmp = cv2.hconcat([b,c])
    im_v2 = cv2.hconcat([im_tmp,a])
    im_tmp = cv2.hconcat([c,a])
    im_v3 = cv2.hconcat([im_tmp,b])
    im_h1 = cv2.vconcat([im_v1, im_v2])
    tile = cv2.vconcat([im_h1, im_v3])
    outfilename = "out"
    outfilename += "_mosaic3"
    outfilename += ".bmp"
    makeimg(outfilename, tile)
elif(len(sys.argv)==5):
    #4ファイルドロップ実行時 4ファイルでのmosaic処理を行った画像を出力する
    a = cv2.imread(sys.argv[1])
    b = cv2.imread(sys.argv[2])
    c = cv2.imread(sys.argv[3])
    d = cv2.imread(sys.argv[4])
    im_v1 = cv2.vconcat([a,b])
    im_v2 = cv2.vconcat([c,d])
    tile = cv2.hconcat([im_v1, im_v2])
    outfilename = "out"
    outfilename += "_mosaic4"
    outfilename += ".bmp"
    makeimg(outfilename, tile)
else:
    #引数無しで実行時 テスト用の画像を使用してタイル処理を行った画像を出力する
    tmp="filepath:"+filepath
    print(tmp)
    if (os.path.exists(filepath)==False):
        messagebox.showerror("program stopped","\"in.bmp\" is not exist")
        quit
        #sys.exit()
    tile = cv2.imread(filepath)
    outfilename = "out"
    outfilename += "_tile"
    outfilename += ".bmp"
    makeimg(outfilename, tile)



print("complete")
#input("push enter to exit")
