# -*- coding:utf-8 -*-

import iRoomtestcase
from zegotestcase import zegoTest
import unittest,myunittest
import sys
import lib.public_functions as pubfunc


mail_recievers = ['liml']


if __name__ == '__main__':
    suite = myunittest.TestSuite()
    tests = [iRoomtestcase.iRoomTest("test_002参与者多次切换角色")]
    # tests =[] test_002参与者多次切换角色 test_001参与者多次加入离开房间 test_004参与者多次加入离开指导房间
    suite.addTests(tests)

    result_file = pubfunc.get_real_dir_path(__file__,'../testresult')+ f'/{pubfunc.getLocalTime()}_result.txt'
    print(result_file)
    runner = myunittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    # tmp = sys.stdout
    # err = sys.stderr
    # sys.stdout = open('out.log','w')
    # sys.stderr = open('error.log','w')

    # sys.stdout = tmp
    # sys.stderr = err
    # sys.stdout = open('out.log','w')
    # print('自动化测试')
    # with open(result_file,'w') as f:
    #     runner = myunittest.TextTestRunner(stream=f,verbosity=2)
    #     runner.run(suite)

    # pubfunc.send_mail(mail_recievers,result_file)