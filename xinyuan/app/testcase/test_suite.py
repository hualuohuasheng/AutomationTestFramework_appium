# -*- coding:utf-8 -*-

import xinyuan.app.testcase.UserTestCase as UserTestCase
import xinyuan.app.testcase.OrderTestCase as OerderTestCase
import unittest
# import xinyuan.app.testcase.public_functions as pub_func
import xinyuan.app.testcase.device as device
# import xinyuan.app.testcase.appiumserver as appium

if __name__ == '__main__':

    device_id = '69DDU17209002446'
    device = device.Device.get_cur_device(device_id, '8.0')
    # appium.AppiumServer.get_port(device_id)    # 启动appium server并获取port
    suite = unittest.TestSuite()
    tests = [OerderTestCase.OrderTest('test_002_验证币币页下单卖出功能正确')]
    suite.addTests(tests)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    # unittest.main(verbosity=2)
