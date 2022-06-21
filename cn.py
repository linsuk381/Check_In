# -*- coding: UTF-8 -*-
from util import *
import time

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码

@retry(stop_max_attempt_number=5)
def hupu():
    try:
        driver = get_web_driver()
        driver.get("https://dy.justcn2.xyz/auth/login")
        driver.find_element_by_xpath("//input[@id='email']").send_keys(username)
        driver.find_element_by_xpath("//input[@id='passwd']").send_keys(password)
        driver.find_element_by_xpath("//button[@id='login']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[@id='checkin']").click()
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    hupu()
