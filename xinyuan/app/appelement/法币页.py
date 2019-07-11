# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from xinyuan.app.appelement.base import BasePage


class 法币页(BasePage):

    def 法币页按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/activity_main_ll_exchange"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 选择法币买卖页签(self, name):
        ele = super().locate_by_textview_name(name)
        return self.driver.find_element(ele[0], ele[1])

    def 选择法币币种页签(self, name):
        ele = super().locate_by_textview_name(name)
        return self.driver.find_element(ele[0], ele[1])

    def 法币页广告_名称(self):
        ele = [By.ID, f"{self.id_loc_base}/tvNickName"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 法币页广告_数量(self):
        ele = [By.ID, f"{self.id_loc_base}/tvAmountOTC"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 法币页广告_最小限额(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMaxLimit"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 法币页广告_最大限额(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMaxLimit"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 法币页广告_银行卡(self):
        ele = [By.ID, f"{self.id_loc_base}/sdvBank"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 法币页广告_支付宝(self):
        ele = [By.ID, f"{self.id_loc_base}/sdvAliPay"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 法币页广告_微信(self):
        ele = [By.ID, f"{self.id_loc_base}/sdvWeChat"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 法币页广告_拍拍(self):
        ele = [By.ID, f"{self.id_loc_base}/sdvPayPal"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 法币页广告_订单数量(self):
        ele = [By.ID, f"{self.id_loc_base}/tvOrderCountOTC"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 法币页广告_百分比(self):
        ele = [By.ID, f"{self.id_loc_base}/tvFactorOTC"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 法币页广告_单价(self):
        ele = [By.ID, f"{self.id_loc_base}/tvPriceOTC"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 法币页广告_购买出售按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvTradeBuyOTC"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 下单页_买卖币种(self):
        ele = [By.ID, f"{self.id_loc_base}/tvCurrencyOTC"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 下单页_单价(self):
        ele = [By.ID, f"{self.id_loc_base}/tvPricePopOTC"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 下单页_数量或交易额编辑框(self):
        ele = [By.ID, f"{self.id_loc_base}/etInputAmountOTC"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 下单页_数量或交易额类型(self):
        ele = [By.ID, f"{self.id_loc_base}/tvInputAmountType"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 下单页_交易数量(self):
        ele = [By.ID, f"{self.id_loc_base}/tvAllAmountOTC"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 下单页_交易数量类型(self):
        ele = [By.ID, f"{self.id_loc_base}/tvAmountTypeOTC"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 下单页_最小限额(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMinLimitOTC"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 下单页_最大限额(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMaxLimitOTC"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 下单页_交易密码(self):
        ele = [By.ID, f"{self.id_loc_base}/etTradePassword"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 下单页_取消按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/btnTradeCancel"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 下单页_立即下单按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llTradeBuyOTC"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 下单页_交易总额(self):
        ele = [By.ID, f"{self.id_loc_base}/tvOTCPriceCNY"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 法币页_增加广告(self):
        if self.is_android:
            xpath = "//android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/" \
                   "android.widget.ImageButton[1]"
        else:
            xpath = ""
        return self.driver.find_element(By.XPATH, xpath)

    def 法币页广告_管理广告按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/img_03"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 管理广告_广告标题(self):
        ele = [By.ID, f"{self.id_loc_base}/tvOrderSide"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 管理广告_广告币种(self):
        ele = [By.ID, f"{self.id_loc_base}/tvCurrency"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 管理广告_广告状态(self):
        ele = [By.ID, f"{self.id_loc_base}/tvOrderStatus"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 管理广告_单价(self):
        ele = [By.ID, f"{self.id_loc_base}/tvPriceValue"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 管理广告_数量(self):
        ele = [By.ID, f"{self.id_loc_base}/tvAmountValue"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 管理广告_已成交量(self):
        ele = [By.ID, f"{self.id_loc_base}/tvStatusValue"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 管理广告_限额(self):
        ele = [By.ID, f"{self.id_loc_base}/tvLimit"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 管理广告_交易货币(self):
        ele = [By.ID, f"{self.id_loc_base}/tvFaitType"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 管理广告_广告编号(self):
        ele = [By.ID, f"{self.id_loc_base}/tvAdvertNumber"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 管理广告_订单时间(self):
        ele = [By.ID, f"{self.id_loc_base}/tvAdvertDate"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 管理广告_查看成交明细(self):
        ele = [By.ID, f"{self.id_loc_base}/tvAdvertDetail"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 管理广告_取消广告(self):
        ele = [By.ID, f"{self.id_loc_base}/tvCancelAdvert"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 法币页广告_发布广告按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/img_02"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 发布广告_买卖币种(self):
        ele = [By.ID, f"{self.id_loc_base}/tvUseCurrency"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 发布广告_使用法币(self):
        ele = [By.ID, f"{self.id_loc_base}/tvUseFaitOne"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 发布广告_买卖价格(self):
        ele = [By.ID, f"{self.id_loc_base}/etSellPrice"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 发布广告_买卖数量(self):
        ele = [By.ID, f"{self.id_loc_base}/etSellNumber"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 发布广告_买卖数量_全部(self):
        ele = [By.ID, f"{self.id_loc_base}/tvTotal"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 发布广告_总金额(self):
        ele = [By.ID, f"{self.id_loc_base}/etSellTotalPrice"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 发布广告_交易方式(self):
        ele = [By.ID, f"{self.id_loc_base}/tvPayTypeSelect"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 发布广告_最小限额(self):
        ele = [By.ID, f"{self.id_loc_base}/etMinLimit"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 发布广告_最小限额_帮助(self):
        ele = [By.ID, f"{self.id_loc_base}/ivMinHelp"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 发布广告_最大限额(self):
        ele = [By.ID, f"{self.id_loc_base}/etMaxLimit"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 发布广告_最大限额_帮助(self):
        ele = [By.ID, f"{self.id_loc_base}/ivMaxHelp"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 发布广告_交易备注(self):
        # 下单后极速付款，到账后请及时放币
        # 请勿在汇款备注内填写比特币、BTC、OTC等任何数字币有关字眼，防止您的汇款被银行拦截
        ele = [By.ID, f"{self.id_loc_base}/etRemark"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 发布广告_发布广告按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvSendAdvert"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 法币页广告_取消X按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/img_01"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 法币页更多设置(self):
        ele = [By.ID, f"{self.id_loc_base}/ivTradeMore"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 法币页更多设置_法币设置(self):
        ele = super().locate_by_textview_name('法币设置')
        return self.driver.find_element(ele[0], ele[1])

    def 法币页更多设置_法币设置_选择法币(self, name):
        ele = super().locate_by_textview_name(name)
        return self.driver.find_element(ele[0], ele[1])

    def 划转页面_币种(self):
        ele = [By.ID, f"{self.id_loc_base}/tvCurrency"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 划转页面_选择币种(self, name):
        ele = super().locate_by_textview_name(name)
        return self.driver.find_element(ele[0], ele[1])

    def 划转页面_账户交换(self):
        ele = [By.ID, f"{self.id_loc_base}/cbTransfer"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 划转页面_from账胡(self):
        ele = [By.ID, f"{self.id_loc_base}/tvFromAccount"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 划转页面_to账户(self):
        ele = [By.ID, f"{self.id_loc_base}/tvToAccount"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 划转页面_划转数量编辑框(self):
        ele = [By.ID, f"{self.id_loc_base}/etNumber"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 划转页面_全部按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvTotal"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 划转页面_当前划转币种类型(self):
        ele = [By.ID, f"{self.id_loc_base}/tvCurrencyType"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 划转页面_账户可用(self):
        ele = [By.ID, f"{self.id_loc_base}/tvTotalMoney"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 划转页面_划转按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvTransfer"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 划转页面_划转记录按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/custom_header_iv_right_btn"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 划转页面_划转记录_数量(self):
        ele = [By.ID, f"{self.id_loc_base}/tvNumber"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 划转页面_划转记录_类型(self):
        ele = [By.ID, f"{self.id_loc_base}/tvType"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 划转页面_划转记录_时间(self):
        ele = [By.ID, f"{self.id_loc_base}/tvDate"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 订单记录_标题(self):
        ele = [By.ID, f"{self.id_loc_base}/tvOrderSide"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 订单记录_币种(self):
        ele = [By.ID, f"{self.id_loc_base}/tvCurrency"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 订单记录_订单状态(self):
        ele = [By.ID, f"{self.id_loc_base}/tvOrderStatus"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 订单记录_订单时间(self):
        ele = [By.ID, f"{self.id_loc_base}/tvTime"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 订单记录_订单数量(self):
        ele = [By.ID, f"{self.id_loc_base}/tvQuantity"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 订单记录_交易金额(self):
        ele = [By.ID, f"{self.id_loc_base}/tvTotalMoney"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 订单记录_交易对象名称(self):
        ele = [By.ID, f"{self.id_loc_base}/tvOrderNickName"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 订单记录_订单详情_交易总额(self):
        ele = [By.ID, f"{self.id_loc_base}/tvOrderPayedTotalMoney"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 订单记录_订单详情_交易单价(self):
        ele = [By.ID, f"{self.id_loc_base}/tvPayedOrderPrice"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 订单记录_订单详情_交易数量(self):
        ele = [By.ID, f"{self.id_loc_base}/tvOrderPayedQuantity"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 订单记录_订单详情_支付方式(self):
        ele = [By.ID, f"{self.id_loc_base}/tvPayedPayTypeTitle"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 订单记录_订单详情_收款人(self):
        ele = [By.ID, f"{self.id_loc_base}/tvOrderPayedNickName"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 订单记录_订单详情_账号(self):
        ele = [By.ID, f"{self.id_loc_base}/tvOrderPayedAccount"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 订单记录_订单详情_订单号(self):
        ele = [By.ID, f"{self.id_loc_base}/tvOrderIdPayed"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 订单记录_订单详情_申诉(self):
        ele = [By.ID, f"{self.id_loc_base}/tvTradePayedComplaint"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 订单记录_取消订单详情_交易总额(self):
        ele = [By.ID, f"{self.id_loc_base}/tvFinishTotalMoney"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 订单记录_取消订单详情_收款人(self):
        ele = [By.ID, f"{self.id_loc_base}/tvFinishNickname"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 订单记录_取消订单详情_交易单价(self):
        ele = [By.ID, f"{self.id_loc_base}/tvFinishPrice"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 订单记录_取消订单详情_交易数量(self):
        ele = [By.ID, f"{self.id_loc_base}/tvFinishQuantity"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 订单记录_取消订单详情_下单时间(self):
        ele = [By.ID, f"{self.id_loc_base}/tvFinishOrderDate"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 订单记录_取消订单详情_订单号(self):
        ele = [By.ID, f"{self.id_loc_base}/tvFinishOrderId"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 收款方式_收款类型(self):
        ele = [By.ID, f"{self.id_loc_base}/tvPayType"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 收款方式_收款人姓名(self):
        ele = [By.ID, f"{self.id_loc_base}/tvName"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 收款方式_收款账号(self):
        ele = [By.ID, f"{self.id_loc_base}/tvContent"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 收款方式_编辑按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/editPay"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 收款方式_编辑_保存按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvSave"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 收款方式_编辑_编辑框(self):
        ele = [By.ID, f"{self.id_loc_base}/etContent"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 收款方式_编辑_添加二维码按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/simpleDraweeView"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 收款方式_编辑_相机拍照按钮(self):
        ele = super().locate_by_textview_name('拍照')
        return self.driver.find_element(ele[0], ele[1])

    def 收款方式_编辑_相机_拍照(self):
        ele = [By.ID, f"{self.id_loc_base}/take_photo"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 收款方式_添加按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/custom_header_tv_right_btn"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 我的昵称_昵称编辑框(self):
        ele = [By.ID, f"{self.id_loc_base}/etAccountNickName"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 我的昵称_保存按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/btnEditNickName"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])
