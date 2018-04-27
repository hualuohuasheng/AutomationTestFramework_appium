#coding=utf-8

import unittest


from appium import webdriver
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'mate7'#安卓随便输入机型即可
desired_caps['appPackage'] = 'com.powerinfo.pi_iroom.demo'
desired_caps['appActivity'] = '.setting.LoginSettingActivity'
desired_caps['autoAcceptAlerts'] = 'true'
desired_caps['noReset'] = 'true'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

gen = "com.powerinfo.pi_iroom.demo:id/"
driver.find_element_by_id(gen + "iv_create_room").click()
driver.find_element_by_id(gen + "iv_setting").click()
driver.find_element_by_id(gen + "mEtBitrate").clear()
driver.find_element_by_id(gen + "mEtBitrate").send_keys('400')
# driver.find_element_by_id(gen + "mSpFps").click()
# driver.find_element_by_android_uiautomator('15').click()
# driver.find_element_by_name("15").click()
# driver.find_element_by_id(gen + "mSpOutputSize").click()
# driver.find_element_by_android_uiautomator('640*360').click()
# driver.find_element_by_name("640*360").click()

driver.find_element_by_id(gen + "bt_developer").click()
driver.find_element_by_id(gen + "mPtcpLog").is_enabled()

driver.find_element_by_id(gen + "mBtnDeleteLog").click()

driver.back()

driver.find_element_by_id(gen + "bt_start").click()






sleep(3)

# driver.quit()
