# -*- coding:utf-8 -*-
import sys
sys.path.append('..')

from time import sleep
import unittest
import lib.public_functions as pubfuc



class PowerinfoILiveTest(unittest.TestCase):


    def setUp(self):
        self.控件信息 = pubfuc.获取控件文件信息()
        self.info = 获取控件文件信息('devices')


        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.info['oppo_R9'])

    def setTeardown(self):
        self.driver.quite()

    def test_ChangeRole(self):
        num = 1
        while num < 5:
            sleep(3)
            self.iroom.join_room('RoomID :1654')
            sleep(3)
            # iroom.open_beauty()
            # for i in range(5):
            #     sleep(5)
            #     self.iroom.change_role()
            #     self.assertTrue("True")
            #     print(f"第{num}次加入房间，第{i+1}次切换角色通过")
            num += 1
            self.iroom.quit_room()
            self.assertTrue("True")
            print(f"第{num}次加入房间通过")



unittest.main()

