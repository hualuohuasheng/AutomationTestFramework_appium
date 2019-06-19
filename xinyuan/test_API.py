# -*- coding:utf-8 -*-

import requests
import unittest


class TestAPI(unittest.TestCase):

    def setUp(self):
        # 初始化测试环境
        self.host = "http://httpbin.org/"

    def tearDown(self):
        pass

    def test_001(self):
        url = self.host + "/post"
        datainfo = {'key': 'value'}
        res = requests.post(url, data=datainfo)
        print(res.json())
        self.assertTrue(False, 'is false')


unittest.main()