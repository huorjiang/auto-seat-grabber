# -*- coding: utf-8 -*-
"""
预科晚自习自动抢座脚本 v0.1
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime

# ---------- 你只要改下面这几行就行 ----------
学号 = "123456789"                    # ← 测试随便填
密码 = "666666"                        # ← 测试随便填
抢座时间 = "00:01:00"                  # ← 改成现在时间+1分钟（比如现在23:59就写00:01:00）
网址 = "https://www.baidu.com"         # ← 测试用百度网址
# ----------------------------------------

print("抢座脚本启动成功！正在等待时间...")
print(f"目标抢座时间：{抢座时间}")

while True:
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"当前时间：{now}", end="\r")  # 实时显示时间
    
    if now >= 抢座时间:
        print("\n时间到！开始抢座！")
        
        # 打开浏览器
        driver = webdriver.Chrome()
        driver.get(网址)                   # ← 改成用上面定义的网址
        
        print("浏览器已打开百度，测试成功！脚本雏形完成！")
        break
    
    time.sleep(1)  # 每秒检查一次时间
