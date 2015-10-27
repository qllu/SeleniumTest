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
from CommonFunction.Operations import Operations
from CommonFunction.WebDriver import WebDriver


class CreateSpaceCategory(unittest.TestCase):
    '''
    新增space目录
    '''

    def setUp(self):
        WebDriver("open", "firefox", "local").setup("fcn")  # 打开浏览器，并打开forest

    def test_create_space_category(self):
        global dataoper, detail_url

        # 读取测试数据
        dataoper = DataReader('QT_Space_create_space_category.xml')

        # 登录用户
        Operations().login(dataoper.readxml('login', 0, 'username'),
                              dataoper.readxml('login', 0, 'password'))
        time.sleep(2)

        # 点击进入garoon各应用程序管理
        # system_url = "https://qatest01.cybozu.cn/g/system/application_list.csp?app_id="
        system_url = WebDriver().testurl("qatest01") + "/g/system/application_list.csp?app_id="
        WebDriver().geturl(system_url)
        time.sleep(2)

        # 点击进入space
        WebDriver().clickitem('byid', dataoper.readxml('space', 0, 'space_link'))
        time.sleep(2)

        # 点击进入类别设置
        WebDriver().clickitem('byid', dataoper.readxml('space', 0, 'cate_set'))
        time.sleep(1)

        # 点击添加目录按钮
        WebDriver().clickitem('bylink', dataoper.readxml('space', 0, u'add_link'))
        time.sleep(1)

        # 输入类别名称
        WebDriver().inputvalue('byid', dataoper.readxml('space', 0, 'cate_name'),
                                   dataoper.readxml('space', 0, 'name'))
        time.sleep(1)

        # 输入类别备注
        WebDriver().inputvalue('byname', dataoper.readxml('space', 0, 'e_comment'),
                                   dataoper.readxml('space', 0, 'comment'))
        time.sleep(1)

        # 保存
        WebDriver().clickitem('bycss', dataoper.readxml('space', 0, 'save'))
        time.sleep(2)

        # 进入详细页面
        WebDriver().clickitem('bylink', dataoper.readxml('space', 0, 'cate_detail'))
        time.sleep(2)
        detail_url = WebDriver().currenturl()

        # 验证，1.类别名称，2.类别说明
        check = WebDriver().gettext('byxpath', dataoper.readxml('space', 0, 'check'))
        check2 = WebDriver().gettext('byxpath', dataoper.readxml('space', 0, 'check2'))
        # print "check:", check
        value = dataoper.readxml('space', 0, 'value')
        value2 = dataoper.readxml('space', 0, 'value2')
        # print "value:", value
        self.assertEqual(check,value), "类别名称不匹配，验证失败"
        self.assertEqual(check2,value2), "类别说明不匹配，验证失败"

    def tearDown(self):
        # 清空数据
        try:
            WebDriver().geturl(detail_url)
            time.sleep(2)
            WebDriver().clickitem('byxpath', dataoper.readxml('space', 0, 'delete_link'))
            time.sleep(1)
            WebDriver().clickitem('byxpath', dataoper.readxml('space', 0, 'delete'))
        except Exception as msg:
            print msg
        else:
            print "space类别已清除"
        finally:
            WebDriver().teardown()  # 关闭浏览器


if __name__ == "__main__":
    unittest.main()
