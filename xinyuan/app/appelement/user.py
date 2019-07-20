# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from xinyuan.app.appelement.base import BasePage


class UserPage(BasePage):

    # 首页上进入用户页面的按钮
    def 进入用户页面按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvUserImg"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    # 用户页面，用户名
    def 用户名(self):
        ele = [By.ID, f"{self.id_loc_base}/userName"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    # 用户页面，uid
    def uid(self):
        ele = [By.ID, f"{self.id_loc_base}/tvUserUID"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    # 用户页面，充值
    def 充值(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMainDeposits"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    # 用户页面，提现
    def 提现(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMainWithdrawals"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    # 用户页面，划转
    def 划转(self):
        ele = [By.ID, f"{self.id_loc_base}/tvMainTransfer"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    # 用户页面，订单管理
    def 订单管理(self):
        ele = [By.ID, f"{self.id_loc_base}/llOrderHistory"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    # 用户页面，实名认证
    def 实名认证(self):
        ele = [By.ID, f"{self.id_loc_base}/llIDVerification"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    # 用户页面，邀请好友
    def 邀请好友(self):
        ele = [By.ID, f"{self.id_loc_base}/invitingFriends"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    # 用户页面，安全验证
    def 安全验证(self):
        ele = [By.ID, f"{self.id_loc_base}/llSecurity"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 安全验证_登录密码(self):
        ele = [By.ID, f"{self.id_loc_base}/changePassword"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 安全验证_登录密码_输入密码(self):
        ele = [By.ID, f"{self.id_loc_base}/etLoginPWD"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 安全验证_登录密码_下一步(self):
        ele = [By.ID, f"{self.id_loc_base}/btnNext"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 安全验证_登录密码_新密码(self):
        ele = [By.ID, f"{self.id_loc_base}/etNewPWD"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 安全验证_登录密码_确认新密码(self):
        ele = [By.ID, f"{self.id_loc_base}/etNewPWDAgain"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 安全验证_提交(self):
        ele = [By.XPATH, "//android.widget.Button[@text='提交']"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 安全验证_谷歌认证(self):
        ele = [By.ID, f"{self.id_loc_base}/llGoogle"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 下一步(self):
        ele = [By.XPATH, f"//android.widget.Button[@text='下一步']"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 安全验证_谷歌认证_密钥(self):
        ele = [By.ID, f"{self.id_loc_base}/tvBackupKey"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 安全验证_谷歌认证_输入密钥(self):
        ele = [By.ID, f"{self.id_loc_base}/etEnterKey"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 安全验证_谷歌认证_登录密码(self):
        ele = [By.ID, f"{self.id_loc_base}/etLoginPWD"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 安全验证_谷歌认证_输入谷歌验证码(self):
        ele = [By.ID, f"{self.id_loc_base}/etGoogleCode"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 安全验证_手机验证(self):
        ele = [By.ID, f"{self.id_loc_base}/llPhoneSecurity"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 安全验证_输入手机验证码(self):
        ele = [By.ID, f"{self.id_loc_base}/etSMS"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 安全验证_发送手机验证码(self):
        ele = [By.ID, f"{self.id_loc_base}/tvSend"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 安全验证_邮箱验证(self):
        ele = [By.ID, f"{self.id_loc_base}/llEmailSecurity"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 安全验证_输入邮箱验证码(self):
        ele = [By.ID, f"{self.id_loc_base}/etEmail"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 安全验证_发送邮箱验证码(self):
        ele = [By.ID, f"{self.id_loc_base}/tvSendEmail"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 安全验证_修改交易密码(self):
        ele = [By.ID, f"{self.id_loc_base}/tradingPassword"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 安全验证_交易密码时效(self):
        ele = [By.ID, f"{self.id_loc_base}/tradingPasswordTime"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    # 用户页面，帮助
    def 帮助(self):
        ele = [By.ID, f"{self.id_loc_base}/llSupport"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 帮助_公告中心(self):
        ele = [By.XPATH, f"//android.view.View[@text='公告中心']"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    # 用户页面，设置
    def 设置(self):
        ele = [By.ID, f"{self.id_loc_base}/llSetting"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    # 用户页面，联系客服
    def 联系客服(self):
        ele = [By.ID, f"{self.id_loc_base}/tvNavigationService"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 设置_退出(self):
        ele = [By.ID, f"{self.id_loc_base}/exitAPP"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 返回(self):
        ele = [By.ID, f"{self.id_loc_base}/custom_header_iv_back"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 设置_语言(self):
        ele = [By.ID, f"{self.id_loc_base}/llLanguage"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 设置_语言_英语(self):
        ele = [By.ID, f"{self.id_loc_base}/llEnglish"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 设置_语言_韩语(self):
        ele = [By.ID, f"{self.id_loc_base}/llKorea"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 设置_语言_简体中文(self):
        ele = [By.ID, f"{self.id_loc_base}/llChinese"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 设置_语言_繁体中文(self):
        ele = [By.ID, f"{self.id_loc_base}/llChineseTW"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 设置_计价方式(self):
        ele = [By.ID, f"{self.id_loc_base}/llCurrencyRate"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 设置_计价方式_货币(self, currency):
        ele = [By.XPATH, f"//android.widget.TextView[@text='{currency}']"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 设置_颜色偏好(self):
        ele = [By.ID, f"{self.id_loc_base}/llColor"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 设置_颜色偏好_红涨绿跌(self):
        ele = [By.ID, f"{self.id_loc_base}/llRedUpsGreenDowns"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 设置_颜色偏好_红跌绿涨(self):
        ele = [By.ID, f"{self.id_loc_base}/llGreenUpsRedDowns"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 设置_检查更新(self):
        ele = [By.ID, f"{self.id_loc_base}/llCheckUpdate"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 设置_关于(self):
        ele = [By.ID, f"{self.id_loc_base}/llCurrencyRate"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 账号编辑框(self):
        ele = [By.ID, f"{self.id_loc_base}/etAccountId"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 密码编辑框(self):
        ele = [By.ID, f"{self.id_loc_base}/etPWD"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 账号清除按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/ivDelete"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 隐藏显示密码(self):
        ele = [By.ID, f"{self.id_loc_base}/hideShowPassword"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 登录按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/btnLogin"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 忘记密码按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvResetPWD"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 忘记密码_账号编辑框(self):
        ele = [By.ID, f"{self.id_loc_base}/etAccount"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 免费注册按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/tvToRegister"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 重置密码_账号编辑框(self):
        ele = [By.ID, f"{self.id_loc_base}/etAccount"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 国家(self):
        ele = [By.ID, f"{self.id_loc_base}/tvCountryName"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 手机号前(self):
        ele = [By.ID, f"{self.id_loc_base}/tvCountry"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 选择国家(self, contry):
        # el1 = self.driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.TextView[1]")
        # el1.click()
        ele = [By.XPATH, f"//android.widget.LinearLayout/android.widget.TextView['text={contry}']"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 昵称编辑框(self):
        ele = [By.ID, f"{self.id_loc_base}/etUniqueName"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 同意条款按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/cbUseTerms"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 密码确认编辑框(self):
        ele = [By.ID, f"{self.id_loc_base}/etReferral"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 注册按钮(self):
        ele = [By.ID, f"{self.id_loc_base}/btnRegister"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 手机注册(self):
        ele = [By.ID, f"{self.id_loc_base}/tvSelectType"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 使用条款(self):
        ele = [By.ID, f"{self.id_loc_base}/tvTerms"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 隐私条款(self):
        ele = [By.ID, f"{self.id_loc_base}/tvPrivacyPolicy"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 电子邮件已经验证按钮(self):
        ele = [By.XPATH, f"//android.widget.Button[@text='电子邮件已经验证']"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def 谷歌验证码(self):
        ele = [By.ID, f"{self.id_loc_base}/tvPrivacyPolicy"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])

    def toast(self, toastmsg):
        ele = [By.ID, f"//android.widget.Toast[@text='{toastmsg}']"] if self.is_android else []
        return self.driver.find_element(ele[0], ele[1])
