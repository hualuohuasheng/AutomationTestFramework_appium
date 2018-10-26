# -*- coding:utf-8 -*-

from iRoomtestcase import iRoomTest_Android
import unittest




if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [iRoomTest_Android("test_003参与者多次切后台")]
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
