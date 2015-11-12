# coding=utf-8
'''
Created on 2015年10月19日
?スペースのメンバーが作成したスペースを閲覧できること
?スペースの参加者以外は作成されたスペースを閲覧できないこと
@author: QLLU
'''
# 导入需要的公共函数类
import time
import unittest
import sys
import os
from selenium.common.exceptions import NoSuchElementException

sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from CommonFunction.DataReader import DataReader
from CommonFunction.Operations import Operations
from CommonFunction.WebDriver import WebDriver


class CreatePrivateSpace(unittest.TestCase):
    '''
    新增space目录
    '''

    @classmethod
    def setUpClass(self):
        WebDriver("open", "firefox", "local").open("qatest01")  # 打开浏览器，并打开forest

    def test1_create_private_space(self):
        global dataoper, detail_url, current_url
        # 读取测试数据并登录
        dataoper = DataReader('QT_Space_create_private_space.xml')
        Operations().login(dataoper.readxml('login', 0, 'username'),
                           dataoper.readxml('login', 0, 'password'))
        time.sleep(2)
        # 点击进入Garoon
        garoon_url = WebDriver().testurl("qatest01") + "/g/"
        WebDriver().geturl(garoon_url)
        time.sleep(1)
        # 点击进入space
        WebDriver().click('bycss', dataoper.readxml('space', 0, 'space_icon'))
        time.sleep(2)
        # 创建space
        WebDriver().click('bylink', dataoper.readxml('space', 0, 'creat_link'))
        time.sleep(1)
        # 输入title
        WebDriver().input('byid', dataoper.readxml('space', 0, 'space_title'),
                                   dataoper.readxml('space', 0, 'title'))
        time.sleep(1)
        # 搜索添加用户
        WebDriver().input('byname', dataoper.readxml('space', 0, 'e_keyword'),
                                   dataoper.readxml('space', 0, 'keyword'))
        time.sleep(1)
        WebDriver().click('byxpath', dataoper.readxml('space', 0, 'search'))
        time.sleep(1)
        WebDriver().click('byid', dataoper.readxml('space', 0, 'add_user'))
        time.sleep(1)
        # 选择公开方式
        WebDriver().click('byid', dataoper.readxml('space', 0, 'private'))

        # 保存
        WebDriver().click('byid', dataoper.readxml('space', 0, 'save'))
        time.sleep(1)
        current_url = WebDriver().currenturl()
        # print "current_url:", current_url

        # 进入详细页面,并获取url
        WebDriver().click('byid', dataoper.readxml('space', 0, 'droplist'))
        time.sleep(1)
        WebDriver().click('bylink', dataoper.readxml('space', 0, 'detail'))
        time.sleep(1)
        detail_url = WebDriver().currenturl()

        # 验证：1.确认space名称；2.确认公开方式
        check = WebDriver().gettext('bycss', dataoper.readxml('space', 0, 'check'))
        check2 = WebDriver().gettext('byxpath', dataoper.readxml('space', 0, 'check2'))
        value = dataoper.readxml('space', 0, 'value')
        value2 = dataoper.readxml('space', 0, 'value2')
        self.assertEqual(check, value), u"space名称不匹配，验证失败"
        self.assertEqual(check2, value2), u"公开方式不匹配，验证失败"

    def test2_member_confirm(self):
        # 使用space成员确认
        Operations().login(dataoper.readxml('confirm', 1, 'username'),
                              dataoper.readxml('confirm', 1, 'password'))
        WebDriver().geturl(current_url)
        time.sleep(2)

        # 确认是否能正常访问
        try:
            WebDriver().is_element_present('byclass', dataoper.readxml('confirm', 1, 'element'))
        except NoSuchElementException as msg:
            print msg
        else:
            print "space成员确认可以访问"

    def test3_other_confirm(self):
        # 使用其他用户确认
        Operations().login(dataoper.readxml('confirm', 0, 'username'),
                              dataoper.readxml('confirm', 0, 'password'))
        time.sleep(1)
        # print "open current_url by other user..."
        WebDriver().geturl(current_url)
        time.sleep(2)
        # 确认是否显示错误页面
        try:
            WebDriver().is_element_present('byclass', dataoper.readxml('confirm', 0, 'element'))
        except NoSuchElementException as msg:
            print msg
        else:
            print "space以外的成员不能访问"

    def tearDown(self):
        # 退出
        Operations().logout()

    @classmethod
    def tearDownClass(self):
        # 清空数据
        try:
            Operations().login(dataoper.readxml('login', 0, 'username'),
                               dataoper.readxml('login', 0, 'password'))
            time.sleep(2)
            WebDriver().geturl(detail_url)
            time.sleep(2)
            WebDriver().click('byid', dataoper.readxml('space', 0, 'delete_link'))
            time.sleep(2)
            WebDriver().click('byxpath', dataoper.readxml('space', 0, 'delete_yes'))
            time.sleep(2)
        except NoSuchElementException as msg:
            print msg
        else:
            print "space数据已清除"
        finally:
            WebDriver().close()  # 关闭浏览器


if __name__ == "__main__":
    unittest.main()
