# encoding: utf-8
import wget #导入模块
print("链接")
url=input() #文件链接
print("放哪？包括文件名")
dizi=input() #存放位置
wget.download(url,dizi)