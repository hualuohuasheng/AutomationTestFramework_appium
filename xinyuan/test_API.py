# -*- coding:utf-8 -*-

import requests
import unittest
import json


def pars_print_json(res):
    结果 = json.dumps(res, indent=4, separators=(', ', ': '))
    print(结果)


class TestAPI(unittest.TestCase):

    def setUp(self):
        # 初始化测试环境
        self.host = "http://121.42.12.93:7778"

    def tearDown(self):
        pass

    def test_001_收到货(self):
        url = self.host + "/idm/kyc/201907191653160013"
        headers = {'key': '092a06e4b8c34448aeecaea9cf745b59'}
        res = requests.get(url, headers=headers)
        pars_print_json(res.json())


if __file__ == '__main__':

    unittest.main()