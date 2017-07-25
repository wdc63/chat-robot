
import requests
import json
import webbrowser
import time
import os


header = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'music.163.com',
            'Referer': 'http://music.163.com/search/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'
        }
default_timeout = 10

def rawHttpRequest(method, action, query=None, urlencoded=None, callback=None, timeout=None):
        if (method == 'GET'):
            url = action if (query == None) else (action + '?' + query)
            connection = requests.get(url, headers=header, timeout=default_timeout)
        elif (method == 'POST'):
            connection = requests.post(
                action,
                data=query,
                headers=header,
                timeout=default_timeout
            )

        connection.encoding = "UTF-8"
        return connection.text

def httpRequest(method, action, query=None, urlencoded=None, callback=None, timeout=None):
        
        connection = json.loads(rawHttpRequest(method, action, query, urlencoded, callback, timeout))
        return connection


def search(s, stype=1, offset=0, total='true', limit=10):
        action = 'http://music.163.com/api/search/get'
        data = {
            's': s,
            'type': stype,
            'offset': offset,
            'total': total,
            'limit': limit
        }
        try:
            result = httpRequest('POST', action, data)["result"]["songs"]
        except:
            data = {
                's': "随机",
                'type': stype,
                'offset': offset,
                'total': total,
                'limit': limit
            }
            result = httpRequest('POST', action, data)["result"]["songs"]
        
        final_result=[]
        for i in result:
            final_result.append([i["duration"],i["name"],i["id"],i["fee"]])
        print(final_result)
        return final_result

def play(name):

    name = name.replace("一首","")
    name = name.replace("音乐","")
    name = name.replace("播放","")
    name = name.replace("歌曲","")
    name = name.replace("歌","")
    name = name.replace("给我","")
    name = name.replace("放歌","")
    name = name.replace("放","")
    
    songlist = search(name)
    print(songlist)
    if len(songlist) < 1:
        return False
    else:
        for i in songlist:
            totaltime = i[0]
            songid = i[2]
            fee = i[3]
            if totaltime/1000 < 420 and fee<1:
                break

        url = r"http://music.163.com/outchain/player?type=2&id="+str(songid)+"&auto=1&height=66"
        webbrowser.open(url)
        count = 0
        while True:
            if count > int(totaltime/1000)-1:
                os.system('taskkill /F /IM chrome.exe')
                break
            time.sleep(1)
            count += 1
            print(count,int(totaltime/1000)-1)
        return True    
