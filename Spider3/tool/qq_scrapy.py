from selenium import webdriver
import time

def login_lagou():
    # 动态连接到火狐浏览器
    browser=webdriver.Firefox(executable_path=r'E:\workplace\geckodriver.exe')
    # 获取网站信息
    browser.get("https://mail.qq.com/")
    # 休眠
    time.sleep(5)
    # 模拟登陆将用户名以及密码传送进去
    browser.switch_to.frame('login_frame')
    browser.find_element_by_id("switcher_plogin").click()

    browser.find_element_by_id('u').send_keys("921730779")

    browser.find_element_by_id("p").send_keys("921730779qian")

    browser.find_element_by_id("login_button").click()



    cookie_dict = {}
    time.sleep(3)
    Cookies = browser.get_cookies()
    print(Cookies)
    for cookie in Cookies:
        cookie_dict[cookie['name']] = cookie['value']
    browser.quit()
    print(cookie_dict)
    return cookie_dict


if __name__ == '__main__':
    login_lagou()