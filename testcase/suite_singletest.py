# -*- coding:utf-8 -*-

from iRoomtestcase import iRoomTest
from zegotestcase import zegoTest
import unittest




if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [iRoomTest("test_002参与者多次切回角色")]
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
