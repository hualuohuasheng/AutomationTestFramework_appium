# -*- coding:utf-8 -*-

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://imweb32.powzamedia.com:8123/login#/index")

driver.find_element_by_id('name').send_keys('manager')
driver.find_element_by_id('pass').send_keys('manager')
driver.find_element_by_class_name('ng-isolate-scope').click()
driver.find_element_by_class_name('bg-olive').click()

driver.find_element_by_css_selector('.fa.fa-fw.fa-sitemap').click()

sleep(2)

driver.find_element_by_xpath("//*[@id='step2']/li[5]/ul/li[3]/a").click()

sleep(2)
#增加配置
#查询修改配置 fa-search
#下发配置 fa-download
#导出配置 fa-sign-out
driver.find_element_by_class_name('fa-plus').click()

sleep(2)

s = driver.find_element_by_name('ConfigurationTemplate')

print(s)

Select(s).select_by_index(1)

ops = Select(s).all_selected_options()
print(ops)

for op in ops:
    print(op)