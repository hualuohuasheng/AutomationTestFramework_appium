# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from xinyuan.app.appelement.base import BasePage


class 资产页(BasePage):

    def 资产页按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/activity_main_ll_marge_trade"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 资产页_设置按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/ivSettingImg"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 资产页_币币账户按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/rBtnTransferExchange"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 资产页_法币账户按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/rBtnTransferFiat"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 资产页_资产汇总_标题按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvBalancesTitle"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 资产页_资产汇总_隐藏显示资产按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/cbHideValue"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 资产页_资产汇总_资产合计显示(self):
        ele = [By.ID, f"{self.id_loc_base}/tvBalancesUSD"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 资产页_资产汇总_换算金额显示(self):
        ele = [By.ID, f"{self.id_loc_base}/tvBalancesFiat"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 资产页_币种资产_勾选隐藏小额资产按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/slideSwitch"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 资产页_币种资产_隐藏小额资产提示按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvHideMinMoneyTip"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 资产页_币种资产_搜索按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/searchBtn"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 资产页_币种资产_搜索编辑框(self):
        ele = [By.ID, f"{self.id_loc_base}/etSearch"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 资产页_币种资产_搜索取消按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvCancelSearch"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 资产页_币种资产_币种名称(self):
        ele = [By.ID, f"{self.id_loc_base}/tvBalancesName"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 资产页_币种资产_币种计价方式(self):
        ele = [By.ID, f"{self.id_loc_base}/tvBalancesVol"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 资产页_币种资产_币种基数名称(self):
        ele = [By.ID, f"{self.id_loc_base}/tvBalancesVol"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 资产页_币种资产_币种数量(self):
        ele = [By.ID, f"{self.id_loc_base}/tvBalancesAmount"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 资产页_币种资产_币种换算金额(self):
        ele = [By.ID, f"{self.id_loc_base}/tvBalancesAmountFiat"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 资产页_资产细节_历史按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/custom_header_tv_right_btn"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 资产页_资产细节_币种名称(self):
        ele = [By.ID, f"{self.id_loc_base}/tvSymbolName"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 资产页_资产细节_币种计价方式(self):
        ele = [By.ID, f"{self.id_loc_base}/tvSymbolNameTip"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 资产页_资产细节_总额(self):
        ele = [By.ID, f"{self.id_loc_base}/tvBalancesTotal"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 资产页_资产细节_可用余额(self):
        ele = [By.ID, f"{self.id_loc_base}/tvBalancesAvailable"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 资产页_资产细节_下单冻结(self):
        ele = [By.ID, f"{self.id_loc_base}/tvBalancesInOrder"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 资产页_资产细节_充值按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/btnBalancesDeposits"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 充值页面_充值地址(self):
        ele = [By.ID, f"{self.id_loc_base}/tvDepositAddress"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 充值页面_复制地址按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llCopyAddress"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 充值页面_充值备注(self):
        ele = [By.ID, f"{self.id_loc_base}/tvDepositRemark"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 充值页面_复制备注按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llCopyRemark"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 充值页面_查看备注二维码按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llShowRemarkQRCode"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 充值页面_查看二维码按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llShowQRCode"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 充值页面_查看二维码_地址(self):
        ele = [By.ID, f"{self.id_loc_base}/tvViewDepositAddress"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 充值页面_查看二维码_复制地址按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/btnViewCopyAddress"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 充值页面_查看二维码_保存二维码按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/btnViewSaveAddress"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 充值页面_查看二维码_关闭按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/ivCloseView"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 资产页_资产细节_提现按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/btnBalancesWithdrawal"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 提现页面_提现历史(self):
        ele = [By.ID, f"{self.id_loc_base}/custom_header_tv_right_btn"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 提现页面_历史记录_交易对(self):
        ele = [By.ID, f"{self.id_loc_base}/tvBalancesPair"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 提现页面_历史记录_数量(self):
        ele = [By.ID, f"{self.id_loc_base}/tvBalancesAmount"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 提现页面_历史记录_状态(self):
        ele = [By.ID, f"{self.id_loc_base}/tvBalancesStatus"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 提现页面_历史记录_日期(self):
        ele = [By.ID, f"{self.id_loc_base}/tvBalancesTime"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 提现页面_历史记录_提现地址(self):
        ele = [By.ID, f"{self.id_loc_base}/tvBalancesAddress"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 提现页面_历史记录_提现id(self):
        ele = [By.ID, f"{self.id_loc_base}/tvBalancesTxid"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 提现页面_历史记录_提现备注(self):
        ele = [By.ID, f"{self.id_loc_base}/tvBalancesRemark"] if self.is_android else []
        return self.driver.find_elements(ele[0], ele[1])

    def 提现页面_可用余额(self):
        ele = [By.ID, f"{self.id_loc_base}/tvAvailableBalance"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 提现页面_提现数量编辑框(self):
        ele = [By.ID, f"{self.id_loc_base}/tvAvailableBalance"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 提现页面_全部按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/etWithdrawAmount"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 提现页面_手续费(self):
        ele = [By.ID, f"{self.id_loc_base}/tvWithdrawalFEE"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 提现页面_手续费类型(self):
        ele = [By.ID, f"{self.id_loc_base}/tvFeeType"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 提现页面_提现地址编辑框(self):
        ele = [By.ID, f"{self.id_loc_base}/etWithdrawalAddress"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 提现页面_二维码按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/ivShowQRCode"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 提现页面_地址下拉按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llWithdrawAddress"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 提现页面_历史地址(self):
        ele = [By.ID, f"{self.id_loc_base}/tvAddressInfo"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 提现页面_历史地址备注(self):
        ele = [By.ID, f"{self.id_loc_base}/tvAddressTitle"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 提现页面_历史地址币种名称(self):
        ele = [By.ID, f"{self.id_loc_base}/tvAddressTitleName"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 提现页面_新增地址按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/llWithdrawAddAddress"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 提现页面_新增地址备注编辑框(self):
        ele = [By.ID, f"{self.id_loc_base}/etAddressLabel"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 提现页面_新增提现地址编辑框(self):
        ele = [By.ID, f"{self.id_loc_base}/etWithdrawalAddress"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 提现页面_新增地址提交按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/btnAddressSubmit"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 提现页面_提现备注编辑框(self):
        ele = [By.ID, f"{self.id_loc_base}/etRemark"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 提现页面_有无提现备注按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvSelectNoRemark"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 提现页面_最小提币数量(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMinWithdrawal"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 提现页面_实际到账(self):
        ele = [By.ID, f"{self.id_loc_base}/tvReceiveAmount"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])
