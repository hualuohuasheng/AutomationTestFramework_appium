# -*- coding:utf-8 -*-
import public_functions
import ilive_main
info = public_functions.get_android_app_info()

iroom = ilive_main.AndriodILive(info)

iroom.choose_functions()
iroom.creat_new_room()