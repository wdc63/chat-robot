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
from multiprocessing import Process



def enter():
    time.sleep(2)
    appname = "语音机器人"
    enter = 0x0D
    window = win32gui.FindWindow(None, appname)
    try:
        win32gui.SetForegroundWindow(window)
    except:
        pass
    win32api.keybd_event(enter,0,0,0)
    time.sleep(0.1)
    win32api.keybd_event(enter,0,0,0)
    time.sleep(0.1)
    win32api.keybd_event(enter,0,0,0)
    time.sleep(0.1)
    win32api.keybd_event(enter,0,0,0)
    time.sleep(0.1)
    win32api.keybd_event(enter,0,0,0)
    time.sleep(0.1)

enter()

     

    
