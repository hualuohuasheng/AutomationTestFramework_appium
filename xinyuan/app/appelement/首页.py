# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from xinyuan.app.appelement.base import BasePage


class 首页(BasePage):

    def 首页按钮(self):
        if self.is_android:
            return self.driver.find_element_by_id("com.ex55.app:id/activity_main_iv_main")
        else:
            return self.driver.find_element_by_id("")

    def 广场按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/custom_header_iv_close"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 群组按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llSocialGroups"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 好友按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llSocialChannels"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 首页_法币交易(self):
        ele = [By.ID, f"{self.id_loc_base}/rlTradeOTC"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 首页_公告中心(self):
        ele = [By.ID, f"{self.id_loc_base}/rlAnnouncementCenter"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 首页_帮助中心(self):
        ele = [By.ID, f"{self.id_loc_base}/rlHelpCenter"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 首页_h5网页关闭按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/custom_header_iv_close"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 首页_标题(self):
        ele = [By.ID, f"{self.id_loc_base}/custom_header_tv_title"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 首页_币种最新价(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMarketsMainPrice"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 首页_币种涨跌幅(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMarketsMainChange"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 首页_币种名称(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMarketsMainTopLeft"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 首页_币种计价方式(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMarketsMainTopRight"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 首页_外汇币种名称(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMarketsMainBottom"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])
