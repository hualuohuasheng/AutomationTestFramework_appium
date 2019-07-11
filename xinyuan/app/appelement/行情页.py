# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from xinyuan.app.appelement.base import BasePage


class 行情页(BasePage):

    def 行情页按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/activity_main_ll_quote"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 行情页搜索按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llSearchImg"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 行情页搜索_币种编辑框(self):
        ele = [By.ID, f"{self.id_loc_base}/etSearchInput"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 行情页搜索_取消按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/searchBack"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 自选通证按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvTab00"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])[0]

    def 区块链通证按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvTab01"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])[0]

    def 外汇通证按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvTab03"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])[0]

    def 潮牌通证按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvTab04"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])[0]

    def 编辑通证按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/ivEditImg"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 编辑通证_添加按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvEditAdd"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 编辑通证_勾选自选按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llFavoritesEdit"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 编辑通证_完成按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvFavoriteFinish"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 编辑通证_勾选按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/cbFavoritesEdit"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 编辑通证_交易对币种(self):
        ele = [By.ID, f"{self.id_loc_base}/tvListName"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 编辑通证_交易对计价币种(self):
        ele = [By.ID, f"{self.id_loc_base}/tvListNameBase"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 编辑通证_置顶按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llFavoritesTop"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 编辑通证_全选按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/cbFavoritesEditAll"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 编辑通证_删除按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llFavoriteDelete"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 币种列表_币种名称(self):
        ele = [By.ID, f"{self.id_loc_base}/tvListName"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 币种列表_币种计价方式名称(self):
        ele = [By.ID, f"{self.id_loc_base}/tvListNameBase"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 币种列表_24H量(self):
        ele = [By.ID, f"{self.id_loc_base}/tvVol"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 币种列表_最新价格按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvPrice"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 币种列表_换算为当前资产计价方式按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvCurrencyPrice"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 币种列表_涨跌幅按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvChange"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    # BTC, ETH。。
    def 选择币种计价方式(self, name):
        ele = super().locate_by_textview_name(name)
        return self.driver.find_element(ele[0], ele[1])

    def 币种列表_名称排序按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvNameDefault"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 币种列表_最新价排序按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvPriceDefault"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 币种列表_涨跌幅排序按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvPercentTop"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 行情详情_自选按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llMarketsFavorites"] if self.is_android else []
        return self.driver.find_elemens(ele[0], ele[1])

    def 行情详情_市场价格(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMarketPrice"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 行情详情_当前计价方式价格(self):
        ele = [By.ID, f"{self.id_loc_base}/tvCurrency"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 行情详情_涨跌幅百分比(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMarketPercent"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 行情详情_最低价(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMarket24Low"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 行情详情_最高价(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMarket24High"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 行情详情_24H量(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMarket24Vol"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    # 时间分段
    def 行情详情_时间分段(self, name):
        ele = super().locate_by_textview_name(name)
        return self.driver.find_element(ele[0], ele[1])

    def 行情详情_时间分段_更多(self):
        ele = [By.ID, f"{self.id_loc_base}/llTabMore"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 行情详情_时间分段_指标(self):
        ele = [By.ID, f"{self.id_loc_base}/llTabIndex"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 行情详情_买入按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llStockBuy"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 行情详情_卖出按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llStockBuy"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])
