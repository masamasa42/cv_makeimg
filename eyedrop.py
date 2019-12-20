# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 10:35:42 2019

@author: manakamura
"""
import cv2
import sys

#1行目に要素についての説明文を追加
#ファイルパスが含まれているのは、どのファイルが該当するか確認の為

def edrop(filepath):
    #ファイルを開いて中身からrgbの値を取り出す
    #出力用の文字列形式にrgbの値を設定して返す

    img_drop = cv2.imread(filepath)
    height, width, color = img_drop.shape
    
    drop_y=height//2 #画像中央位置
    drop_x=width//2 #同上
    check_height=18
    check_width=18

    #例外的に画像が小さいケースに対応
    if(check_height>height):
        check_height=height-2
    if(check_width>width):
        check_width=width-2
    
    b=[]
    g=[]
    r=[]
    for y in range(drop_y-(check_height//2),drop_y+(check_height//2)):
        for x in range(drop_x-(check_width//2),drop_x+(check_width//2)):
            b.append(img_drop[y,x][0])
            g.append(img_drop[y,x][1])
            r.append(img_drop[y,x][2])
    #中央値取得
    b.sort()
    g.sort()
    r.sort()
    tmp=check_height*check_width//2#中央値のindex

    ret_str = ""
    ret_str += filepath
    ret_str += ","+str(height)
    ret_str += ","+str(width)
    ret_str += ","+str(b[tmp])
    ret_str += ","+str(g[tmp])
    ret_str += ","+str(r[tmp])
#    ret_str += ""
#    print(r)

    return ret_str

#main    
out_str="" #ファイル出力用文字列
if(len(sys.argv)>1):
    out_str+="filepath,height,width,b,g,r\n"#1行目 項目名
    for i in range(1,len(sys.argv)):
        #入力の各画像ファイルについて実施
        #out_str += "---\n"
        #print(sys.argv[i])
        out_str += edrop(sys.argv[i])
        out_str += "\n"
    #print(out_str)
    file = open('out.csv', 'w')#出力ファイル名 固定
    file.write(out_str)
    file.close()
else:
    print("hoge")#引数無い場合
    

    