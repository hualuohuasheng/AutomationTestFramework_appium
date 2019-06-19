# -*-coding:utf-8 -*-
# author:
# time:
#################

import requests


def download_img(url, img_save):
    # 获取到验证码图片的src链接后，下载保存到本地
    res = requests.get(url)
    with open(img_save, 'wb') as f:
        f.write(res.content)

url1 = 'http://necaptcha.nosdn.127.net/9d546e0a0ee4446b80a72807d6462c7e.jpg'
url2 = 'http://necaptcha.nosdn.127.net/ab127cbd881c4209a29bfc5a122efd84.png'

download_img(url1, 'icon.jpg')
download_img(url2, 'icon.png')