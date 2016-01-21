# coding=utf-8
'''
Created on 2015年10月14日
1.スペースのメンバーが作成したスペースを閲覧できること
2.スペースの参加者以外も作成されたスペースを閲覧できること
@author: QLLU
'''
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
from selenium.common.exceptions import NoSuchElementException


class CreatePublicSpace(unittest.TestCase):
    '''
    新增space目录
    '''
    @classmethod
    def setUpClass(self):
        global domain, driver
        domain = "qatest01"
        driver = WebDriver("open", "firefox", "local")
        driver.open(domain, "slash")  # 打开浏览器，并打开forest

    def test1_create_public_space(self):
        global dataoper, detail_url, current_url
        # 读取测试数据并登录
        dataoper = DataReader('QT_Space_create_public_space.xml')
        Operations().login(dataoper.readxml('login', 0, 'username'),
                              dataoper.readxml('login', 0, 'password'))
        driver.wait(3)
        # 点击进入Garoon
        driver.open(domain, "g")
        driver.wait(2)
        # 点击进入space
        driver.click('bycss', dataoper.readxml('space', 0, 'space_icon'))
        driver.wait(3)
        # 创建space
        driver.click('bylink', dataoper.readxml('space', 0, 'creat_link'))
        driver.wait(2)
        # 输入title
        driver.input('byid', dataoper.readxml('space', 0, 'space_title'),
                                dataoper.readxml('space', 0, 'title'))
        driver.wait(2)
        # 搜索添加用户
        driver.input('byname', dataoper.readxml('space', 0, 'e_keyword'),
                                dataoper.readxml('space', 0, 'keyword'))
        driver.wait(2)
        driver.click('byxpath', dataoper.readxml('space', 0, 'search'))
        driver.wait(2)
        driver.click('byid', dataoper.readxml('space', 0, 'add_user'))
        driver.wait(2)
        # 选择公开方式
        driver.click('byid', dataoper.readxml('space', 0, 'public'))
        # 保存
        driver.click('byid', dataoper.readxml('space', 0, 'save'))
        driver.wait(2)
        current_url = driver.currenturl()
        # print "current_url:", current_url
        # 进入详细页面
        driver.click('byid', dataoper.readxml('space', 0, 'droplist'))
        driver.wait(2)
        driver.click('bylink', dataoper.readxml('space', 0, 'detail'))
        driver.wait(2)
        detail_url = driver.currenturl()
        # 验证：1.确认space名称；2.确认公开方式
        check = driver.gettext('byxpath', dataoper.readxml('space', 0, 'check'))
        check2 = driver.gettext('byxpath', dataoper.readxml('space', 0, u'check2'))
        value = dataoper.readxml('space', 0, 'value')
        value2 = dataoper.readxml('space', 0, u'value2')

        self.assertEqual(value, check), "space名称不匹配，验证失败"
        self.assertEqual(value2, check2), "space公开方式不匹配，验证失败"

    def test2_member_confirm(self):
        # 成员用户确认
        Operations().login(dataoper.readxml('confirm', 1, 'username'),
                              dataoper.readxml('confirm', 1, 'password'))
        # print "open current_url by other user..."
        driver.geturl(current_url)
        driver.wait(3)
        # 确认是否存在元素
        if driver.is_element_present('byclass', dataoper.readxml('confirm', 1, 'element')) is False:
            print "元素验证失败"
            assert False

    def test3_other_user_confirm(self):
        # 使用其他用户确认
        Operations().login(dataoper.readxml('confirm', 0, 'username'),
                              dataoper.readxml('confirm', 0, 'password'))
        # print "open current_url by other user..."
        driver.geturl(current_url)
        driver.wait(3)
        # 确认是否存在元素
        if driver.is_element_present('byclass', dataoper.readxml('confirm', 0, 'element')) is False:
            print "元素验证失败"
            assert False

    def test4_delete_space(self):
        Operations().login(dataoper.readxml('login', 0, 'username'), dataoper.readxml('login', 0, 'password'))
        driver.wait(3)
        driver.geturl(detail_url)
        driver.wait(3)
        driver.click('byid', dataoper.readxml('space', 0, 'delete_link'))
        driver.wait(3)
        try:
            driver.click('byxpath', dataoper.readxml('space', 0, 'delete_yes'))
            driver.wait(3)
        except Exception as msg:
            print msg

    def tearDown(self):
        # 退出
        Operations().logout()

    @classmethod
    def tearDownClass(self):
        # 关闭浏览器
        driver.close()


if __name__ == "__main__":
    unittest.main()
