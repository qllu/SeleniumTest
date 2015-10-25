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
from CommonFunction.QT_Operations import QT_Operations
from CommonFunction.WebDriverHelp import WebDriverHelp


class AddShareTodo(unittest.TestCase):
    '''
    新增space目录
    '''
    @classmethod
    def setUpClass(self):
        WebDriverHelp("open", "firefox", "local").setup("fcn")  # 打开浏览器，并打开forest

    def test1_add_share_todo(self):
        # 新建space
        global dataoper, space_url
        # 读取测试数据并登录
        dataoper = DataReader('QT_Space_add_share_todo.xml')
        QT_Operations().login(dataoper.readxml('login', 0, 'username'),
                              dataoper.readxml('login', 0, 'password'))
        time.sleep(2)
        space_url = 'https://qatest01.cybozu.cn/g/space/top.csp?spid=117#tid=117'
        WebDriverHelp().geturl(space_url)
        time.sleep(2)

        """
        # 点击进入Garoon
        garoon_url = "https://qatest01.cybozu.cn/g/"
        WebDriverHelp().geturl(garoon_url)
        time.sleep(1)
        # 点击进入space
        WebDriverHelp().clickitem('bycss', dataoper.readxml('space', 0, 'space_icon'))
        time.sleep(2)
        # 创建space
        WebDriverHelp().clickitem('bylink', dataoper.readxml('space', 0, 'creat_link'))
        time.sleep(1)
        # 输入title
        WebDriverHelp().inputvalue('byid', dataoper.readxml('space', 0, 'space_title'),
                                   dataoper.readxml('space', 0, 'title'))
        # 搜索添加用户
        WebDriverHelp().inputvalue('byname', dataoper.readxml('space', 0, 'e_keyword'),
                                   dataoper.readxml('space', 0, 'keyword'))
        time.sleep(1)
        WebDriverHelp().clickitem('byxpath', dataoper.readxml('space', 0, 'search'))
        time.sleep(1)
        WebDriverHelp().clickitem('byid', dataoper.readxml('space', 0, 'add_user'))
        time.sleep(1)

        # 保存
        WebDriverHelp().clickitem('byid', dataoper.readxml('space', 0, 'save'))
        time.sleep(1)
        space_url = WebDriverHelp().currenturl()
        """

        # 点击添加Todo，输入标题、选择成员并保存
        WebDriverHelp().clickitem('bycss', dataoper.readxml('todo', 0, 'todo_add'))
        time.sleep(2)
        WebDriverHelp().inputvalue('byid', dataoper.readxml('todo', 0, 'todo_name_input'),
                                   dataoper.readxml('todo', 0, 'todo_name'))
        time.sleep(1)
        WebDriverHelp().selectvalue('byid', dataoper.readxml('todo', 0, 'select_member'),
                                   dataoper.readxml('todo', 0, 'member1'))
        WebDriverHelp().selectvalue('byid', dataoper.readxml('todo', 0, 'select_member'),
                                   dataoper.readxml('todo', 0, 'member2'))
        time.sleep(1)
        WebDriverHelp().clickitem('byid', dataoper.readxml('todo', 0, 'add_member'))
        time.sleep(2)
        WebDriverHelp().clickitem('byid', dataoper.readxml('todo', 0, 'save'))
        time.sleep(2)

    def test2_member_add_todo(self):
        # 使用其他成员添加Todo，输入标题、选择成员并保存
        QT_Operations().login(dataoper.readxml('todo', 0, 'username'),
                              dataoper.readxml('todo', 0, 'password'))
        WebDriverHelp().geturl(space_url)
        time.sleep(2)
        # 调用添加todo的方法
        WebDriverHelp().clickitem('bycss', dataoper.readxml('todo', 0, 'todo_add'))
        time.sleep(2)
        WebDriverHelp().inputvalue('byid', dataoper.readxml('todo', 0, 'todo_name_input'),
                                   dataoper.readxml('todo', 0, 'todo_name2'))
        time.sleep(1)
        WebDriverHelp().selectvalue('byid', dataoper.readxml('todo', 0, 'select_member'),
                                   dataoper.readxml('todo', 0, 'member1'))
        WebDriverHelp().selectvalue('byid', dataoper.readxml('todo', 0, 'select_member'),
                                   dataoper.readxml('todo', 0, 'member2'))
        time.sleep(1)
        WebDriverHelp().clickitem('byid', dataoper.readxml('todo', 0, 'add_member'))
        time.sleep(2)
        WebDriverHelp().clickitem('byid', dataoper.readxml('todo', 0, 'save'))
        time.sleep(2)

    def test3_process_todo(self):
        """
        QT_Operations().login(dataoper.readxml('login', 0, 'username'),
                              dataoper.readxml('login', 0, 'password'))
        WebDriverHelp().geturl(space_url)
        """
        pass

    def tearDown(self):
        # 退出
        QT_Operations().logout()



    @classmethod
    def tearDownClass(self):
        # 清空space数据
        """
        try:
            QT_Operations().login(dataoper.readxml('login', 0, 'username'),
                                  dataoper.readxml('login', 0, 'password'))
            WebDriverHelp().geturl(space_url)
            time.sleep(2)
            WebDriverHelp().clickitem('byid', dataoper.readxml('space', 0, 'droplist'))
            time.sleep(1)
            WebDriverHelp().clickitem('bylink', dataoper.readxml('space', 0, 'detail'))
            time.sleep(1)
            WebDriverHelp().clickitem('byid', dataoper.readxml('space', 0, 'delete_link'))
            time.sleep(2)
            WebDriverHelp().clickitem('byxpath', dataoper.readxml('space', 0, 'delete_yes'))
            time.sleep(2)
        except Exception as msg:
            print msg
        else:
            print "Discussion数据已清除"
        finally:
            WebDriverHelp().teardown()
        """
        pass

if __name__ == "__main__":
    unittest.main()