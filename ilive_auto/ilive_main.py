# -*- coding:utf-8 -*-

import os
import re
from time import sleep
from appium import webdriver

class PublicDriver:

    def __init__(self,desired_caps,command_executor="http://localhost:4723/wd/hub"):
        self.caps = desired_caps
        self.driver = webdriver.Remote(command_executor, self.caps)

    def location_by_xpath(self,name,type='TextView',deviceos='android'):
        xpath=f"//android.widget.{type}[@text='{name}']" if deviceos =='android' else f"//"
        # print(xpath)
        return self.driver.find_element_by_xpath(xpath)

    def location_by_id(self,functionid,deviceos='android'):
        id=f"{self.caps['appPackage']}:id/{functionid}" if deviceos =='android' else f"xuictest"
        return self.driver.find_element_by_id(id)

class AndriodILive(PublicDriver):

    def __init__(self,desired_caps,command_executor="http://localhost:4723/wd/hub"):
        super().__init__(desired_caps,command_executor)

    #创建一个新房间
    def creat_new_room(self):
        self.location_by_id("iv_create_room").click()
        sleep(1)
        # self.location_by_id("bt_start")
        self.location_by_xpath('START','Button').click()
        sleep(1)
        #返回创建的room id
        return self.location_by_id('tv_roomId').get_attribute('text')

    #加入房间
    def join_room(self,roomid):
        self.location_by_xpath(roomid).click()
        sleep(1)
        self.location_by_xpath('JOIN', 'Button').click()
        sleep(1)


    # 退出房间
    def quit_room(self):
        self.location_by_id("iv_back").click()

    #选择多人群聊、主播PK、直播推流、游戏连麦
    def choose_functions(self,group='多人群聊'):
        self.location_by_xpath(group).click()

    #设置齿轮
    def settings(self):
        self.location_by_id('iv_setting').click()

    #切换摄像头
    def switch_camera(self):
        self.location_by_id('iv_camera').click()

    #开关闪光灯
    def torch(self):
        self.location_by_id('iv_torch').click()

    #切换角色
    def change_role(self):
        self.location_by_id('iv_changeRole').click()

    #开关美颜
    def open_beauty(self):
        self.location_by_id('iv_beauty').click()

    #切换房间
    def change_room(self,roomid):
        self.location_by_id('iv_changeRoom').click()
        self.location_by_xpath(roomid).click()

