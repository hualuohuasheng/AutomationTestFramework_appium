# -*- coding:utf-8 -*-


class User:

    def __init__(self, driver):
        self.driver = driver
        self.is_android = 'desired' in driver.desired_capabilities

    # 首页上进入用户页面的按钮
    @property
    def 进入用户页面按钮(self):
        if self.is_android:
            return self.driver.find_element_by_id("com.ex55.app:id/tvUserImg")
        else:
            return self.driver.find_element_by_id("")

    # 用户页面，用户名
    @property
    def 用户名(self):
        if self.is_android:
            return self.driver.find_element_by_id("com.ex55.app:id/userName")
        else:
            return self.driver.find_element_by_id("")

    # 用户页面，uid
    @property
    def uid(self):
        if self.is_android:
            return self.driver.find_element_by_id("com.ex55.app:id/tvUserUID")
        else:
            return self.driver.find_element_by_id("")

    # 用户页面，充值
    @property
    def 充值(self):
        if self.is_android:
            return self.driver.find_element_by_id("com.ex55.app:id/tvMainDeposits")
        else:
            return self.driver.find_element_by_id("")

    # 用户页面，提现
    @property
    def 提现(self):
        if self.is_android:
            return self.driver.find_element_by_id("com.ex55.app:id/tvMainWithdrawals")
        else:
            return self.driver.find_element_by_id("")

    # 用户页面，划转
    @property
    def 划转(self):
        if self.is_android:
            return self.driver.find_element_by_id("com.ex55.app:id/tvMainTransfer")
        else:
            return self.driver.find_element_by_id("")

    # 用户页面，订单管理
    @property
    def 订单管理(self):
        if self.is_android:
            return self.driver.find_element_by_id("com.ex55.app:id/llOrderHistory")
        else:
            return self.driver.find_element_by_id("")

    # 用户页面，实名认证
    @property
    def 实名认证(self):
        if self.is_android:
            return self.driver.find_element_by_id("com.ex55.app:id/llIDVerification")
        else:
            return self.driver.find_element_by_id("")

    # 用户页面，邀请好友
    @property
    def 邀请好友(self):
        if self.is_android:
            return self.driver.find_element_by_id("com.ex55.app:id/invitingFriends")
        else:
            return self.driver.find_element_by_id("")

    # 用户页面，安全验证
    @property
    def 安全验证(self):
        if self.is_android:
            return self.driver.find_element_by_id("com.ex55.app:id/llSecurity")
        else:
            return self.driver.find_element_by_id("")

    # 用户页面，帮助
    @property
    def 帮助(self):
        if self.is_android:
            return self.driver.find_element_by_id("com.ex55.app:id/llSupport")
        else:
            return self.driver.find_element_by_id("")

    # 用户页面，设置
    @property
    def 设置(self):
        if self.is_android:
            return self.driver.find_element_by_id("com.ex55.app:id/llSetting")
        else:
            return self.driver.find_element_by_id("")

    # 用户页面，联系客服
    @property
    def 联系客服(self):
        if self.is_android:
            return self.driver.find_element_by_id("com.ex55.app:id/tvNavigationService")
        else:
            return self.driver.find_element_by_id("")
