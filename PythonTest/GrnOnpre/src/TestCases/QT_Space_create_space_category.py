# coding=utf-8
"""
Created on 2015年10月9日
カテゴリが作成されること
@author: QLLU
"""
# 导入需要的公共函数类
import time, unittest, sys, os
sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from CommonFunction.DataReader import DataReader
from CommonFunction.QT_Operations import QT_Operations
from CommonFunction.WebDriverHelp import WebDriverHelp


class CreateSpaceCategory(unittest.TestCase):
    '''
    新增space目录
    '''

    def setUp(self):
        WebDriverHelp("open", "firefox", "local").setup("fcn")  # 打开浏览器，并打开forest

    def test_create_space_category(self):
        global dataoper, detail_url

        # 读取测试数据
        dataoper = DataReader('QT_Space_create_space_category.xml')

        # 登录用户
        QT_Operations().login(dataoper.readxml('login', 0, 'username'),
                              dataoper.readxml('login', 0, 'password'))
        time.sleep(2)

        # 点击进入garoon各应用程序管理
        system_url = "https://qatest01.cybozu.cn/g/system/application_list.csp?app_id="
        WebDriverHelp().geturl(system_url)
        time.sleep(2)

        # 点击进入space
        WebDriverHelp().clickitem('byid', dataoper.readxml('space', 0, 'space_link'))
        time.sleep(2)

        # 点击进入类别设置
        WebDriverHelp().clickitem('byid', dataoper.readxml('space', 0, 'cate_set'))
        time.sleep(1)

        # 点击添加目录按钮
        WebDriverHelp().clickitem('bylink', dataoper.readxml('space', 0, u'add_link'))
        time.sleep(1)

        # 输入类别名称
        WebDriverHelp().inputvalue('byid', dataoper.readxml('space', 0, 'cate_name'),
                                   dataoper.readxml('space', 0, 'name'))
        time.sleep(1)

        # 输入类别备注
        WebDriverHelp().inputvalue('byname', dataoper.readxml('space', 0, 'e_comment'),
                                   dataoper.readxml('space', 0, 'comment'))
        time.sleep(1)

        # 保存
        WebDriverHelp().clickitem('bycss', dataoper.readxml('space', 0, 'save'))
        time.sleep(2)

        # 进入详细页面
        WebDriverHelp().clickitem('bylink', dataoper.readxml('space', 0, 'cate_detail'))
        time.sleep(2)
        detail_url = WebDriverHelp().currenturl()

        # 验证
        check = WebDriverHelp().gettext('byxpath', dataoper.readxml('space', 0, 'check'))
        check2 = WebDriverHelp().gettext('byxpath', dataoper.readxml('space', 0, 'check2'))
        # print "check:", check
        value = dataoper.readxml('space', 0, 'value')
        value2 = dataoper.readxml('space', 0, 'value2')
        # print "value:", value
        # self.assertEqual(check,value)
        # self.assertEqual(check2,value2)
        try:
            self.assertEqual(check, value)
            self.assertEqual(check2, value2)
        except AssertionError, msg:
            print msg

    def tearDown(self):
        # 清空数据
        try:
            WebDriverHelp().geturl(detail_url)
            time.sleep(2)
            WebDriverHelp().clickitem('byxpath', dataoper.readxml('space', 0, 'delete_link'))
            time.sleep(1)
            WebDriverHelp().clickitem('byxpath', dataoper.readxml('space', 0, 'delete'))
        except Exception as msg:
            print msg
        finally:
            WebDriverHelp().teardown()  # 关闭浏览器


if __name__ == "__main__":
    unittest.main()
