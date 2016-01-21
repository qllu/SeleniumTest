# coding=utf-8
"""
Created on 2015年10月14日
1.施設グループが追加されること
2.施設が追加されること
@author: QLLU
"""
# 导入需要的公共函数类
import time
import unittest
import sys
import os

sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from CommonFunction.DataReader import DataReader
from CommonFunction.Operations import Operations
from CommonFunction.WebDriver import WebDriver

def add_facility_group():
    global group_url, group_detail_url
    # 进入日程安排系统后台，添加设备组
    garoon_url = WebDriver().testurl("qatest01") + "/g/system/application_list.csp?app_id="
    WebDriver().geturl(garoon_url)
    driver.wait(2)
    WebDriver().click("byid", "schedule")
    WebDriver().click("byid", "schedule/system/facility_group")
    WebDriver().click("byid", "schedule/system/facility_group_add")
    driver.wait(2)
    WebDriver().input("byname", "facilitygroupName-def", "fac_group1")
    WebDriver().input("byname", "memo", "this is a facility group")
    WebDriver().click("byid", "facility_group_add_submit")
    WebDriver().click("bylink", "fac_group1")
    group_url = WebDriver().currenturl()
    # 点击设备组进入详情
    WebDriver().click("byxpath", "//div[2]/span/a")
    driver.wait(2)
    group_detail_url = WebDriver().currenturl()

def add_facility():
    global fac_detail_url
    WebDriver().geturl(group_url)
    driver.wait(3)
    WebDriver().click("byid", "schedule/system/facility_add")
    WebDriver().input("byname", "facilityName-def", "fac1")
    WebDriver().input("byname", "facility_code", "fac1_code")
    WebDriver().input("byname", "memo", "this is a facility")
    WebDriver().click("byid", "facility_add_submit")
    # 点击进入设备详情
    WebDriver().click("byxpath", "//td[2]/span/a")
    fac_detail_url = WebDriver().currenturl()

def del_fac():
    WebDriver().geturl(fac_detail_url)
    driver.wait(3)
    WebDriver().click("byxpath", "//span[2]/span[2]/span/a")
    WebDriver().click("bycss", "input.margin")
    # 删除设备组
    WebDriver().geturl(group_detail_url)
    driver.wait(3)
    WebDriver().click("byxpath", "//span[2]/span[2]/span/a")
    WebDriver().click("bycss", "input.margin")

class AddFacilityGroup(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        global domain, driver
        domain = "qatest01"
        driver = WebDriver("open", "firefox", "local")
        driver.open(domain, "slash")  # 打开浏览器，并打开forest

    def test1_add_facility_group(self):
        global group_url, group_detail_url
        dataoper = DataReader('QT_Sche_add_facility_group.xml')
        Operations().login(dataoper.readxml('login', 0, 'username'),
                              dataoper.readxml('login', 0, 'password'))
        driver.wait(3)
        add_facility_group()
        check1 = driver.gettext("bycss", "td")
        check2 = driver.gettext("byxpath", "//tr[4]/td")
        self.assertEqual(check1, "fac_group1"), "设备组名称验证失败"
        self.assertEqual(check2, "this is a facility group") ,"设备组备注验证失败"


    def test2_add_facility(self):
        add_facility()
        check3 = driver.gettext("bycss", "td")
        self.assertEqual(check3, "fac1")


    @classmethod
    def tearDownClass(self):
        # 清空数据
        try:
            del_fac()
        except Exception as msg:
            print msg, "Data has not been removed."
        finally:
            driver.close()


if __name__ == "__main__":
    unittest.main()
