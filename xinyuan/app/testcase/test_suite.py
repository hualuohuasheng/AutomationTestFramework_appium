# -*- coding:utf-8 -*-

from xinyuan.app.testcase.UserTestCase import UserTest
import unittest
import xinyuan.app.testcase.public_functions as pub_func
import xinyuan.app.testcase.device as device
import xinyuan.app.testcase.appiumserver as appium

if __name__ == '__main__':

    device_id = '69DDU17209002446'
    device = device.Device.get_cur_device(device_id, '8.0')
    # appium.AppiumServer.get_port(device_id)    # 启动appium server并获取port
    # suite = unittest.TestSuite()
    # tests = 1
    # suite.addTests(tests)
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)
    # pub_func.Device.get_device_info(['huaweihonor9'])
    unittest.main(verbosity=2)