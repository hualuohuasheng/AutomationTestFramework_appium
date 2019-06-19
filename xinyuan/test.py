# -*- coding:utf-8 -*-
from PIL import Image
from selenium import webdriver
from time import sleep
import pickle
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

# desired_caps = DesiredCapabilities.CHROME
# print(desired_caps)
# desired_caps['pageLoadStrategy'] = 'none'

driver = webdriver.Chrome()

# 对于输入网站后必须输入用户名和密码才能进入，
# 可以这种方式访问：http://username:password@url
# admin:55.exchange@global.dev_test_uat_pub.55.exchange:5555/home
url = "http://global.dev_test_uat.55.exchange:5555"
driver.get(url)
driver.set_page_load_timeout(60)
login = WebDriverWait(driver, 30, 1).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'login')))

driver.maximize_window()
sleep(5)
driver.find_element_by_class_name('login').click()
sleep(3)
driver.find_element_by_xpath("//input[@type='text' and @class='ivu-input ivu-input-default']").send_keys('15811055254')
driver.find_element_by_xpath("//input[@type='password' and @class='ivu-input ivu-input-default']").send_keys('xinyuanlml0617')
driver.find_element_by_css_selector(".loginbtn").click()
# driver.find_element_by_xpath('loginbtn ivu-btn ivu-btn-primary').click()
sleep(5)
location1 = driver.find_element_by_xpath("//img[@class='yidun_bg-img']").location
size1 = driver.find_element_by_xpath("//img[@class='yidun_bg-img']").size
print(location1,size1)

location2 = driver.find_element_by_xpath("//img[@class='yidun_jigsaw']").location
size2 = driver.find_element_by_xpath("//img[@class='yidun_jigsaw']").size
print(location2, size2)

# driver.save_screenshot('test-1.png')
src_1 = driver.find_element_by_xpath("//img[@class='yidun_bg-img']").get_property('src')
print(src_1)
driver.find_element_by_xpath("//img[@class='yidun_bg-img']").screenshot('test-1.png')
driver.find_element_by_xpath("//img[@class='yidun_jigsaw']").screenshot('test-2.png')
driver.find_element_by_xpath("//div[@class='yidun_slider']").click()
sleep(20)

cookies = driver.get_cookies()

driver.find_element_by_link_text('订单').click()
sleep(10)

driver.close()
driver.get(url)
for i in cookies:
    driver.add_cookie(i)
