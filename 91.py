from util import *

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码
img_path = os.getcwd() + "/1.png"

@retry(stop_max_attempt_number=5)
def check_in_91():
    try:
        driver = get_web_driver()
        driver.get("https://leshuyun.com/login")
        driver.find_element_by_xpath("//input[@id='emailInp']").send_keys(username)
        driver.find_element_by_xpath("//input[@id='emailPwdInp']").send_keys(password)
        driver.find_element_by_xpath("//button[@type='submit']").click()

        WebDriverWait(driver, 10).until(driver.find_element_by_xpath("//a[contains(text(),'点我签到~')]")).click()
        # driver.find_element_by_xpath("//a[contains(text(),'点我签到~')]").click() # 点击'签到' 按钮
        if driver.find_elements_by_xpath("//button[contains(text(),'我要签到')]") != []:
            driver.find_element_by_xpath("//button[contains(text(),'我要签到')]").click()
            print('签到成功')
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    check_in_91()
