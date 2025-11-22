# -*- coding: utf-8 -*-
"""
预科晚自习自动抢座脚本 v0.1
作者：你的大名（GitHub用户名）
功能：每天固定时间打开浏览器，准备抢座
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime

# ---------- 你只要改下面这几行就行 ----------
学号 = "你的学号"          # ← 改成你的
密码 = "你的密码"          # ← 改成你的
抢座时间 = "22:00:00"      # 教务系统开放抢座的时间，比如22:00:00
# ----------------------------------------

print("抢座脚本启动成功！正在等待时间...")
print(f"目标抢座时间：{抢座时间}")

while True:
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"当前时间：{now}", end="\r")  # 实时显示时间
    
    if now >= 抢座时间:
        print("\n时间到！开始抢座！")
        
        # 打开浏览器
        driver = webdriver.Chrome()  # 第一次运行会让你下载ChromeDriver，我后面教你
        driver.get("你们学校的教务系统网址")  # ← 这里改成你们预科抢座的网址
        
        # 后面我们再慢慢加登录、点击座位等代码
        print("浏览器已打开，脚本雏形完成！")
        break
    
    time.sleep(1)  # 每秒检查一次时间