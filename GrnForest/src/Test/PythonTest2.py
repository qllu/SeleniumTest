#!/usr/bin/env python
#encoding: utf-8

#coding=utf-8
from selenium import webdriver
import time


#实例化一个火狐配置文件
fp = webdriver.FirefoxProfile()

#设置各项参数，参数可以通过在浏览器地址栏中输入about:config查看。

#设置成0代表下载到浏览器默认下载路径；设置成2则可以保存到指定目录
fp.set_preference("browser.download.folderList",2)


#是否显示开始,(个人实验，不管设成True还是False，都不显示开始，直接下载)
fp.set_preference("browser.download.manager.showWhenStarting",False)


#下载到指定目录
fp.set_preference("browser.download.dir","d:\\test")

#不询问下载路径；后面的参数为要下载页面的Content-type的值
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/octet-stream")

dr = webdriver.Firefox(firefox_profile=fp)

dr.get("https://pypi.python.org/pypi/selenium")
time.sleep(2)
dr.find_elements_by_xpath(".//*[@id='content']/div[3]/table/tbody/tr[3]/td[1]/span/a[1]").click()





