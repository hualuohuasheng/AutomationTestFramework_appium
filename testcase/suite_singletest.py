# -*- coding:utf-8 -*-

from iRoomtestcase import iRoomTest
import unittest




if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [iRoomTest("test_003参与者多次切后台")]
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
