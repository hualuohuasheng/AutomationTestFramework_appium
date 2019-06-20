# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep
import unittest
import xinyuan.public_main as pub_func


class TestGuoJiZhan(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = "http://global.dev_test_uat.55.exchange:5555"
        cls.browser = webdriver.Chrome()
        cls.browser.get(cls.url)
        cls.browser.set_page_load_timeout(60)
        WebDriverWait(cls.browser, 30, 1).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, 'login')))
        cls.browser.maximize_window()

    def setUp(self):
        if '订单' not in self.browser.page_source:
            self.browser.find_element_by_class_name('login').click()
            sleep(3)
            self.browser.find_element_by_xpath(
                "//input[@type='text' and @class='ivu-input ivu-input-default']").send_keys(
                '15811055254')
            self.browser.find_element_by_xpath(
                "//input[@type='password' and @class='ivu-input ivu-input-default']").send_keys(
                'xinyuanlml0617')
            self.browser.find_element_by_css_selector(".loginbtn").click()
            sleep(2)
            cut_img_element = (By.XPATH, "//img[@class='yidun_jigsaw']")
            back_img_element = (By.XPATH, "//img[@class='yidun_bg-img']")
            slider_element = (By.XPATH, "//div[@class='yidun_slider']")
            WebDriverWait(self.browser, 30, 1).until(expected_conditions.presence_of_element_located(back_img_element))
            WebDriverWait(self.browser, 30, 1).until(expected_conditions.presence_of_element_located(cut_img_element))
            pub_func.slider_verification_code_163yidun(self.browser, cut_img_element, back_img_element, slider_element)

    def tearDown(self):
        self.browser.find_element(By.XPATH, "//a[@href='/home']").click()
        sleep(2)

    def test_001_login(self):
        ActionChains(self.browser).move_to_element(self.browser.find_element_by_link_text('交易中心')).perform()
        sleep(0.5)
        self.browser.find_element_by_xpath("//span[@text='区块链交易']").click()
        self.browser.implicitly_wait(10)
        print('订单' in self.browser.page_source)
        self.assertTrue(self.browser.find_element(By.LINK_TEXT, '订单'), '登录失败，订单按钮未找到')

    def test_002_dingdan(self):
        self.browser.find_element_by_link_text('订单').click()
        sleep(2)
        self.browser.find_element_by_css_selector("div.ivu-tabs-tab").click()
        sleep(2)
        tables = self.browser.find_elements_by_class_name('ivu-table-row')
        for i in tables:
            print(i)
            print(i.get_property('text'))
