# -*- coding:utf-8 -*-


class 首页:

    def __init__(self, driver):
        self.driver = driver
        self.is_android = 'desired' in driver.desired_capabilities

    @property
    def 首页按钮(self):
        if self.is_android:
            return self.driver.find_element_by_id("com.ex55.app:id/activity_main_iv_main")
        else:
            return self.driver.find_element_by_id("")


