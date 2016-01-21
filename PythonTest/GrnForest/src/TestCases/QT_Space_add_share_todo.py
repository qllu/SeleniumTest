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
        global domain, driver
        domain = "qatest01"
        driver = WebDriver("open", "firefox", "local")
        driver.open(domain, "slash")  # 打开浏览器，并打开forest

    def test1_add_share_todo(self):
        # 新建space
        global dataoper, space_url
        # 读取测试数据并登录
        dataoper = DataReader('QT_Space_add_share_todo.xml')
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
        # 搜索添加用户
        driver.input('byname', dataoper.readxml('space', 0, 'e_keyword'),
                                   dataoper.readxml('space', 0, 'keyword'))
        driver.wait(2)
        driver.click('byxpath', dataoper.readxml('space', 0, 'search'))
        driver.wait(2)
        driver.click('byid', dataoper.readxml('space', 0, 'add_user'))
        driver.wait(2)

        # 保存
        driver.click('byid', dataoper.readxml('space', 0, 'save'))
        driver.wait(2)
        space_url = driver.currenturl()


        # 点击添加Todo，输入标题、选择成员并保存
        driver.click('bycss', dataoper.readxml('todo', 0, 'todo_add'))
        driver.wait(3)
        driver.input('byid', dataoper.readxml('todo', 0, 'todo_name_input'),
                                   dataoper.readxml('todo', 0, 'todo_name'))
        driver.wait(2)
        driver.select('byid', dataoper.readxml('todo', 0, 'select_member'),
                                   dataoper.readxml('todo', 0, 'member1'))
        driver.select('byid', dataoper.readxml('todo', 0, 'select_member'),
                                   dataoper.readxml('todo', 0, 'member2'))
        driver.wait(2)
        driver.click('byid', dataoper.readxml('todo', 0, 'add_member'))
        driver.wait(3)
        driver.click('byid', dataoper.readxml('todo', 0, 'save'))
        driver.wait(3)

    def test2_member_add_todo(self):
        # 使用其他成员添加Todo，输入标题、选择成员并保存
        Operations().login(dataoper.readxml('todo', 0, 'username'),
                              dataoper.readxml('todo', 0, 'password'))
        driver.geturl(space_url)
        driver.wait(3)
        # 调用添加todo的方法
        driver.click('bycss', dataoper.readxml('todo', 0, 'todo_add'))
        driver.wait(3)
        driver.input('byid', dataoper.readxml('todo', 0, 'todo_name_input'),
                                   dataoper.readxml('todo', 0, 'todo_name2'))
        driver.wait(2)
        driver.select('byid', dataoper.readxml('todo', 0, 'select_member'),
                                   dataoper.readxml('todo', 0, 'member1'))
        driver.select('byid', dataoper.readxml('todo', 0, 'select_member'),
                                   dataoper.readxml('todo', 0, 'member2'))
        driver.wait(2)
        driver.click('byid', dataoper.readxml('todo', 0, 'add_member'))
        driver.wait(3)
        driver.click('byid', dataoper.readxml('todo', 0, 'save'))
        driver.wait(3)

    def test3_process_todo(self):
        # u1完成todo
        Operations().login(dataoper.readxml('login', 0, 'username'),
                              dataoper.readxml('login', 0, 'password'))
        driver.geturl(space_url)
        driver.wait(3)
        driver.click('byxpath', dataoper.readxml('todo', 0, 'todo_link'))
        driver.wait(3)
        driver.click('bycss', dataoper.readxml('todo', 0, 'make_complete'))
        driver.wait(2)
        Operations().logout()
        # u2完成todo
        Operations().login(dataoper.readxml('todo', 0, 'username'),
                              dataoper.readxml('todo', 0, 'password'))
        driver.geturl(space_url)
        driver.wait(3)
        driver.click('byxpath', dataoper.readxml('todo', 0, 'todo_link'))
        driver.wait(3)
        driver.click('bycss', dataoper.readxml('todo', 0, 'make_complete'))
        driver.wait(2)
        driver.click('byxpath', dataoper.readxml('todo', 0, 'shar_todo_link'))
        driver.wait(2)
        driver.click('byxpath', dataoper.readxml('todo', 0, 'complete_link'))
        driver.wait(5)
        check = driver.gettext('bylink', dataoper.readxml('todo', 0, 'todo_check'))
        value = dataoper.readxml('todo', 0, 'value')
        driver.wait(2)
        self.assertEqual(value, check), u"已完成的todo信息不匹配，验证失败"
        driver.wait(2)

    def tearDown(self):
        # 退出
        Operations().logout()


    @classmethod
    def tearDownClass(self):
        # 清空space数据

        try:
            Operations().login(dataoper.readxml('login', 0, 'username'),
                                  dataoper.readxml('login', 0, 'password'))
            driver.geturl(space_url)
            driver.wait(3)
            driver.click('byid', dataoper.readxml('space', 0, 'droplist'))
            driver.wait(2)
            driver.click('bylink', dataoper.readxml('space', 0, 'detail'))
            driver.wait(2)
            driver.click('byid', dataoper.readxml('space', 0, 'delete_link'))
            driver.wait(3)
            driver.click('byxpath', dataoper.readxml('space', 0, 'delete_yes'))
            driver.wait(3)
        except Exception as msg:
            print msg, "Data has not been removed."
        finally:
            driver.close()


if __name__ == "__main__":
    unittest.main()