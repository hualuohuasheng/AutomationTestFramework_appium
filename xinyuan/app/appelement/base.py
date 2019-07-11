# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.is_android = 'desired' in driver.capabilities
        self.id_loc_base = 'com.ex55.app:id'

    @classmethod
    def locate_by_textview_name(cls, name):
        ele = [By.XPATH, f"//android.widget.TextView[@text='{name}']"] if cls.is_android else []
        return ele

    @classmethod
    def locate_by_button_name(cls, name):
        ele = [By.XPATH, f"//android.widget.Button[@text='{name}']"] if cls.is_android else []
        return ele
