# -*- coding:utf-8 -*-
# import re
# sys.path.append('..')

from time import sleep
import unittest
import lib.public_functions as pubfuc
import multiprocessing
from appium import webdriver
import testcase.zuji_behavior as zuji_behavior
import logging

logger = logging.getLogger('autolog')


class ZujiTest(unittest.TestCase):

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
                desire_caps['bundleId'] = 'com.btxg.xvideo'  # bootstrapA50
                # desire_caps['waitForQuiescence'] = 'false'
            else:
                desire_caps['appPackage'] = 'com.soccerv'
                desire_caps['appActivity'] = 'com.soccerv.MainActivity'
            driver = webdriver.Remote(f"http://localhost:{self.sd.aport[i]}/wd/hub", self.sd.realdevice[i])
            sleep(20)
            self.driverlist.append(driver)

        logger.info(self.driverlist)

    def test_001足记登录(self):
        logger.info('test_001足记登录')
        procs = []
        pool = multiprocessing.Pool(processes=len(self.driverlist))
        proc = pool.apply_async(zuji_behavior.login, (self.driverlist[0], self.device_name[0],))
        procs.append(proc)
        for i in procs:
            i.get()
        for i in procs:
            i.wait()

    def test_002足记创建加入比赛(self):
        logger.info('test_001足记登录')
        procs = []
        pool = multiprocessing.Pool(processes=len(self.driverlist))
        proc = pool.apply_async(zuji_behavior.joingame, (self.driverlist[0], self.driverlist[1], self.device_name[0],))
        procs.append(proc)
        for i in procs:
            i.get()
        for i in procs:
            i.wait()

    def test_003足记播放视频(self):
        logger.info('test_001足记登录')
        procs = []
        pool = multiprocessing.Pool(processes=len(self.driverlist))
        proc = pool.apply_async(zuji_behavior.playgamevideo, (self.driverlist[0], self.device_name[0],))
        procs.append(proc)
        for i in procs:
            i.get()
        for i in procs:
            i.wait()

    def tearDown(self):
        logger.info('test运行完成')
        # quite the device driver
        pass
        # for driver in self.driverlist:
        #     driver.quit()



