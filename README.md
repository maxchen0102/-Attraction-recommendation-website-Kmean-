#  台灣景點推薦網站(基於機器學習Kmean方法)

# 解決問題： 
以往想去類似景點的地方的時候，會不知道如何下關鍵字找不到台灣的類似景點。
但透過這個系統，只要有當地的照片，這個系統會使用機器學習Kmean方法進行運算，來推薦類似景點的地方給使用者，可以更精準的找到台灣的類似景點，同時結合觀光局的網頁和簡介，可以更方便安排旅程，增加台灣國人的旅遊率。




# 網站介紹：
以下為系統流程圖

![](https://hackmd.io/_uploads/HkZJZCtWa.png)

首頁下方紅色框處，可以傳送您最近去過的景點，系統會使用機器學習Kmean方法，推薦給您類似風景的台灣景點。

![](https://hackmd.io/_uploads/Hyn5i2HZ6.png)

這邊假設使用者傳入下圖(台南的沙灘照)，想要去類似的台灣景點。並上傳系統

![](https://hackmd.io/_uploads/SyOzhhSbT.png)

系統會推薦給您台灣相似的景點，並且附上這個景點的簡介(取自交通部觀光局的官方簡介) 且這邊是透過機器學習Kmean演算法，來計算圖片像素得出的。
這邊種共會推薦四個

![](https://hackmd.io/_uploads/SyL2s6tbp.png)


![](https://hackmd.io/_uploads/ByraoTYbT.png)


另外，每個景點可以按下紅框處的按鈕，可以前往交通部觀光局的網站，可以觀看觀光局針對此景點的更多描述，還有旅遊建議，方便使用者快速規劃行程。

![](https://hackmd.io/_uploads/BJhET3rZ6.png)

下圖為連結到的觀光局網站，裡面有此推薦地點的詳細介紹。

![](https://hackmd.io/_uploads/BkUaahrb6.png)

下圖為輸入北橫山中照片的推薦結果

![](https://hackmd.io/_uploads/SJRNc6KW6.png)

![](https://hackmd.io/_uploads/BJw8cTYbT.png)







---
# 使用技術：
1. Kmean機器學習演算法
2. Django 網站框架 
3. Bootstrap 
4. python 
5. HTML &CSS 
6. SQLite 資料庫系統 