# import requests
# payload ={'key1':'value1','key2':'value2'}
# r=requests.get('https://unsplash.com',params=payload)
# print(r.text)
#
# r=requests.post("http://httpbin.org/post",data=payload)
# print(r.text)
#
# r=requests.put("http://httpbin.org/put")
# print(r.text)
# r=requests.delete("http://httpbin.org/delete")
# print(r.text)
# r=requests.head("http://httpbin.org/get")
# print(r.text)
# r=requests.options("http://httpbin.org/get")
# print(r.text)

# from bs4 import BeautifulSoup
# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# """
# soup=BeautifulSoup(html_doc,'html.parser')
# find=soup.find('p')
# print("find's return type is ", type(find))
# print("find's content is", find)
# print("find's Tag Name is ", find.name)
# print("find's Attribute(class) is ", find['class'])
# print('NavigableString is：', find.string)
# u=soup.name
# print(u)
# head_tag=soup.head
# print(soup.p)
# title_tag=head_tag.contents[0]
#
# for child in title_tag.children:
#     print(child)
#
# title_tag=soup.title
# title_tag.string.parent
# print(soup.parent)
# link=soup.a
# link
# for parent in link.parents:
#     if parent is None:
#         print(parent)
#     else:
#         print(parent.name)
# import requests
# from bs4 import BeautifulSoup
# import os
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
#weburl='https://unsplash.com'
# weburl='http://www.simple-style.com/'
# r=requests.get(weburl,headers=headers)
#
# all_a=BeautifulSoup(r.text,'html.parser').find_all('img')
#print(BeautifulSoup(r.text,'html.parser').find_all('img'))
# for img in all_a:
#      print(img['src'])

#一个简单的pyhthon网页爬虫
import requests
from bs4 import BeautifulSoup
import os

class simpleStyle():
    def __init__(self): #类的初始化操作
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'} #给请求指定一个请求头来模拟chrome浏览器
        self.web_url='http://www.simple-style.com/'#要访问的网页地址
        self.folder_path='D:\simpleStylePic' #设置图片要存放的文件目录
    def request(self,url): #返回网页的response
        r=requests.get(url,headers=self.headers)
        return r
    def mkdir(self,path): ##这个函数创建文件夹
        path=path.strip()
        isExists=os.path.exists(path)
        if not isExists:
            print('create folder: ',path)
            os.makedirs(path)
            print('create success')
        else:
             print("folder is exists,do not need create it again")
    def save_img(self,url,name): ##保存图片
        print("start save pic ...")
        pic=self.request(url)
        file_name=name+'.jpg'
        print("start save file")
        f=open(file_name,'ab')
        f.write(pic.content)
        print(file_name,'save success')
        f.close()
    def get_pic(self):#主函数
        print("start get web...")
        r=self.request(self.web_url)
        print("start get tag...")
        all_a = BeautifulSoup(r.text, 'lxml').find_all('img')#获取网页中的class为cV68d的所有a标签
        print("start create folder")
        self.mkdir(self.folder_path)
        os.chdir(self.folder_path)
        i=1
        for img in all_a: #循环每个标签，获取标签中图片的url并且进行网络请求，最后保存图片
            self.save_img(img['src'],str(i))
            i+=1

getPic=simpleStyle()#创建类的实例
getPic.get_pic()#执行类中的方法