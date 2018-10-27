# -*- coding:utf-8 -*-
import sys,re,subprocess
sys.path.append('..')

from time import sleep
import unittest
import lib.public_functions as pubfuc
import multiprocessing
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class iRoomTest_Android(unittest.TestCase):

    def setUp(self):
        self.控件信息 = pubfuc.获取控件文件信息()['iRoom_Android']
        #第一个为主播
        devicelist = ['oppo_R9','p10_270','p10_269']
        self.sd = pubfuc.StartDriver(devicelist)

        self.proc_list = []

        print(self.proc_list)
        for i in range(len(self.sd.devicelist)):
            cmd = f"lsof -i:{self.sd.aport[i]}"
            nodeproc = subprocess.getoutput(cmd)
            if f"localhost:{self.sd.aport[i]}" in nodeproc:
                procport = re.split('\s+',nodeproc.split('\n')[1])[1]
                print(procport)
                subprocess.Popen(f'kill {procport}',shell=True)
            self.proc_list.append(multiprocessing.Process(target=self.sd.startAppiumServer, args=(i,)))

        print(self.proc_list)

        for pro in self.proc_list:
            pro.start()
            sleep(1)

        for pro in self.proc_list:
            pro.join()

        while len(self.sd.getNodeProcPid()) < len(devicelist):
            sleep(1)


        print(self.sd.getNodeProcPid())

        self.driverlist = []

        for i in range(len(self.sd.devicelist)):
            driver = webdriver.Remote(f"http://localhost:{self.sd.aport[i]}/wd/hub", self.sd.realdevice[i])
            self.driverlist.append(driver)



    def test_001参与者多次加入离开房间(self):
        self.driverlist[0].find_element_by_xpath(self.控件信息['多人群聊']['xpath']).click()
        self.driverlist[0].find_element_by_id(self.控件信息['创建房间']['id']).click()
        sleep(1)
        self.driverlist[0].find_element_by_id(self.控件信息['START']['id']).click()

        pubfuc.waittimeout(self.driverlist[0].find_element_by_id(self.控件信息['离开房间']['id']))
        pages = self.driverlist[0].page_source
        roomid = str(re.findall('RoomId:\d+',pages)[0]).split(':')[1]
        sleep(1)

        print(re.sub("xxxx",roomid,self.控件信息['房间列表']['xpath']))
        num = 1

        self.driverlist[1].find_element_by_xpath(self.控件信息['多人群聊']['xpath']).click()
        sleep(0.5)
        roomxpath = re.sub("xxxx", roomid, self.控件信息['房间列表']['xpath'])
        while num <501:
            print(f"第{num}次加入房间")
            pubfuc.waittimeout(self.driverlist[1].find_element_by_xpath(roomxpath))
            self.driverlist[1].find_element_by_xpath(roomxpath).click()
            pubfuc.waittimeout(self.driverlist[1].find_element_by_id(self.控件信息['JOIN']['id']))
            self.driverlist[1].find_element_by_id(self.控件信息['JOIN']['id']).click()
            sleep(5)
            self.driverlist[1].find_element_by_id(self.控件信息['离开房间']['id']).click()
            sleep(1)
            num += 1

    def test_002参与者多次切回角色(self):
        self.driverlist[0].find_element_by_xpath(self.控件信息['多人群聊']['xpath']).click()
        self.driverlist[0].find_element_by_id(self.控件信息['创建房间']['id']).click()
        sleep(1)
        self.driverlist[0].find_element_by_id(self.控件信息['START']['id']).click()

        pubfuc.waittimeout(self.driverlist[0].find_element_by_id(self.控件信息['离开房间']['id']))
        pages = self.driverlist[0].page_source
        roomid = str(re.findall('RoomId:\d+', pages)[0]).split(':')[1]
        sleep(1)

        print(re.sub("xxxx", roomid, self.控件信息['房间列表']['xpath']))
        num = 1

        self.driverlist[1].find_element_by_xpath(self.控件信息['多人群聊']['xpath']).click()
        sleep(0.5)
        roomxpath = re.sub("xxxx", roomid, self.控件信息['房间列表']['xpath'])
        pubfuc.waittimeout(self.driverlist[1].find_element_by_xpath(roomxpath))
        self.driverlist[1].find_element_by_xpath(roomxpath).click()
        pubfuc.waittimeout(self.driverlist[1].find_element_by_id(self.控件信息['JOIN']['id']))
        self.driverlist[1].find_element_by_id(self.控件信息['JOIN']['id']).click()
        while num < 501:
            print(f"第{num}次切换角色")
            sleep(1)
            self.driverlist[1].find_element_by_id(self.控件信息['切换角色']['id']).click()
            sleep(5)
            num += 1

        self.driverlist[1].find_element_by_id(self.控件信息['离开房间']['id']).click()
        sleep(1)


    def test_003参与者多次切后台(self):
        self.driverlist[0].find_element_by_xpath(self.控件信息['多人群聊']['xpath']).click()
        self.driverlist[0].find_element_by_id(self.控件信息['创建房间']['id']).click()
        sleep(1)
        self.driverlist[0].find_element_by_id(self.控件信息['START']['id']).click()

        pubfuc.waittimeout(self.driverlist[0].find_element_by_id(self.控件信息['离开房间']['id']))
        pages = self.driverlist[0].page_source
        roomid = str(re.findall('RoomId:\d+', pages)[0]).split(':')[1]
        sleep(1)

        print(re.sub("xxxx", roomid, self.控件信息['房间列表']['xpath']))
        num = 1

        self.driverlist[1].find_element_by_xpath(self.控件信息['多人群聊']['xpath']).click()
        sleep(0.5)
        roomxpath = re.sub("xxxx", roomid, self.控件信息['房间列表']['xpath'])
        pubfuc.waittimeout(self.driverlist[1].find_element_by_xpath(roomxpath))
        self.driverlist[1].find_element_by_xpath(roomxpath).click()
        self.driverlist[1].find_element_by_id(self.控件信息['JOIN']['id']).click()
        while num < 501:
            self.driverlist[0].desired_capabilities
            sleep(5)
            print(f"第{num}次切后台")
            self.driverlist[1].background_app(15)
            num += 1


    def test_004参与者多次加入离开指导房间(self):
        num = 1
        while num < 101:
            for driver in self.driverlist:
                print(f"第{num}次,{driver}加入房间")
                if num == 1:
                    driver.find_element_by_xpath(self.控件信息['多人群聊']['xpath']).click()
                    sleep(1)
                roomxpath = re.sub("xxxx", '4033', self.控件信息['房间列表']['xpath'])
                pubfuc.waittimeout(driver.find_element_by_xpath(roomxpath))
                driver.find_element_by_xpath(roomxpath).click()
                pubfuc.waittimeout(driver.find_element_by_id(self.控件信息['JOIN']['id']))
                driver.find_element_by_id(self.控件信息['JOIN']['id']).click()
                sleep(2)
            for driver in self.driverlist:
                driver.find_element_by_id(self.控件信息['离开房间']['id']).click()
                sleep(2)
            num += 1

    def test_005参与者多次切后台(self):
        for driver in self.driverlist:
            driver.find_element_by_xpath(self.控件信息['多人群聊']['xpath']).click()
            sleep(1)
            roomxpath = re.sub("xxxx", '4036', self.控件信息['房间列表']['xpath'])
            pubfuc.waittimeout(driver.find_element_by_xpath(roomxpath))
            driver.find_element_by_xpath(roomxpath).click()
            pubfuc.waittimeout(driver.find_element_by_id(self.控件信息['JOIN']['id']))
            driver.find_element_by_id(self.控件信息['JOIN']['id']).click()
            sleep(3)
        num = 1
        while num < 301:
            for driver in self.driverlist:
                sleep(1)
                print(f"第{num}次切后台")
                driver.background_app(5)

            num += 1

    def test_006参与者多次切换角色(self):
        for driver in self.driverlist:
            driver.find_element_by_xpath(self.控件信息['多人群聊']['xpath']).click()
            sleep(1)
            roomxpath = re.sub("xxxx", '4036', self.控件信息['房间列表']['xpath'])
            pubfuc.waittimeout(driver.find_element_by_xpath(roomxpath))
            driver.find_element_by_xpath(roomxpath).click()
            pubfuc.waittimeout(driver.find_element_by_id(self.控件信息['JOIN']['id']))
            driver.find_element_by_id(self.控件信息['JOIN']['id']).click()
            sleep(3)
        num = 1
        while num < 301:
            for driver in self.driverlist:
                print(f"第{num}次切后台")
                driver.find_element_by_id(self.控件信息['切换角色']['id']).click()
                sleep(3)

            num += 1


    def tearDown(self):
        # self.sd.killNodeProPid(self.proc_pid_list)
        for driver in self.driverlist:
            driver.quit()

        for proc in self.proc_list:
            proc.kill()




