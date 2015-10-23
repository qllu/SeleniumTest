# coding=utf-8
'''
Created on 2015年10月14日
1.ファイルを添付したディスカッションが作成できること
2.ディスカッションが削除できること
3.ファイルを添付したコメントをディスカッションに書き込めること
@author: QLLU
'''
# 导入需要的公共函数类
import time, unittest, sys, os

sys.path.append("..")
sys.path.append(os.getcwd() + "/src/")
from CommonFunction.DataReader import DataReader
from CommonFunction.QT_Operations import QT_Operations
from CommonFunction.WebDriverHelp import WebDriverHelp

class CreateDiscussion(unittest.TestCase):
    '''
    新增space目录
    '''
    @classmethod
    def setUpClass(self):
        WebDriverHelp("open", "firefox", "local").setup("fcn")  # 打开浏览器，并打开forest

    def test1_create_discussion(self):
        # 调用新建space的方法

        global dataoper, detail_url, current_url
        # 读取测试数据并登录
        dataoper = DataReader('QT_Space_create_discussion.xml')
        QT_Operations().login(dataoper.readxml('login', 0, 'username'),
                              dataoper.readxml('login', 0, 'password'))
        time.sleep(2)
        # 点击进入Garoon
        garoon_url = "https://qatest01.cybozu.cn/g/space/application/discussion/index.csp?spid=7"
        WebDriverHelp().geturl(garoon_url)
        time.sleep(1)

        """
        # 点击进入space
        WebDriverHelp().clickitem('bycss', dataoper.readxml('space', 0, 'space_icon'))
        time.sleep(2)
        # 创建space
        WebDriverHelp().clickitem('bylink', dataoper.readxml('space', 0, 'creat_link'))
        time.sleep(1)
        # 输入title
        WebDriverHelp().inputvalue('byid', dataoper.readxml('space', 0, 'space_title'),
                                   dataoper.readxml('space', 0, 'title'))
        time.sleep(1)
        # 搜索添加用户
        WebDriverHelp().inputvalue('byname', dataoper.readxml('space', 0, 'e_keyword'),
                                   dataoper.readxml('space', 0, 'keyword'))
        time.sleep(1)
        WebDriverHelp().clickitem('byxpath', dataoper.readxml('space', 0, 'search'))
        time.sleep(1)
        WebDriverHelp().clickitem('byid', dataoper.readxml('space', 0, 'add_user'))
        time.sleep(1)
        # 选择公开方式
        WebDriverHelp().clickitem('byid', dataoper.readxml('space', 0, 'public'))
        # 保存
        WebDriverHelp().clickitem('byid', dataoper.readxml('space', 0, 'save'))
        time.sleep(1)
        current_url = WebDriverHelp().currenturl()
        """
        # 点击添加讨论区
        WebDriverHelp().clickitem('bycss', dataoper.readxml('space', 0, 'add_disc'))
        time.sleep(1)
        # 输入标题、内容，上传附件
        WebDriverHelp().inputvalue('byid', dataoper.readxml('space', 0, 'disc_title'),
                                   dataoper.readxml('space', 0, 'title'))
        time.sleep(1)
        WebDriverHelp().inputvalue('byid', dataoper.readxml('space', 0, 'disc_content'),
                                   dataoper.readxml('space', 0, 'content'))
        WebDriverHelp().inputvalue('byid', dataoper.readxml('space', 0, 'file_upload'),
                                   dataoper.readxml('space', 0, 'file'))
        time.sleep(2)
        # 保存
        WebDriverHelp().clickitem('byid', dataoper.readxml('space', 0, 'disc_save'))



    def test2_member_confirm(self):
        pass

    def test3_other_confirm(self):
        pass

    def tearDown(self):
        # 退出
        QT_Operations().logout()

    @classmethod
    def tearDownClass(self):
        WebDriverHelp().teardown()


if __name__ == "__main__":
    unittest.main()