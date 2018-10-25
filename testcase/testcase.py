# -*- coding:utf-8 -*-
import sys
sys.path.append('..')

from time import sleep
import unittest
import lib.public_functions as pubfuc
import multiprocessing
from appium import webdriver


class PowerinfoILiveTest(unittest.TestCase):


    def setUp(self):
        self.控件信息 = pubfuc.获取控件文件信息()
        devicelist = ['ip6s_test13','p10_268']
        self.sd = pubfuc.StartDriver(['ip6s_test13','p10_268'])
        self.proc_pid_list = self.sd.getNodeProcPid()


        proc_list = []
        while len(self.proc_pid_list) < len(devicelist):
            for i in range(len(self.sd.devicelist)):
                proc_list.append(multiprocessing.Process(target=self.sd.startAppiumServer, args=(i,)))

            for pro in proc_list:
                pro.start()

            for pro in proc_list:
                pro.join()
        print('sup')
        print(self.proc_pid_list)

        self.driverlist = []

        for i in range(len(self.sd.devicelist)):
            driver = webdriver.Remote(f"http://localhost:{self.sd.aport[i]}/wd/hub", self.sd.realdevice[i])
            self.driverlist.append(driver)


    def test_minus(self):
        self.driverlist[0]
        print('test1')

        # self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.info['oppo_R9'])

    def tearDown(self):
        # self.sd.killNodeProPid(self.proc_pid_list)
        for driver in self.driverlist:
            driver.quit()






if __name__ == '__main__':
    uittest.main()

