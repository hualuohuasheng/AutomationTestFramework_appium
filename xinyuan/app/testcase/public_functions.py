# -*- coding:utf-8 -*-

import subprocess
import sys
import os
import re
import socket
import cv2
import numpy as np
import requests
from selenium.webdriver import ActionChains
from time import sleep


def get_device_id():
    cmd = "adb devices"
    res = subprocess.getoutput(cmd)
    device_id = []
    if 'win32' in sys.platform:
        adb_info = res.split('\n')
        if len(adb_info) > 2:
            for info in adb_info[1:-1]:
                device_id.append(info.split('\t')[0])
        else:
            print("获取手机id出错：未发现手机")
    return device_id


def check_port_used(port, host="127.0.0.1"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, int(port)))
        s.shutdown(2)
        return True
    except WindowsError:
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


def stop_appium_server():
    if 'win32' in sys.platform:
        node_res = subprocess.getoutput("tasklist|findstr node")
        for res in node_res.split('\n'):
            if 'node.exe' in res:
                node_pid = re.findall('\\d+', res)[0]
                subprocess.getoutput(f"taskkill /F /PID {node_pid}")


class AppiumServer:

    @classmethod
    def get_port(cls, device, is_ios=False):
        cls.port = start_appium_server(device, is_ios)


def download_img_by_src(browser, img_element, img_save):
    # 获取到验证码图片的src链接后，下载保存到本地
    img_src = browser.find_element(img_element[0], img_element[1]).get_property('src')
    # print(img_src)
    res = requests.get(img_src)
    with open(img_save, 'wb') as f:
        f.write(res.content)


def read_img_file(cut_dir, back_dir):
    cut_image = cv2.imread(cut_dir)
    back_image = cv2.imread(back_dir)
    # print(back_image)
    cut_height, cut_width, _ = cut_image.shape
    back_height, back_width, _ = back_image.shape

    mid = (back_height - cut_height) // 2
    # print(mid)
    if mid > 0:
        back_image = back_image[mid: (back_height - mid), :]

    # print(back_image.shape)
    return cut_image, back_image


def best_match(back_canny, operator, cut_width, back_width):
    max_value, pos_x = 0, 0
    for x in range(cut_width, back_width - cut_width):
        block = back_canny[:, x:x + cut_width]
        value = (block * operator).sum()
        if value > max_value:
            max_value = value
            pos_x = x
    return pos_x, max_value


def get_back_canny(back_img):
    img_blur = cv2.GaussianBlur(back_img, (3, 3), 0)
    img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)
    img_canny = cv2.Canny(img_gray, 100, 200)

    # cv2.imshow('Canny', img_canny)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return img_canny


def get_operator(cut_img, cut_height, cut_width):
    cut_gray = cv2.cvtColor(cut_img, cv2.COLOR_BGR2GRAY)

    _, cut_binary = cv2.threshold(cut_gray, 127, 255, cv2.THRESH_BINARY)
    # 获取边界
    contours, hierarchy = cv2.findContours(cut_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # 获取最外层边界
    contour = contours[-1]
    # operator矩阵
    operator = np.zeros((cut_height, cut_width))
    # 根据 contour填写operator
    for point in contour:
        operator[point[0][1]][point[0][0]] = 1

    # cv2.imshow('operator', operator)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return operator


def get_distance(back_img, cut_img):
    back_height, back_width, _ = back_img.shape
    cut_height, cut_width, _ = cut_img.shape

    back_canny = get_back_canny(back_img)
    operator = get_operator(cut_img, cut_height, cut_width)
    pos_x, max_value = best_match(back_canny, operator, cut_width, back_width)
    print(pos_x, back_width)
    if pos_x > 10:
        pos_x += 10
    return pos_x


def slider_verification_code_163yidun(browser, cut_element, back_element, slider_element):
    while True:
        # 将验证码的背景图和滑块图片下载下来
        download_img_by_src(browser, back_element, 'back.jpg')
        download_img_by_src(browser, cut_element, 'cut.png')
        sleep(1)
        cut_image, back_image = read_img_file('cut.png', 'back.jpg')
        distance = get_distance(back_img=back_image, cut_img=cut_image)
        print(distance)
        if distance:
            action = ActionChains(browser)
            action.click_and_hold(browser.find_element(slider_element[0], slider_element[1])).perform()
            # tracks = get_track(distance)
            # for i in tracks:
            action.move_by_offset(xoffset=distance, yoffset=-1).perform()
            action = ActionChains(browser)
            sleep(1)
            action.release().perform()
            sleep(5)
        if re.findall("订单", browser.page_source, re.S):
            break
        if '失败过多，点此重试' in browser.page_source:
            browser.find_element_by_xpath("//span[@class='yidun_tips__text']").click()
