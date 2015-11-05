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


class AllowAttacheFiles(unittest.TestCase):

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
        WebDriver().clickitem("byid", "schedule/system/common_set")



    def test2_confirm(self):
        global fac_detail_url
        WebDriver().geturl(group_url)
        time.sleep(2)
        WebDriver().clickitem("byid", "schedule/system/facility_add")
        WebDriver().inputvalue("byname", "facilityName-def", "fac1")
        WebDriver().inputvalue("byname", "facility_code", "fac1_code")
        WebDriver().inputvalue("byname", "memo", "this is a facility")
        WebDriver().clickitem("byid", "facility_add_submit")
        time.sleep(2)
        # 点击进入设备详情
        WebDriver().clickitem("byxpath", "//td[2]/span/a")
        check3 = WebDriver().gettext("bycss", "td")
        self.assertEqual(check3, "fac1")
        fac_detail_url = WebDriver().currenturl()

    @classmethod
    def tearDownClass(self):
        # 清空数据
        try:
            # 删除设备
            WebDriver().geturl(fac_detail_url)
            time.sleep(2)
            WebDriver().clickitem("byxpath", "//span[2]/span[2]/span/a")
            WebDriver().clickitem("bycss", "input.margin")
            # 删除设备组
            WebDriver().geturl(group_detail_url)
            time.sleep(2)
            WebDriver().clickitem("byxpath", "//span[2]/span[2]/span/a")
            WebDriver().clickitem("bycss", "input.margin")
        except Exception as msg:
            print msg, "数据无法还原"
        finally:
            WebDriver().teardown()


if __name__ == "__main__":
    unittest.main()
