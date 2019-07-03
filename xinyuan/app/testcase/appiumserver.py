# -*- coding:utf8 -*-

import subprocess
import os
import socket


def check_port_used(port, host="127.0.0.1"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, int(port)))
        s.shutdown(2)
        return True
    except Exception:
        return False


def get_useful_port():
    port = 4723
    i = 0
    while check_port_used(port):
        i += 1
        port = 4723 + i * 2
    return port, i


def start_appium_server(device, is_ios=False):
    excute_cmd_base = f"node {os.environ['APPIUM']}/Resources/app/node_modules/appium/build/lib/main.js -a 127.0.0.1"
    port, index = get_useful_port()
    deviceport = f'--webdriveragent-port {8100+index}' if is_ios else f'-bp {port + 1}'
    excute_cmd = f"{excute_cmd_base} -p {port} {deviceport} -U {device} " \
        f"--local-timezone --log-timestamp --command-timeout 3000"

    subprocess.Popen(excute_cmd, shell=True,
                     stdout=open(f"{os.path.curdir}/appiumlog_{device}.txt", 'w+'))
    return port


class AppiumServer:

    @classmethod
    def get_port(cls, device, is_ios=False):
        cls.port = start_appium_server(device, is_ios)
