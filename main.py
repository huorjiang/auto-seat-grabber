import time
import datetime
from selenium import webdriver

# 1分钟后自动打开百度测试
目标时间 = (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime("%H:%M:%S")
print(f"脚本启动！将在 {目标时间} 打开百度测试")

while True:
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"当前时间：{now}  等待中...", end="\r")
    if now >= 目标时间:
        print("\n时间到！打开浏览器...")
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com")
        print("成功打开百度！脚本正常！")
        time.sleep(10)
        driver.quit()
        break
    time.sleep(1)
