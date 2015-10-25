# coding=utf-8
'''
Created on 2015年10月14日
1.ファイルを添付したディスカッションが作成できること
2.ファイルを添付したコメントをディスカッションに書き込めること
3.ディスカッションが削除できること
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
        # 新建space
        global dataoper, space_url, disc_url, upfile1
        # 读取测试数据并登录
        dataoper = DataReader('QT_Space_create_discussion.xml')
        QT_Operations().login(dataoper.readxml('login', 0, 'username'),
                              dataoper.readxml('login', 0, 'password'))
        time.sleep(2)
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
        # 选择公开方式
        WebDriverHelp().clickitem('byid', dataoper.readxml('space', 0, 'public'))
        # 保存
        WebDriverHelp().clickitem('byid', dataoper.readxml('space', 0, 'save'))
        time.sleep(1)
        space_url = WebDriverHelp().currenturl()

        # 点击添加讨论区
        WebDriverHelp().clickitem('bycss', dataoper.readxml('disc', 0, 'add_disc'))
        time.sleep(1)
        # 输入标题、内容，上传附件并保存
        upfile1 = os.path.abspath('../Attachement/cybozu.gif')

        WebDriverHelp().inputvalue('byid', dataoper.readxml('disc', 0, 'title_input'),
                                   dataoper.readxml('disc', 0, 'disc_title'))
        time.sleep(1)
        WebDriverHelp().inputvalue('byid', dataoper.readxml('disc', 0, 'content_input'),
                                   dataoper.readxml('disc', 0, 'content'))
        time.sleep(1)
        WebDriverHelp().inputvalue('byid', dataoper.readxml('disc', 0, 'disc_upfile'), upfile1)
        time.sleep(3)
        WebDriverHelp().clickitem('byid', dataoper.readxml('disc', 0, 'disc_save'))
        # 获取discussion的URL
        disc_url = WebDriverHelp().currenturl()

        # 提交带附件的回复
        upfile2 = os.path.abspath('../Attachement/test.txt')
        WebDriverHelp().inputvalue('byid', dataoper.readxml('disc', 0, 'comment_input'),
                                   dataoper.readxml('disc', 0, 'comment'))
        time.sleep(2)
        WebDriverHelp().inputvalue('byid', dataoper.readxml('disc', 0, 'comment_upfile'), upfile2)
        time.sleep(3)
        WebDriverHelp().clickitem('byid', dataoper.readxml('disc', 0, 'comment_submit'))
        time.sleep(2)


    def test2_other_confirm(self):
        QT_Operations().login(dataoper.readxml('confirm', 0, 'username'),
                              dataoper.readxml('confirm', 0, 'password'))
        time.sleep(2)
        WebDriverHelp().geturl(disc_url)
        time.sleep(3)
        WebDriverHelp().inputvalue('byid', dataoper.readxml('confirm', 0, 'comment_input'),
                                   dataoper.readxml('confirm', 0, 'comment'))
        time.sleep(2)
        WebDriverHelp().inputvalue('byid', dataoper.readxml('confirm', 0, 'comment_upfile'), upfile1)
        time.sleep(3)
        WebDriverHelp().clickitem('byid', dataoper.readxml('confirm', 0, 'comment_submit'))
        time.sleep(2)

    def test3_delete_discssion(self):
        QT_Operations().login(dataoper.readxml('login', 0, 'username'),
                              dataoper.readxml('login', 0, 'password'))
        time.sleep(2)
        WebDriverHelp().geturl(disc_url)
        time.sleep(2)
        WebDriverHelp().clickitem('bycss', dataoper.readxml('delete', 0, 'droplist'))
        WebDriverHelp().clickitem('byid', dataoper.readxml('delete', 0, 'delete_link'))
        WebDriverHelp().clickitem('byid', dataoper.readxml('delete', 0, 'delete_yes'))
        time.sleep(2)

    def tearDown(self):
        # 退出
        QT_Operations().logout()

    @classmethod
    def tearDownClass(self):
        # 清空space数据
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


if __name__ == "__main__":
    unittest.main()