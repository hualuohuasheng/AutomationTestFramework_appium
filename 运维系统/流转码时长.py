# -*- coding: utf-8 -*-
import os
import json
import time


def 生成数据文件(groupid, level):
    t = int(time.time())
    print(t)
    origin_dict = {
        "channels": [
            {
                "channel_name": f"{groupid}/mlinkm/test1",
                "channeltime": 10000
            }
        ],
        "level": level,
        "time": t
    }

    json_dict = json.loads(json.dumps(origin_dict))
    with open(f"e:/test1.json", 'a+') as file:
        json.dump(json_dict, file, indent=4)
        file.write('\n')


生成数据文件('inke', 1)
生成数据文件('inke', 2)
