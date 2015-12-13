# coding=utf-8
"""
Created on 2015年10月14日
1.共有ToDoを登録できること
2.共有ToDoタブで、担当者に設定されたユーザーにToDoが追加されていること
@author: QLLU
"""
# 导入需要的公共函数类
import time, unittest, sys, os

sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from CommonFunction.DataReader import DataReader
from CommonFunction.Operations import Operations
from CommonFunction.WebDriver import WebDriver



class AddShareTodo(unittest.TestCase):
    '''
    新增space目录
    '''
    @classmethod
    def setUpClass(self):
        global domain
        domain = "qatest01"
        WebDriver("open", "firefox", "local").open(domain, "slash")  # 打开浏览器，并打开forest

    def test1_add_share_todo(self):
        # 新建space
        global dataoper, space_url
        # 读取测试数据并登录
        dataoper = DataReader('QT_Space_add_share_todo.xml')
        Operations().login(dataoper.readxml('login', 0, 'username'),
                              dataoper.readxml('login', 0, 'password'))
        time.sleep(2)

        # 点击进入Garoon
        WebDriver().open(domain, "g")
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
        # 搜索添加用户
        WebDriver().input('byname', dataoper.readxml('space', 0, 'e_keyword'),
                                   dataoper.readxml('space', 0, 'keyword'))
        time.sleep(1)
        WebDriver().click('byxpath', dataoper.readxml('space', 0, 'search'))
        time.sleep(1)
        WebDriver().click('byid', dataoper.readxml('space', 0, 'add_user'))
        time.sleep(1)

        # 保存
        WebDriver().click('byid', dataoper.readxml('space', 0, 'save'))
        time.sleep(1)
        space_url = WebDriver().currenturl()


        # 点击添加Todo，输入标题、选择成员并保存
        WebDriver().click('bycss', dataoper.readxml('todo', 0, 'todo_add'))
        time.sleep(2)
        WebDriver().input('byid', dataoper.readxml('todo', 0, 'todo_name_input'),
                                   dataoper.readxml('todo', 0, 'todo_name'))
        time.sleep(1)
        WebDriver().select('byid', dataoper.readxml('todo', 0, 'select_member'),
                                   dataoper.readxml('todo', 0, 'member1'))
        WebDriver().select('byid', dataoper.readxml('todo', 0, 'select_member'),
                                   dataoper.readxml('todo', 0, 'member2'))
        time.sleep(1)
        WebDriver().click('byid', dataoper.readxml('todo', 0, 'add_member'))
        time.sleep(2)
        WebDriver().click('byid', dataoper.readxml('todo', 0, 'save'))
        time.sleep(2)

    def test2_member_add_todo(self):
        # 使用其他成员添加Todo，输入标题、选择成员并保存
        Operations().login(dataoper.readxml('todo', 0, 'username'),
                              dataoper.readxml('todo', 0, 'password'))
        WebDriver().geturl(space_url)
        time.sleep(2)
        # 调用添加todo的方法
        WebDriver().click('bycss', dataoper.readxml('todo', 0, 'todo_add'))
        time.sleep(2)
        WebDriver().input('byid', dataoper.readxml('todo', 0, 'todo_name_input'),
                                   dataoper.readxml('todo', 0, 'todo_name2'))
        time.sleep(1)
        WebDriver().select('byid', dataoper.readxml('todo', 0, 'select_member'),
                                   dataoper.readxml('todo', 0, 'member1'))
        WebDriver().select('byid', dataoper.readxml('todo', 0, 'select_member'),
                                   dataoper.readxml('todo', 0, 'member2'))
        time.sleep(1)
        WebDriver().click('byid', dataoper.readxml('todo', 0, 'add_member'))
        time.sleep(2)
        WebDriver().click('byid', dataoper.readxml('todo', 0, 'save'))
        time.sleep(2)

    def test3_process_todo(self):
        # u1完成todo
        Operations().login(dataoper.readxml('login', 0, 'username'),
                              dataoper.readxml('login', 0, 'password'))
        WebDriver().geturl(space_url)
        time.sleep(2)
        WebDriver().click('byxpath', dataoper.readxml('todo', 0, 'todo_link'))
        time.sleep(2)
        WebDriver().click('bycss', dataoper.readxml('todo', 0, 'make_complete'))
        time.sleep(1)
        Operations().logout()
        # u2完成todo
        Operations().login(dataoper.readxml('todo', 0, 'username'),
                              dataoper.readxml('todo', 0, 'password'))
        WebDriver().geturl(space_url)
        time.sleep(2)
        WebDriver().click('byxpath', dataoper.readxml('todo', 0, 'todo_link'))
        time.sleep(2)
        WebDriver().click('bycss', dataoper.readxml('todo', 0, 'make_complete'))
        time.sleep(1)
        WebDriver().click('byxpath', dataoper.readxml('todo', 0, 'shar_todo_link'))
        time.sleep(1)
        WebDriver().click('byxpath', dataoper.readxml('todo', 0, 'complete_link'))
        time.sleep(3)
        check = WebDriver().gettext('bylink', dataoper.readxml('todo', 0, 'todo_check'))
        value = dataoper.readxml('todo', 0, 'value')
        time.sleep(1)
        self.assertEqual(value, check), u"已完成的todo信息不匹配，验证失败"
        time.sleep(1)

    def tearDown(self):
        # 退出
        Operations().logout()


    @classmethod
    def tearDownClass(self):
        # 清空space数据

        try:
            Operations().login(dataoper.readxml('login', 0, 'username'),
                                  dataoper.readxml('login', 0, 'password'))
            WebDriver().geturl(space_url)
            time.sleep(2)
            WebDriver().click('byid', dataoper.readxml('space', 0, 'droplist'))
            time.sleep(1)
            WebDriver().click('bylink', dataoper.readxml('space', 0, 'detail'))
            time.sleep(1)
            WebDriver().click('byid', dataoper.readxml('space', 0, 'delete_link'))
            time.sleep(2)
            WebDriver().click('byxpath', dataoper.readxml('space', 0, 'delete_yes'))
            time.sleep(2)
        except Exception as msg:
            print msg
        else:
            print "Space及todo数据已清除"
        finally:
            WebDriver().close()


if __name__ == "__main__":
    unittest.main()