# -*- coding:utf-8 -*-

import os,re,time
import subprocess
from pathlib import Path
import yaml
import platform
import multiprocessing
from appium import webdriver

def 获取当前系统():
    systeminfo = platform.platform()
    # print(systeminfo)
    if 'Windows' in systeminfo :
        systemname = 'windows'
    elif 'Darwin' in systeminfo :
        systemname = 'mac'
    else:
        systemname = 'linux'
    return systemname

def 获取控件文件信息(filename='app控件'):
    控件文件路径 = Path(__file__).cwd().parent / f'{filename}.yml'
    with open(控件文件路径,'r', encoding='gbk') as loadfile:
        info = yaml.load(loadfile)
    return info


def 启动appium_server(udid,port=4723):
    if 'mac' in 获取当前系统():
        excute_cmd_base = "node /Applications/Appium.app/Contents/Resources/app/node_modules/appium/build/lib/main.js"
    else:
        excute_cmd_base = "appium"
    excute_cmd = "{} -a 127.0.0.1 -p {} -U {} --session-override".format(excute_cmd_base,port,udid)

    subprocess.Popen()
    print(excute_cmd)

def cleanNodeProcess():
    是否mac = 'mac' in 获取当前系统()
    if 是否mac:
        execute_cmd = 'ps -A|grep node'
        cmd_res = subprocess.getoutput(execute_cmd)
        for res in cmd_res.split('\n'):
            if 'node /' in res:
                print(res)
                pid = re.split('\s+', res)[0]
                print(pid)
                kill_cmd = f'kill {pid}'
                kill_res = subprocess.getoutput(kill_cmd)
                print(kill_res)
    else:
        execute_cmd = 'tasklist|findstr node'
        cmd_res = subprocess.getoutput(execute_cmd)
        for res in cmd_res.split('\n'):
            if 'node.exe' in res:
                pid = re.split('\s+', res)[1]
                # print(pid)
                kill_cmd = f'taskkill /F /PID {pid}'
                kill_res = subprocess.getoutput(kill_cmd)
                print(kill_res)


def waittimeout(element,timeout=10):
    begintime = time.time()
    while begintime + timeout > time.time():
        if element is not None:
            break


def get_android_app_info(app="iRoom"):

    # get device name
    deviceId = subprocess.getoutput('adb devices').split('\n')[1].split("\t")[0]

    # get Android device systerm version
    deviceVersion = subprocess.getoutput('adb shell getprop ro.build.version.release')

    # get app package name and activity

    if 'mac' in 获取当前系统():
        find_exec = 'grep'
    else:
        find_exec = 'findstr'
    cmd_exec = f'adb shell dumpsys window w |{find_exec} \/|{find_exec} name='

    getappInfo = subprocess.getoutput(cmd_exec)
    appInfo = re.findall(r'com.+?tivity', getappInfo)[0].split('/')
    appPackage = appInfo[0]
    appActivity = appInfo[1]

    desired_caps = {
        'platformName': 'Android',
        'platformVersion': deviceVersion.rstrip('\n'),
        'deviceName': deviceId,
        'appPackage': appPackage,
        'appActivity': appActivity,
        'autoAcceptAlerts': 'true',
        'noReset': 'true'
    }

    print(desired_caps)
    return desired_caps

def get_ios_app_info():
    udid = os.popen('idevice_id --list').readlines()
    bundleid = os.popen("ideviceInstaller -l|grep PowerInfo").readlines()
    device_os_version = os.popen('ideviceinfo -k ProductVersion').readlines()

    desired_caps = {
        'platformName':'IOS',
        'platformVesion': device_os_version[0].rstrip(),
        'deviceName': 'IPhone',
        'automationName': 'XCUITest',
        'bundleId': bundleid[0].split(',')[0],
        'udid': udid[0].rstrip(),
        'noReset': 'true'
    }

    print(desired_caps)
    return desired_caps


class StartDriver():

    def __init__(self,devicelist):
        设备信息 = 获取控件文件信息('devices')
        self.aport = list(range(4723, 4800, 2))
        self.bport = list(range(4724, 4800, 2))
        self.iosport = list(range(8100,8200,2))
        self.devicelist = devicelist
        self.realdevice = [设备信息[device] for device in devicelist]


    def startAppiumServer(self,i):
        appium_env = os.environ['APPIUM']
        是否mac系统 = 'mac' in 获取当前系统()
        excute_cmd_base = f"node {appium_env}/Resources/app/node_modules/appium/build/lib/main.js -a 127.0.0.1"
        # print(excute_cmd_base)
        uidkey = 'udid' if 'IOS' in self.realdevice[i]['platformName'] else 'deviceName'

        deviceport = f'--webdriveragent-port {self.iosport[i]}' if 'IOS' in self.realdevice[i]['platformName'] else f'-bp {self.bport[i]}'
        # print(uidkey)
        excute_cmd = f"{excute_cmd_base} -p {self.aport[i]} {deviceport} -U {self.realdevice[i][uidkey]} --local-timezone --log-timestamp --command-timeout 3000"

        appiumlogpath = '/Users/liminglei/Desktop/appium/' if 是否mac系统 else 'c:/'

        subprocess.Popen(excute_cmd,shell=True,stdout=open(f"{appiumlogpath}appiumlog_{self.realdevice[i][uidkey]}.txt",'w+'))

        time.sleep(5)

    def getNodeProcPid(self):

        pidlist = []

        for i in range(len(self.devicelist)):
            if 'mac' in 获取当前系统():
                cmd = f'lsof -i:{self.aport[i]}'
            else:
                cmd = f'netstat -ano|findstr {self.aport[i]}'
            getportused = subprocess.getoutput(cmd)
            info = getportused.split('\n')
            if f':{self.aport[i]}' in getportused:
                pid = re.split('\s+', info[1])[1] if 'mac' in 获取当前系统() else re.split('\s+', info[0])[-1]
                pidlist.append(pid)

        # print(pidlist)
        return pidlist

    def killNodeProPid(self,pidlist):

        for pid in pidlist :
            subprocess.Popen(f'kill {pid}',shell=True)


def startMultAppiumServer(sd):

    proc_list = []

    for i in range(len(sd.devicelist)):
        proc_list.append(multiprocessing.Process(target=sd.startAppiumServer,args=(i,)))

    for pro in proc_list:
        pro.start()

    for pro in proc_list:
        pro.join()

