# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 21:13:41 2017

@author: Alwayswdc
@project: Turing Robot and Baiduyiyin Demo
需要下载百度语音合成的第三方库，也就是这个aip库，详见百度语音官网
"""
import urllib,json
from aip import AipSpeech
import os
import time
import win32api
import win32gui
import win32con
from multiprocessing import Process
from music import *



##语音合成模块
def say(text):
    # 定义常量
    APP_ID = '6752465'
    API_KEY = 'F2YEpcgLHg5taERxAzvDfVGX'
    SECRET_KEY = 'PCrZsfE95KDFNBmkkkfgaGhEr7fDVcCD'
    # 初始化AipSpeech对象
    aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result  = aipSpeech.synthesis(text, 'zh', 1, {'vol': 5,})
    with open('auido.mp3', 'wb') as f:
        f.write(result)
        f.close()
    os.system("mpg123-win32.exe auido.mp3")

##图灵聊天模块    
def chat(text='hello'):
    url = 'http://www.tuling123.com/openapi/api'
    key = '65fd73e1a68f4fcd8c2305b2fc71b903'
    uid = '12345'
    
    parmas = urllib.parse.urlencode({
            'key':key,
            'info':text,
            'userid':uid
            }).encode(encoding='UTF8')

    res = urllib.request.urlopen(url,parmas)
    res = res.readall().decode('utf-8')
    res = json.loads(res)
    text = res['text']
    say(text)
    print ('susan说:',text)


##输入与互动进程
def main_thread():
    F6 = 0x75
    while True:        
        win32api.keybd_event(F6,0,0,0)
        time.sleep(0.05)
        win32api.keybd_event(F6,0 ,win32con.KEYEVENTF_KEYUP ,0)
        
        input_words = ""
        for line in iter(input,"~~~~~不可能完成的任务~~~~~~"):
            input_words += line
            if " " in input_words or "？" in input_words:
                break
        print("您说："+input_words)
        
        win32api.keybd_event(F6,0,0,0)
        time.sleep(0.05)
        win32api.keybd_event(F6,0 ,win32con.KEYEVENTF_KEYUP ,0)
        
        if "播放" in input_words or "一首" in input_words or "音乐" in input_words or "歌曲" in input_words or "歌" in input_words:
            play(input_words)
        else:  
            chat(input_words)
        
##不停回车
def hawk_enter():
    appname = "语音机器人"
    enter = 0x0D
    count = 0
    while True:
        if count % 10 == 0:
            window = win32gui.FindWindow(None, appname)
            try:
                win32gui.SetForegroundWindow(window)
            except:
                pass
        if window != 0:
            win32api.keybd_event(enter,0,0,0)
            time.sleep(0.05)
            win32api.keybd_event(enter,0 ,win32con.KEYEVENTF_KEYUP ,0)
        time.sleep(1)
        count += 1
      
      
if __name__ == '__main__':
    
    worker = Process(target=hawk_enter, args=())
    worker.start()
    main_thread()

     

    
