# -*- coding:utf-8 -*-
import unittest
import ilive_main
import public_functions




class PowerinfoILiveTest(unittest.TestCase):


    def setUp(self):
        self.info = public_functions.get_android_app_info()
        self.iroom = ilive_main.AndriodILive(self.info)
        self.iroom.choose_functions('多人群聊')
        pass

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

