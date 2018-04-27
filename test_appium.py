


#coding=utf-8
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['deviceName'] = 'CSX0217629006119'#华为荣耀9
desired_caps['appPackage'] = 'com.powerinfo.pi_iroom.demo'
desired_caps['appActivity'] = '.setting.LoginSettingActivity'
desired_caps['autoAcceptAlerts'] = 'true'
desired_caps['noReset'] = 'true'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_id("com.powerinfo.pi_iroom.demo:id/mEtNdSelect").send_keys("999")
driver.find_element_by_id("com.powerinfo.pi_iroom.demo:id/mEtGroupId").send_keys("iRoom")
driver.find_element_by_id("com.powerinfo.pi_iroom.demo:id/mBtnStart").click()



sleep(3)

# driver.quit()
