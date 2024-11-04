# !/usr/bin/env python
# coding: utf-8

import os
import stat
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException

from LOGGER import GetLogger

logger = GetLogger(logger_name="XiaoHongShu", debug=False, log_file="XiaoHongShu.log")

USERPATH = os.path.abspath("./userData")

if not os.path.exists(USERPATH):
    os.mkdir(USERPATH)
    # 赋予所有用户完全访问权限
    os.chmod(USERPATH, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 设置权限为 77

chrome_options = Options()

# 使用用户数据目录
chrome_options.add_argument(f"--user-data-dir={USERPATH}")
chrome_options.add_argument("--window-size=1280,720")
service = Service('./chromedriver.exe')

driver = webdriver.Chrome(options=chrome_options, service=service)

# 定义常量
LOGIN_CONTAINER_CLASS = 'login-container'
LOGIN_BTN_CLASS = 'login-btn'
USER_BTN_CLASS = 'user'
XIAOHONGSHU_URL = 'https://www.xiaohongshu.com/explore'

# 登录函数
def login():
    driver.get(XIAOHONGSHU_URL)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, LOGIN_CONTAINER_CLASS)))
    except TimeoutException:
        try:
            login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, LOGIN_BTN_CLASS)))
            login_button.click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, LOGIN_CONTAINER_CLASS)))
        except:
            logger.error("登录失败")
            return False
    logger.info("请使用手机扫码登录，请不要关闭登录页面否则会导致程序报错")
    
    while True:
        try:
            WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, LOGIN_CONTAINER_CLASS)))
            if driver.find_elements(By.CLASS_NAME, LOGIN_BTN_CLASS):
                logger.warning("不要关闭登录页面，请正常扫码登录！")
                driver.find_element(By.CLASS_NAME, LOGIN_BTN_CLASS).click()
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, LOGIN_CONTAINER_CLASS)))
            elif driver.find_elements(By.CLASS_NAME, USER_BTN_CLASS):
                logger.info("登录成功！")
                return True
            else:
                logger.error("登录失败，发生了未知的错误!")
                return False
        except Exception as e:
            logger.info("页面已经刷新...5秒后重启登录")
            logger.info("如果您发现页面的二维码已经刷新请手动点击刷新")
            time.sleep(5)

if __name__ == '__main__':
    if login():
        logger.info("登录成功,这下可以直接运行App.py了")
    else:
        logger.error("登录失败，请检查您的网络连接和登录信息")