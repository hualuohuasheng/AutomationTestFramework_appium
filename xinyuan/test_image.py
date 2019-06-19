# -*-coding:utf-8 -*-
from PIL import Image
from PIL import ImageChops
import cv2
import numpy as np
import os


def get_cut_new_img(imgfile):
    img = cv2.imread(imgfile)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 1)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    draw_img3 = cv2.drawContours(img.copy(), contours, -1, (0, 0, 255), 3)
    # cv2.imshow("draw_img3", draw_img3)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    newimg = img.copy()
    x, y, w, h = cv2.boundingRect(contours[-1])
    cv2.rectangle(newimg, (x, y), (x + w, y + h), (0, 0, 255), 3)
    print(x, y)
    newimage = img[y + 2:y + h - 2, x + 2:x + w - 2]  # 先用y确定高，再用x确定宽
    cv2.imwrite("new1.png", newimage)

    captcha = Image.open('1.png')
    captcha_bg = Image.open('D:/1/1.png')
    diff = ImageChops.difference(captcha, captcha_bg)


# get_cut_new_img('2.png')


def test_Canny():
    img = cv2.imread("1.png", 0)
    cv2.imwrite("canny1.jpg", cv2.Canny(img, 200, 300))
    cv2.imshow("canny", cv2.imread("canny1.jpg"))
    cv2.waitKey()
    cv2.destroyAllWindows()


def get_distance(target, template):
    img_rgb = cv2.imread(target)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)  # 将图像从一个颜色空间转换为另一个颜色空间
    temp = cv2.imread(template, 0)
    run = 1
    w, h = temp.shape[::-1]
    res = cv2.matchTemplate(img_gray, temp, cv2.TM_CCOEFF_NORMED)
    L = 0
    R = 1
    flag = 0
    # while run < 20:
    while not flag:
        run += 1
        threshold = (R + L) / 2.
        # print threshold
        if threshold < 0:
            print
            'get_distance Error'
            return None
        loc = np.where(res >= threshold)
        # print len(loc[1])
        if len(loc[1]) > 1:
            L += (R - L) / 2.
        elif len(loc[1]) == 1:
            print
            '目标区域起点x坐标为：%d' % loc[1][0]
            flag = 1
        # break
        else:
            R -= (R - L) / 2.
    # 展示圈出来的区域
    for pt in zip(*loc[::-1]):
    	cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7, 249, 151), 2)
    cv2.imshow('Detected', img_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return loc[1][0]


def match(target, template):
    img_rgb = cv2.imread(target)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(template, 0)
    run = 1
    w, h = template.shape[::-1]
    print(w, h)
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    run = 1

    # 使用二分法查找阈值的精确值
    L = 0
    R = 1
    while run < 20:
        run += 1
        threshold = (R + L) / 2
        print(threshold)
        if threshold < 0:
            print('Error')
            return None
        loc = np.where(res >= threshold)
        print(len(loc[1]))
        if len(loc[1]) > 1:
            L += (R - L) / 2
        elif len(loc[1]) == 1:
            print('目标区域起点x坐标为：%d' % loc[1][0])
            break
        elif len(loc[1]) < 1:
            R -= (R - L)/2

        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7, 249, 151), 2)
        cv2.imshow('Detected', img_rgb)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return loc[1][0]


def match_img(target, template):
    image = cv2.imread(target)

    # 预处理，转换为灰度图片
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 高斯处理
    gray = cv2.GaussianBlur(gray, (3, 3), 1)
    # 二值化处理
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    draw_img3 = cv2.drawContours(gray.copy(), contours, 2, (0, 0, 255), 3)

    print(len(contours))
    cv2.imshow('binary', draw_img3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# match_img('1.png', 'new.png')


def koutu():
    img = cv2.imread('2.png')
    rect = (275, 120, 170, 320)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    x, y, w, h = cv2.boundingRect(contours[-1])
    rect = (y + 2, y + h - 2, x + 2,x + w - 2)
    print(x, y,x+w,y+h)
    print(rect)
    mask = np.zeros(img.shape[:2], np.uint8)
    bgModel = np.zeros((1, 65), np.float64)
    fgModel = np.zeros((1, 65), np.float64)
    cv2.grabCut(img, mask, rect, bgModel, fgModel, 5, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype(np.uint8)

    out = img * mask2[:, :, np.newaxis]

    cv2.imshow('output', out)
    cv2.waitKey()

koutu()