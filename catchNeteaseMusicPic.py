import os
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
# weburl='http://music.163.com/#/artist/album?id=101988&limit=120&offset=0'
# driver = webdriver.PhantomJS()
# driver.get(weburl)
# driver.switch_to.frame("g_iframe")
# html = driver.page_source
#
# all_li=BeautifulSoup(html,'lxml').find(id='m-song-module').find_all('li')
#
# for li in all_li:
#     album_img = li.find('img')['src']
#     album_name = li.find('p', class_='dec')['title']
#     album_date = li.find('span', class_='s-fc3').get_text()
#     photo_name = album_date + ' - ' + album_name.replace('/', '').replace(':', ',') + '.jpg'
#     end_pos = album_img.index('?')
#     album_url = album_img[:end_pos]
#     print(album_url, photo_name)

class AlbumCover():
    def __init__(self):
        self.weburl='http://music.163.com/#/artist/album?id=101988&limit=120&offset=0'
        self.folder_path='D:\simpleStylePic'
    def request(self,url):
        r=requests.get(url)
        return r

    def save_img(self,url,filename):
        print("loading Picture......")
        img = self.request(url)
        print("save Pic......")
        f=open(filename,'ab')
        f.write(img.content)
        print(filename,"save success")
        f.close()
    def mkdir(self,path):
        path=path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print("create folder: ",path)
            os.makedirs(path)
            print("success")
            return True
        else:
            print("folder exists,do not need create it again")
            return False

    def get_files(self,path):
        pic_name=os.listdir(path)
        return pic_name

    def spider(self):
        print("start")
        driver=webdriver.PhantomJS()
        driver.get(self.weburl)
        driver.switch_to.frame("g_iframe")
        html=driver.page_source
        self.mkdir(self.folder_path)
        os.chdir(self.folder_path)
        filenames=self.get_files(self.folder_path)
        all_li = BeautifulSoup(html, 'lxml').find(id='m-song-module').find_all('li')
        for li in all_li:
            album_img = li.find('img')['src']
            album_name = li.find('p', class_='dec')['title']
            album_date = li.find('span', class_='s-fc3').get_text()
            end_pos=album_img.index('?')
            album_url=album_img[:end_pos]

            photo_name = album_date + ' - ' + album_name.replace('/', '').replace(':', ',') + '.jpg'
            print(album_url, photo_name)

            if photo_name in filenames:
                print('do not need downloaded again')
            else:
                self.save_img(album_url, photo_name)

album_cover=AlbumCover()
album_cover.spider()

# for li in all_li:
#     album_img = li.find('img')['src']
#     album_name = li.find('p', class_='dec')['title']
#     album_date = li.find('span', class_='s-fc3').get_text()
#     end_pos = album_img.index('?')
#     album_img_url = album_img[:end_pos]
#
#     photo_name = album_date + ' - ' + album_name.replace('/', '').replace(':', ',') + '.jpg'
#     print(album_img_url, photo_name)
#
#     if photo_name in file_names:
#         print('图片已经存在，不再重新下载')
#     else:
#         self.save_img(album_img_url, photo_name)


