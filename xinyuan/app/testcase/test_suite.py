# -*- coding:utf-8 -*-

from xinyuan.app.testcase.UserTestCase import UserTest
import unittest
import xinyuan.app.testcase.public_functions as pub_func
import xinyuan.app.testcase.device as device

if __name__ == '__main__':

    device = device.Device.get_cur_device('1')
    # suite = unittest.TestSuite()
    # tests = 1
    # suite.addTests(tests)
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)
    # pub_func.Device.get_device_info(['huaweihonor9'])
    unittest.main(verbosity=2)