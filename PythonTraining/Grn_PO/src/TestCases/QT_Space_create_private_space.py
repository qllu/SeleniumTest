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
        global domain, driver
        domain = "qatest01"
        driver = WebDriver("open", "firefox", "local")
        driver.open(domain, "slash")  # 打开浏览器，并打开forest

    def test1_create_private_space(self):
        global dataoper, detail_url, current_url
        # 读取测试数据并登录
        dataoper = DataReader('QT_Space_create_private_space.xml')
        Operations().login(dataoper.readxml('login', 0, 'username'),
                           dataoper.readxml('login', 0, 'password'))
        time.sleep(2)
        # 点击进入Garoon
        driver.open(domain, "g")
        time.sleep(1)
        # 点击进入space
        driver.click('bycss', dataoper.readxml('space', 0, 'space_icon'))
        time.sleep(2)
        # 创建space
        driver.click('bylink', dataoper.readxml('space', 0, 'creat_link'))
        time.sleep(1)
        # 输入title
        driver.input('byid', dataoper.readxml('space', 0, 'space_title'),
                                   dataoper.readxml('space', 0, 'title'))
        time.sleep(1)
        # 搜索添加用户
        driver.input('byname', dataoper.readxml('space', 0, 'e_keyword'),
                                   dataoper.readxml('space', 0, 'keyword'))
        time.sleep(1)
        driver.click('byxpath', dataoper.readxml('space', 0, 'search'))
        time.sleep(1)
        driver.click('byid', dataoper.readxml('space', 0, 'add_user'))
        time.sleep(1)
        # 选择公开方式
        driver.click('byid', dataoper.readxml('space', 0, 'private'))

        # 保存
        driver.click('byid', dataoper.readxml('space', 0, 'save'))
        time.sleep(1)
        current_url = driver.currenturl()
        # print "current_url:", current_url

        # 进入详细页面,并获取url
        driver.click('byid', dataoper.readxml('space', 0, 'droplist'))
        time.sleep(1)
        driver.click('bylink', dataoper.readxml('space', 0, 'detail'))
        time.sleep(1)
        detail_url = driver.currenturl()

        # 验证：1.确认space名称；2.确认公开方式
        check = driver.gettext('bycss', dataoper.readxml('space', 0, 'check'))
        check2 = driver.gettext('byxpath', dataoper.readxml('space', 0, 'check2'))
        value = dataoper.readxml('space', 0, 'value')
        value2 = dataoper.readxml('space', 0, 'value2')
        self.assertEqual(check, value), u"space名称不匹配，验证失败"
        self.assertEqual(check2, value2), u"公开方式不匹配，验证失败"

    def test2_member_confirm(self):
        # 使用space成员确认
        Operations().login(dataoper.readxml('confirm', 1, 'username'),
                              dataoper.readxml('confirm', 1, 'password'))
        driver.geturl(current_url)
        time.sleep(2)

        # 确认是否能正常访问
        if driver.is_element_present('byclass', dataoper.readxml('confirm', 1, 'element')) is False:
            print "不能正常访问space"
            assert False

    def test3_other_user_confirm(self):
        # 使用其他用户确认
        Operations().login(dataoper.readxml('confirm', 0, 'username'),
                              dataoper.readxml('confirm', 0, 'password'))
        time.sleep(1)
        # print "open current_url by other user..."
        driver.geturl(current_url)
        time.sleep(2)
        # 确认是否显示错误页面
        if driver.is_element_present('byclass', dataoper.readxml('confirm', 0, 'element')) is False:
            print "space以外的成员不能访问"
            assert False

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
            driver.geturl(detail_url)
            time.sleep(2)
            driver.click('byid', dataoper.readxml('space', 0, 'delete_link'))
            time.sleep(2)
            driver.click('byxpath', dataoper.readxml('space', 0, 'delete_yes'))
            time.sleep(2)
        except NoSuchElementException as msg:
            print msg, "Data has not been removed."
        finally:
            driver.close()  # 关闭浏览器


if __name__ == "__main__":
    unittest.main()
