# coding=utf-8
"""
Created on 2015年10月14日
1.施設グループが追加されること
2.施設が追加されること
@author: QLLU
"""
# 导入需要的公共函数类
import time, unittest, sys, os
sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from CommonFunction.DataReader import DataReader
from CommonFunction.Operations import Operations
from CommonFunction.WebDriver import WebDriver


class AddFacilityGroup(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        WebDriver("open", "firefox", "local").setup("qatest01")  # 打开浏览器，并打开forest

    def test1_add_facility_group(self):
        global group_url, group_detail_url
        dataoper = DataReader('QT_Sche_add_facility_group.xml')
        Operations().login(dataoper.readxml('login', 0, 'username'),
                              dataoper.readxml('login', 0, 'password'))
        time.sleep(2)
        # 进入日程安排系统后台
        garoon_url = WebDriver().testurl("qatest01") + "/g/system/application_list.csp?app_id="
        WebDriver().geturl(garoon_url)
        time.sleep(1)
        WebDriver().clickitem("byid", "schedule")
        WebDriver().clickitem("byid", "schedule/system/facility_group")
        WebDriver().clickitem("byid", "schedule/system/facility_group_add")
        time.sleep(1)
        WebDriver().inputvalue("byname", "facilitygroupName-def", "test")
        WebDriver().inputvalue("byname", "memo", "this is a facility group")
        WebDriver().clickitem("byid", "facility_group_add_submit")
        group_url = WebDriver().currenturl()
        # 点击设备组进入详情
        WebDriver().clickitem("bylink", "fac_group1")
        WebDriver().clickitem("byxpath", "//div[2]/span/a")
        group_detail_url = WebDriver().currenturl()
        check1 = WebDriver().gettext("bycss", "td")
        check2 = WebDriver().gettext("byxpath", "//tr[4]/td")
        self.assertEqual(check1, "fac_group1")
        self.assertEqual(check2, "this is a facility group")

    def test2_add_facility(self):
        WebDriver().geturl(group_url)
        time.sleep(2)
        WebDriver().clickitem("byid", "schedule/system/facility_add")
        WebDriver().inputvalue("byname", "facilityName-def", "fac1")
        WebDriver().inputvalue("byname", "facility_code", "fac1_code")
        WebDriver().inputvalue("byname", "memo", "this is a facility")
        WebDriver().clickitem("byid", "facility_add_submit")
        time.sleep(2)
        # 点击进入设备详情
        WebDriver().clickitem("bylink", "fac1")
        check3 = WebDriver().gettext("bycss", "td")
        self.assertEqual(check3, "fac1")

    @classmethod
    def tearDownClass(self):
        # 清空数据
        try:
            WebDriver().clickitem("bylink", "test")
            WebDriver().clickitem("byxpath", "//div[2]/span/a")
            WebDriver().clickitem("byxpath", "//span[2]/span[2]/span/a")
            time.sleep(1)
            WebDriver().clickitem("bycss", "input.margin")
        except Exception as msg:
            print msg
        finally:
            WebDriver().teardown()


if __name__ == "__main__":
    unittest.main()
