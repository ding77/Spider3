#coding:utf-8
#爬取微信好友头像并进行拼接
import itchat
import math
import PIL.Image as Image
import os
#登录
itchat.auto_login()
#获取好友信息
friends = itchat.get_friends(update=True)[0:]
#获取好友头像并保存在目录文件夹下
num = 0
for friend in friends:
    image = itchat.get_head_img(userName=friend["UserName"]) #用 itchat.get_head_img(userName=None)来爬取好友列表的头像
    fileImage = open("E:\微信图片" + "/" + str(num) + ".jpg",'wb') #将好友头像下载到本地文件夹
    fileImage.write(image)
    fileImage.close()
    num += 1

#将微信图像进行拼接
dirs = os.listdir("E:\微信图片")
each_size = int(math.sqrt(float(1800*1900)/len(dirs)))
line = int(1900/each_size)#每行的个数
photographic = Image.new("RGB",(1800,1900))#设置新生成图片的格式以及大小
# 初始化每行每列的图片个数
x = 0
y = 0
for i in range(0,len(dirs)): 
    try:
        imageOfFriends = Image.open("E:\微信图片" + "/" + str(i) + ".jpg") #打开一张照片，PIL库的应用
    except IOError:
        print ("error")
    else:
        # 缩小图片
        image_resize = imageOfFriends.resize((each_size,each_size))
        # 拼接图片
        photographic.paste(image_resize,(x*each_size,y*each_size)) 
        x += 1
        if x == line:#达到每行的个数就换行
            x = 0
            y += 1
#保存图像，发送给文件助手，显示图像
photographic.save("E:\微信图片" + "/" + "all.jpg")
itchat.send_image("E:\微信图片" + "/" + "all.jpg","filehelper") #把图片发送给微信文件助手（filehelper
photographic.show()