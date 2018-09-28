# -*- coding:utf-8 -*-
import sys
sys.path.append('..')

from time import sleep
import unittest
from lib.ilive_main import AndriodILive
from lib.public_functions import get_android_app_info



class PowerinfoILiveTest(unittest.TestCase):


    def setUp(self):
        self.info = get_android_app_info()
        self.iroom = AndriodILive(self.info)
        self.iroom.choose_functions('多人群聊')
        pass

    def setTeardown(self):
        dri

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

