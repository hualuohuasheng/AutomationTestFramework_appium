# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.is_android = 'desired' in driver.capabilities
        self.id_loc_base = 'com.ex55.app:id'

    def locate_by_textview_name(self, name):
        ele = f"//android.widget.TextView[@text='{name}']" if self.is_android else f"//XCUIElementTypeStaticText" \
            f"[@name='{name}']"
        return [By.XPATH,ele]

    def locate_by_button_name(self, name):
        ele = f"//android.widget.Button[@text='{name}']" if self.is_android else f"//XCUIElementTypeButton[@name" \
            f"='{name}']"
        return [By.XPATH, ele]

    def 选择页签(self, name):
        ele = self.locate_by_textview_name(name)
        return self.driver.find_element(ele[0], ele[1])

    def button(self, name):
        ele = self.locate_by_button_name(name)
        return self.driver.find_element(ele[0], ele[1])

    def 返回(self):
        ele = [By.ID, f"{self.id_loc_base}/custom_header_iv_back"] if self.is_android else [By.ID, 'fanhui']
        return self.driver.find_element(ele[0], ele[1])
