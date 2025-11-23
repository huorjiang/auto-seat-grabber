import time
from selenium import webdriver

print("脚本已启动，10秒后用 Edge 打开百度……")
time.sleep(10)        # 倒计时10秒，够你准备拍照

# 直接用你电脑自带的 Edge，不下载任何驱动，永不被墙！
options = webdriver.EdgeOptions()
# 下这一行可以隐藏“Chrome 正受自动化软件控制”提示条（更清爽）
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Edge(options=options)
driver.get("https://www.baidu.com")

print("成功！百度已经打开！有30秒时间拍照，然后自动关闭")
time.sleep(30)        # 给你30秒尽情拍照
driver.quit()
print("脚本结束，完美！")

print("来水个日活")
