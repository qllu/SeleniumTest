# coding=utf-8
"""
Created on 2015年10月14日
1.通常予定が登録されること
2.参加者に予定の共有者が含まれていること
3.ファイルが添付されておりダウンロードできること
4.施設欄に施設が含まれていること
@author: QLLU
"""
# 导入需要的公共函数类
import time, unittest, sys, os
from selenium.common.exceptions import NoSuchElementException
sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from CommonFunction.DataReader import DataReader
from CommonFunction.Operations import Operations
from CommonFunction.WebDriver import WebDriver


class AddSche(unittest.TestCase):

    def setUp(self):
        WebDriver("open","firefox","local").open("qatest01")  # 打开浏览器，并打开forest

    def test1_add_sche_with_users_facility(self):
        dataoper = DataReader('QT_Sche_add_facility_group.xml')
        Operations().login(dataoper.readxml('login', 0, 'username'),
                              dataoper.readxml('login', 0, 'password'))
        time.sleep(2)


    def tearDown(self):
        # 清空数据
        pass


if __name__ == "__main__":
    unittest.main()
