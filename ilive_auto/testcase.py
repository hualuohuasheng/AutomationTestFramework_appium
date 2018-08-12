# -*- coding:utf-8 -*-
import public_functions
import ilive_main
from time import sleep
import unittest

info = public_functions.get_android_app_info()

iroom = ilive_main.AndriodILive(info)

iroom.choose_functions('多人群聊直播')


num = 1
while num < 100:
    sleep(1)
    iroom.join_room('RoomID :3237')
    sleep(2)
    #iroom.open_beauty()
    for i in range(5):
        sleep(5)
        iroom.change_role()
        print(f"第{num}次加入房间，第{i+1}次切换角色通过")
    num +=1
    iroom.quit_room()






