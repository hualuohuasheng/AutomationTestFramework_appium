# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from xinyuan.app.appelement.base import BasePage


class 币币页(BasePage):

    # 首页上进入用户页面的按钮
    def 币币页按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/activity_main_ll_personal"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 币种标题显示(self):
        ele = [By.ID, f"{self.id_loc_base}/tvTradeCoinsTitle"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 搜索按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/custom_header_iv_right_btn"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 搜索输入框(self):
        ele = [By.ID, f"{self.id_loc_base}/etSearchInput"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 搜索_取消按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/searchBack"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 搜索_清除搜索内容按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/ivSearchDelete"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 搜索_结果(self):
        ele = [By.ID, f"{self.id_loc_base}/tvSearchListName"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 币种标签选择(self, page):
        ele = [By.XPATH, f"//android.widget.TextView[@text='{page}']"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 币种选择(self):
        ele = [By.XPATH, f"//android.widget.TextView[@text='XRP/USDT']"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 获取所有币种(self, coins):
        ele = [By.XPATH, f"//android.widget.TextView[@id='{self.id_loc_base}/tvListName' and contains(@text, '{coins}')]"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 获取指定币种的最新价(self, coins):
        ele = [By.XPATH, f"//android.widget.TextView[@id='{self.id_loc_base}/tvListName' and contains(@text, '{coins}')]"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 买入标签按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/rbTradeBuy"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 卖出标签按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/rbTradeSell"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 价格编辑框(self):
        ele = [By.ID, f"{self.id_loc_base}/etInputPrice"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 数量编辑框(self):
        ele = [By.ID, f"{self.id_loc_base}/etInputAmount"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 价格减少按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/btnTradeOrderPriceSubtract"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 价格增加按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/btnTradeOrderPriceAdd"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 换算价格显示(self):
        ele = [By.ID, f"{self.id_loc_base}/tvCurrencyMoney"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 币种可用数量显示(self):
        ele = [By.ID, f"{self.id_loc_base}/tradeOrderAvailable"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 数量比例按钮(self, percent):
        ele = [By.ID, f"{self.id_loc_base}/btnPercent{percent}"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 成交金额显示(self):
        ele = [By.ID, f"{self.id_loc_base}/tvResultPrice"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 买入按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvTradeOrder"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 卖出按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvTradeOrder"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 全部按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvLookAll"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 订单价格(self, price):
        ele = [By.XPATH, f"//android.widget.TextView[@text='{price}']"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 订单数量(self, amount):
        ele = [By.XPATH, f"//android.widget.TextView[@text='{amount}']"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 左上行情按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/ivTradeCoinsMarket"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 右上更多功能按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llTradeCoinsMore"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 充值按钮(self):
        ele = [By.XPATH, f"//android.widget.TextView[@text='充值']"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 历史委托按钮(self):
        ele = [By.XPATH, f"//android.widget.TextView[@text='历史委托']"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 获取盘口所有价格(self):
        ele = [By.ID, f"{self.id_loc_base}/tvDepthItemPrice"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 获取盘口所有数量(self):
        ele = [By.ID, f"{self.id_loc_base}/tvDepthItemAmount"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 获取当前委托所有订单币种(self):
        ele = [By.ID, f"{self.id_loc_base}/tvSymbol"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    #  订单是买入还是卖出
    def 获取当前委托所有订单状态(self):
        ele = [By.ID, f"{self.id_loc_base}/tvStatus"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 获取当前委托所有订单价格(self):
        ele = [By.ID, f"{self.id_loc_base}/tvPrice"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 获取当前委托所有订单数量(self):
        ele = [By.ID, f"{self.id_loc_base}/tvAmount"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 获取当前委托所有订单日期(self):
        ele = [By.ID, f"{self.id_loc_base}/tvOrderDateTime"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 获取当前委托所有订单时间(self):
        ele = [By.ID, f"{self.id_loc_base}/tvOrderTime"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 获取当前委托所有订单取消(self):
        ele = [By.ID, f"{self.id_loc_base}/tvCancel"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 历史委托_筛选按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/custom_header_tv_right_btn"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 历史委托_筛选_币种编辑框(self):
        ele = [By.ID, f"{self.id_loc_base}/etCoinsTitle"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 历史委托_筛选_选择计价单位(self):
        ele = [By.ID, f"{self.id_loc_base}/cbCoinsType"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 历史委托_筛选_计价单位(self, name):
        ele = [By.XPATH, f"//android.widget.TextView[@text='{name}']"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 历史委托_筛选_重置按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/btnScreeningReset"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 历史委托_筛选_确认按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/btnScreeningEnter"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 历史委托_筛选_table按钮(self, name):
        ele = [By.XPATH, f"//android.widget.TextView[@text='{name}']"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])



