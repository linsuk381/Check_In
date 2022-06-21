from util import *
import time

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码

@retry(stop_max_attempt_number=5)
def hupu():
    try:
        driver = get_web_driver()
        driver.get("https://leshuyun.com/login")
        driver.find_element_by_xpath("//input[@id='emailInp']").send_keys(username)
        driver.find_element_by_xpath("//input[@id='emailPwdInp']").send_keys(password)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//a[contains(text(),'点我签到~')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[contains(text(),'我要签到')]").click()
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    hupu()
