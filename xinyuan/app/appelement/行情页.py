# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from xinyuan.app.appelement.base import BasePage


class 行情页(BasePage):

    def 行情页按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/activity_main_ll_quote"] if self.is_android else [MobileBy.ACCESSIBILITY_ID, '行情']
        return self.driver.find_element(ele[0], ele[1])

    def 行情页搜索按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llSearchImg"] if self.is_android else [MobileBy.ACCESSIBILITY_ID, 'serch icon']
        return self.driver.find_element(ele[0], ele[1])

    def 行情页搜索_币种编辑框(self):
        ele = [By.ID, f"{self.id_loc_base}/etSearchInput"] if self.is_android else [By.CLASS_NAME, 'XCUIElementTypeTextField']
        return self.driver.find_element(ele[0], ele[1])

    def 行情页搜索_取消按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/searchBack"] if self.is_android else [MobileBy.ACCESSIBILITY_ID, '取消']
        return self.driver.find_element(ele[0], ele[1])

    def 自选通证按钮(self):
        if self.is_android:
            ele = [By.ID, f"{self.id_loc_base}/tvTab00"]
            return self.driver.find_elements(ele[0], ele[1])[0]
        else:
            return self.driver.find_element(MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeScrollView[1]/XCUIElementTypeOther[1]')

    def 区块链通证按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvTab01"] if self.is_android else [MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeScrollView[1]/XCUIElementTypeOther[2]']
        return self.driver.find_elements(ele[0], ele[1])[0]

    def 外汇通证按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvTab03"] if self.is_android else [MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeScrollView[1]/XCUIElementTypeOther[3]']
        return self.driver.find_elements(ele[0], ele[1])[0]

    def 潮牌通证按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvTab04"] if self.is_android else [MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeScrollView[1]/XCUIElementTypeOther[4]']
        return self.driver.find_elements(ele[0], ele[1])[0]

    def 编辑通证按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/ivEditImg"] if self.is_android else [By.ID, 'quotes edit']
        return self.driver.find_element(ele[0], ele[1])

    def 编辑通证_添加按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvEditAdd"] if self.is_android else [MobileBy.ACCESSIBILITY_ID, '添加']
        return self.driver.find_element(ele[0], ele[1])

    def 搜索_结果(self):
        ele = [By.ID, f"{self.id_loc_base}/tvSearchListName"] if self.is_android else [MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell/XCUIElementTypeButton[1]']
        return self.driver.find_element(ele[0], ele[1])

    def 编辑通证_勾选自选按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llFavoritesEdit"] if self.is_android else [MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell/XCUIElementTypeButton[2]']
        return self.driver.find_element(ele[0], ele[1])

    def 编辑通证_完成按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvFavoriteFinish"] if self.is_android else [MobileBy.ACCESSIBILITY_ID, '完成']
        return self.driver.find_element(ele[0], ele[1])

    def 编辑通证_勾选按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/cbFavoritesEdit"] if self.is_android else [MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell/XCUIElementTypeButton']
        return self.driver.find_elements(ele[0], ele[1])

    def 编辑通证_交易对币种(self):
        ele = [By.ID, f"{self.id_loc_base}/tvListName"] if self.is_android else [MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeCell/XCUIElementTypeButton']
        return self.driver.find_elements(ele[0], ele[1])

    def 编辑通证_交易对计价币种(self):
        ele = [By.ID, f"{self.id_loc_base}/tvListNameBase"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 编辑通证_置顶按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llFavoritesTop"] if self.is_android else [MobileBy.ACCESSIBILITY_ID, 'top icon']
        return self.driver.find_elements(ele[0], ele[1])

    def 编辑通证_全选按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/cbFavoritesEditAll"] if self.is_android else [MobileBy.ACCESSIBILITY_ID, '全选']
        return self.driver.find_element(ele[0], ele[1])

    def 编辑通证_删除按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llFavoriteDelete"] if self.is_android else [MobileBy.ACCESSIBILITY_ID, '删除']
        return self.driver.find_element(ele[0], ele[1])

    def 币种列表_币种名称(self):
        ele = [By.ID, f"{self.id_loc_base}/tvListName"] if self.is_android else [By.XPATH, "//XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText[1]"]
        return self.driver.find_elements(ele[0], ele[1])

    def 币种列表_币种计价方式名称(self):
        ele = [By.ID, f"{self.id_loc_base}/tvListNameBase"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 币种列表_24H量(self):
        ele = [By.ID, f"{self.id_loc_base}/tvVol"] if self.is_android else [By.XPATH, "//XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText[2]"]
        return self.driver.find_elements(ele[0], ele[1])

    def 币种列表_最新价格按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvPrice"] if self.is_android else [By.XPATH, "//XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText[3]"]
        return self.driver.find_elements(ele[0], ele[1])

    def 币种列表_换算为当前资产计价方式按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvCurrencyPrice"] if self.is_android else [By.XPATH, "//XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText[4]"]
        return self.driver.find_elements(ele[0], ele[1])

    def 币种列表_涨跌幅按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvChange"] if self.is_android else [By.XPATH, "//XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeStaticText[5]"]
        return self.driver.find_elements(ele[0], ele[1])

    # BTC, ETH。。
    def 选择币种计价方式(self, name):
        if self.is_android:
            ele = super().locate_by_textview_name(name)
        else:
            ele = [MobileBy.ACCESSIBILITY_ID, name]
        return self.driver.find_element(ele[0], ele[1])

    def 币种列表_名称排序按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvNameDefault"] if self.is_android else [By.XPATH, '//XCUIElementTypeStaticText[@name="名称"]/..']
        return self.driver.find_element(ele[0], ele[1])

    def 币种列表_最新价排序按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvPriceDefault"] if self.is_android else [By.XPATH, '//XCUIElementTypeStaticText[@name="最新价"]/..']
        return self.driver.find_element(ele[0], ele[1])

    def 币种列表_涨跌幅排序按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvPercentTop"] if self.is_android else [By.XPATH, '//XCUIElementTypeStaticText[@name="涨跌幅"]/..']
        return self.driver.find_element(ele[0], ele[1])

    def 行情详情_返回按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llMarketsReturn"] if self.is_android else [MobileBy.ACCESSIBILITY_ID, 'quoteReturn']
        return self.driver.find_element(ele[0], ele[1])

    def 行情详情_标题(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMarketsTitle"] if self.is_android else [By.XPATH, '//XCUIElementTypeNavigationBar/XCUIElementTypeStaticText/XCUIElementTypeStaticText']
        return self.driver.find_element(ele[0], ele[1])

    def 行情详情_分享按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llMarketsShare"] if self.is_android else [MobileBy.ACCESSIBILITY_ID, 'qupteShare']
        return self.driver.find_element(ele[0], ele[1])

    def 行情详情_分享_保存图片按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/ivLogo"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 行情详情_自选按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llMarketsFavorites"] if self.is_android else [MobileBy.ACCESSIBILITY_ID, 'Collection']
        return self.driver.find_element(ele[0], ele[1])

    def 行情详情_市场价格(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMarketPrice"] if self.is_android else [MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeApplication/XCUIElementTypeCell/XCUIElementTypeStaticText[1]']
        return self.driver.find_element(ele[0], ele[1])

    def 行情详情_当前计价方式价格(self):
        ele = [By.ID, f"{self.id_loc_base}/tvCurrency"] if self.is_android else [MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeApplication/XCUIElementTypeCell/XCUIElementTypeStaticText[2]']
        return self.driver.find_element(ele[0], ele[1])

    def 行情详情_涨跌幅百分比(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMarketPercent"] if self.is_android else [MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeApplication/XCUIElementTypeCell/XCUIElementTypeStaticText[3]']
        return self.driver.find_element(ele[0], ele[1])

    def 行情详情_最低价(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMarket24Low"] if self.is_android else [MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeApplication/XCUIElementTypeCell/XCUIElementTypeStaticText[6]']
        return self.driver.find_element(ele[0], ele[1])

    def 行情详情_最高价(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMarket24High"] if self.is_android else [MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeApplication/XCUIElementTypeCell/XCUIElementTypeStaticText[7]']
        return self.driver.find_element(ele[0], ele[1])

    def 行情详情_24H量(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMarket24Vol"] if self.is_android else [MobileBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeApplication/XCUIElementTypeCell/XCUIElementTypeStaticText[8]']
        return self.driver.find_element(ele[0], ele[1])

    # 时间分段
    def 行情详情_时间分段(self, name):
        ele = super().locate_by_textview_name(name) if self.is_android else [MobileBy.ACCESSIBILITY_ID, name]
        return self.driver.find_element(ele[0], ele[1])

    def 行情详情_时间分段_更多(self):
        ele = [By.ID, f"{self.id_loc_base}/llTabMore"] if self.is_android else [MobileBy.ACCESSIBILITY_ID, '更多']
        return self.driver.find_element(ele[0], ele[1])

    def 行情详情_时间分段_指标(self):
        ele = [By.ID, f"{self.id_loc_base}/llTabIndex"] if self.is_android else [MobileBy.ACCESSIBILITY_ID, '指标']
        return self.driver.find_element(ele[0], ele[1])

    def 行情详情_买入按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llStockBuy"] if self.is_android else [MobileBy.ACCESSIBILITY_ID, '买入']
        return self.driver.find_element(ele[0], ele[1])

    def 行情详情_卖出按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llStockBuy"] if self.is_android else [MobileBy.ACCESSIBILITY_ID, '卖出']
        return self.driver.find_element(ele[0], ele[1])
