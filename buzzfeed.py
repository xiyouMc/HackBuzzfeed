#coding:utf-8
from datetime import datetime
import requests
import json
import time
import os
startPage = '/videos?render_template=0&page=0'
print('开始爬取Buzzfeed视频，每隔20分钟刷新一次。。。')
def requestBuzzfeed(page):
    print datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    s = requests.get('https://www.buzzfeed.com'+page)
    print(s.status_code)
    result = json.loads(s.text)
    cards = result["cards"]
    nextPage = result["nextPage"]
    if nextPage is None:
        print('Video Over,刷新中... 等待20分钟')
        time.sleep(1*60*20)
        requestBuzzfeed(startPage)
    else:
        if cards == []:
            print('card is null!')
        else:
            print("write file.")
            f = open('videos/' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S')+'.json','w')
            f.write(json.dumps(cards))
            f.close()
        requestBuzzfeed(nextPage)
if os.path.exists('videos'):
    print('视频JSON文件保存在videos文件夹中...')
else:
    os.makedirs(r'videos')
requestBuzzfeed(startPage)
