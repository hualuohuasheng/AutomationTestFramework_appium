# -*- coding:utf-8 -*-
import sys
sys.path.append('..')

from time import sleep
import unittest
from lib.ilive_main import AndriodILive
from lib.public_functions import get_android_app_info
import yaml

class Liveme(unittest.TestCase):

    def setUp(self):
        global driver
        self.info = get_android_app_info()
        driver = webdriver.Remote('http://localhost:4723/wd/hub', self.info)
        self.id = f"{self.info['appPackage']}:id/{functionid}"


    def test_001_开播(self):
        #开播
        driver.find_element_by_id(f"{self.info['appPackage']}:id/uplive").click()
        sleep(1)
        #选择多人直播
        driver.find_element_by_id(f"{self.info['appPackage']}:id/live_multi_layout").click()
        #点击开播
        driver.find_element_by_id(f"{self.info['appPackage']}:id/txt_video_start_live").click()
        sleep(5)
        driver.find_element_by_id(f"{self.info['appPackage']}:id/shortid_iv")..get_attribute('text')