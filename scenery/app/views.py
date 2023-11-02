from django.shortcuts import render
from app.models import Pic 
# Create your views here.

import numpy as np
import cv2
from matplotlib import pyplot as plt
import glob 
import os 
from sklearn.cluster import KMeans
from keras.preprocessing.image import  img_to_array
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from sklearn.datasets import make_blobs
import matplotlib
matplotlib.use("Agg")



def index(request):
    #照片傳入接口
   
        #==========================================================
        
 
        ##照片儲存 呈現在前端
    a="3e2e123123"
    return render(request,"index.html",locals())

def result(request):
    
    #照片傳入接口
   
        
    user_image_list=[]
    if request.method == "POST":
        user_img = request.FILES.get('user_image')
        #user_image_list.append(img_to_array(Image.open(user_img)))   
        #print(user_image_list)
        
        # 讀取訓練照片資料集 
        image_list=[]
        test_list=[]

        train_label=[] #根據迴圈讀取的資料夾 當作label 的依據 去製作對應的label矩陣，並且用位置去對應
        count=0 
        picture_number=0 
        picture_num_label=[]
        picture_name_label=[]
        picture_list=[]
        for i in glob.glob(os.path.join("static/image_2/","*")): 
            #for j in glob.glob(os.path.join(i,"*")):
                picture_list.append(i)
                image_list.append(img_to_array(Image.open(i))/255) # 正規化 
                #print(image_list)
                #print(i.split("/")[-1].split("_")[0]) # 取出訓練集照片的檔名作為label 
                picture=i.split(".")[0] # 
                #print(picture)
                picture_num_label.append(int(picture.split("-")[-1]))# 取出訓練集照片讀入順序的label
                picture_name_label.append(picture.split("-")[0]) # 取出訓練集照片讀入順序的地名
        #print(picture_num_label)    #類別數字label

        #print(len(picture_name_label))  #地名
        #print(picture_name_label)
        
        # 使用者照片讀取 並加入原本的資料庫的資料中的最後面(原本12張圖 +1 張等於13張)
        image_list.append(img_to_array(Image.open(user_img))/255) 

        #print(len(image_list))

        arr=np.array(image_list) # img to array 
        print("全部訓練資料的陣列: ",arr.shape) 
        
        
        data=arr.reshape(13,250*250*3) 
        print(data.shape)
        kmeans=KMeans(n_clusters=3)
        kmeans=kmeans.fit(data) # 訓練
        clusterIndex= kmeans.predict(data)  # 目前是使用原本資料去cluster 

        print("預測結果=",clusterIndex)
        print(picture_num_label)
        # 使用者的圖片被加在最後，所以分類類別的結果就是list 最後一個
        print(clusterIndex[-1])
        
        
        #原始資料的label 和預測後的數字的對應 
        # 因為kmean的標籤是隨機的。 
        
        dic={}
        for i in range(len(picture_num_label)): 
            if picture_num_label[i] != clusterIndex[i]:
                dic[picture_num_label[i]]=clusterIndex[i] 
            else: 
                dic[picture_num_label[i]]=clusterIndex[i]
                
        print("原始資料的label和分群後的label的hash table=", dic) 

        print("預測結果的label(在原始資料集)= ",clusterIndex[-1])

        for i in dic: 
            if dic[i]==clusterIndex[-1]: #查看kmean分群後的標籤，是看原始資料的哪個label。 
                predict_label=i  #找到了要取出key
                specific_label=i
        predict_label=str(predict_label)
        print("預測結果的label(在原始資料集)= ",predict_label)

        
        
        #產生相近的圖片，以及地點
        #print(picture_list)
        relate_image_list=[]
        for i in picture_list:
            pic_label=i.split(".")[0].split("-")[-1]  #取出照片庫中，所有和使用者圖片相符的label的圖片
            #print(type(pic_label))
            if pic_label==predict_label:
                relate_image_list.append(i.split("/")[-1])
        
        
        print("圖片檔名稱=",relate_image_list)
        unit = Pic.objects.filter(pic_label=specific_label)
        #unit=Pic.objects.all()

        
        
        #相關的圖片的地名
        relate_image_name_list=[]
        for i in relate_image_list: 
            relate_image_name_list.append(i.split("-")[0])
        print("地名名稱", relate_image_name_list)
        
        
    a=relate_image_name_list
    return render(request,"result.html",locals())



