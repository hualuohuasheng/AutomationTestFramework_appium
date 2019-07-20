# -*- coding:utf-8 -*-

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import xinyuan.public_main as pub_func

# desired_caps = DesiredCapabilities.CHROME
# print(desired_caps)
# desired_caps['pageLoadStrategy'] = 'none'

# 对于输入网站后必须输入用户名和密码才能进入，
# 可以这种方式访问：http://username:password@url 如：admin:55.exchange@global.dev_test_uat_pub.55.exchange:5555/home/
url = "http://global.dev_test_uat.55.exchange"
driver = webdriver.Chrome()
driver.get(url)
driver.set_page_load_timeout(60)
login = WebDriverWait(driver, 30, 1).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'login')))

driver.maximize_window()
sleep(2)
driver.find_element_by_class_name('login').click()
sleep(3)
driver.find_element_by_xpath("//input[@type='text' and @class='ivu-input ivu-input-default']").send_keys('15811055254')
driver.find_element_by_xpath("//input[@type='password' and @class='ivu-input ivu-input-default']").send_keys('xinyuanlml0617')
driver.find_element_by_css_selector(".loginbtn").click()
sleep(2)

cut_img_element = (By.XPATH, "//img[@class='yidun_jigsaw']")
back_img_element = (By.XPATH, "//img[@class='yidun_bg-img']")
slider_element = (By.XPATH, "//div[@class='yidun_slider']")
WebDriverWait(driver, 30, 1).until(expected_conditions.presence_of_element_located(back_img_element))
WebDriverWait(driver, 30, 1).until(expected_conditions.presence_of_element_located(cut_img_element))
pub_func.slider_verification_code_163yidun(driver, cut_img_element, back_img_element, slider_element)


driver.find_element_by_link_text('订单').click()
sleep(10)
