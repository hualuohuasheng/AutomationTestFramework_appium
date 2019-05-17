# -*- coding:utf-8 -*-
# import re
# sys.path.append('..')

from time import sleep
import unittest
import lib.public_functions as pubfuc
import multiprocessing
from appium import webdriver
import testcase.dokidokibehavior as dokidokibehavior
import logging

logger = logging.getLogger('autolog')


class dokidokiTest(unittest.TestCase):

    def setUp(self):
        # 在当前目录，新建mail.txt，文件第一行存放设备列表，第二行存放roomid
        with open('mail.txt', 'r') as f:
            info = f.readlines()
        devicelist = info[0].rstrip().split(',')
        logger.info(f'devicelist: {devicelist}')
        self.device_name = devicelist
        self.roomid = info[1].split('#')[0].rstrip()
        self.sd = pubfuc.StartDriver(devicelist)
        self.proc_list = []

        pubfuc.cleannodeproc()
        for i in range(len(self.sd.devicelist)):
            self.proc_list.append(multiprocessing.Process(target=self.sd.startappiumserver, args=(i,)))

        for pro in self.proc_list:
            pro.start()

        for pro in self.proc_list:
            pro.join()

        while len(self.sd.getnodeprocpid()) < len(devicelist):
            sleep(1)

        logger.info(self.sd.getnodeprocpid())

        self.driverlist = []

        for i in range(len(self.sd.devicelist)):
            logger.info(i)
            desire_caps = self.sd.realdevice[i]
            if 'bundleId' in desire_caps:
                desire_caps['bundleId'] = 'net.imusic.android.dokidoki'
                # desire_caps['waitForQuiescence'] = 'false'
            else:
                desire_caps['appPackage'] = 'net.imusic.android.dokidoki'
                desire_caps['appActivity'] = 'net.imusic.android.dokidoki.page.main.MainActivity'
            driver = webdriver.Remote(f"http://localhost:{self.sd.aport[i]}/wd/hub", self.sd.realdevice[i])

            self.driverlist.append(driver)

        logger.info(self.driverlist)

    def test_001参与者多次加入离开房间(self):
        logger.info('test_001参与者多次加入离开房间')
        num = 1
        procs = []
        pool = multiprocessing.Pool(processes=len(self.driverlist))
        print(self.driverlist)
        driverA = self.driverlist[1]
        driverB = self.driverlist[0]
        print(driverA)
        print(driverB)
        print(1)
        driverA.find_element_by_id("net.imusic.android.dokidoki:id/btn_live").click()
        driverB.find_element_by_id("net.imusic.android.dokidoki:id/btn_live").click()
        sleep(2)
        driverA.find_element_by_id("net.imusic.android.dokidoki:id/live_icon").click()
        driverB.find_element_by_id("net.imusic.android.dokidoki:id/live_icon").click()
        sleep(2)
        driverA.find_element_by_id("net.imusic.android.dokidoki:id/btn_live").click()
        driverB.find_element_by_id("net.imusic.android.dokidoki:id/btn_live").click()
        sleep(10)
        while num < 301:
            driverA.find_element_by_id("net.imusic.android.dokidoki:id/btn_interaction").click()
            sleep(2)
            driverA.find_element_by_id("net.imusic.android.dokidoki:id/ll_pk").click()
            sleep(2)
            driverA.find_element_by_id("net.imusic.android.dokidoki:id/rl_friends").click()
            sleep(3)
            driverA.find_element_by_id("net.imusic.android.dokidoki:id/tv_invite").click()
            sleep(5)
            driverB.find_element_by_id("net.imusic.android.dokidoki:id/tv_accept").click()
            sleep(10)
            driverA.find_element_by_id("net.imusic.android.dokidoki:id/tv_end_pk").click()  #结束PK
            sleep(2)
            driverA.find_element_by_id("net.imusic.android.dokidoki:id/tv_right").click()
            sleep(5)
            num += 1
        driverA.find_element_by_id("net.imusic.android.dokidoki:id/btn_close").click()
        driverB.find_element_by_id("net.imusic.android.dokidoki:id/btn_close").click()
        sleep(2)
        driverA.find_element_by_id("android:id/button1").click()
        driverB.find_element_by_id("android:id/button1").click()
        sleep(2)
        driverA.find_element_by_id("net.imusic.android.dokidoki:id/btn_close").click()
        driverB.find_element_by_id("net.imusic.android.dokidoki:id/btn_close").click()
        sleep(5)


    def tearDown(self):
        logger.info('test运行完成')
        # quite the device driver
        # pass
        for driver in self.driverlist:
            driver.quit()
        # for proc in self.proc_list:
            # print(proc.is_alive())
            # proc.terminate()


