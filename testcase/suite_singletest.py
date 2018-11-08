# -*- coding:utf-8 -*-

import iRoomtestcase
from zegotestcase import zegoTest
import unittest,myunittest
import sys
import lib.public_functions as pubfunc


mail_recievers = ['liml']


if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = [iRoomtestcase.iRoomTest("test_001参与者多次加入离开房间")]
    # tests =[]
    suite.addTests(tests)

    result_file = pubfunc.get_real_dir_path(__file__,'../testresult')+ f'/{pubfunc.getLocalTime()}_result.txt'
    print(result_file)

    with open(result_file,'a') as f:
        runner = unittest.TextTestRunner(stream=f,verbosity=2)
        runner.run(suite)

    # pubfunc.send_mail(mail_recievers,result_file)