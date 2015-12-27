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
from CommonFunction.Operations import Operations
from CommonFunction.WebDriver import WebDriver

class CreateDiscussion(unittest.TestCase):
    '''
    新增space目录
    '''
    @classmethod
    def setUpClass(self):
        global domain, driver
        domain = "qatest01"
        driver = WebDriver("open", "firefox", "local")
        driver.open(domain, "slash")  # 打开浏览器，并打开forest

    def test1_create_discussion(self):
        # 新建space
        global dataoper, space_url, disc_url, upfile1
        # 读取测试数据并登录
        dataoper = DataReader('QT_Space_create_discussion.xml')
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
        driver.click('byclass', dataoper.readxml('space', 0, 'creat_link'))
        time.sleep(1)
        # 输入title
        driver.input('byid', dataoper.readxml('space', 0, 'space_title'),
                                   dataoper.readxml('space', 0, 'title'))
        # 选择公开方式
        driver.click('byid', dataoper.readxml('space', 0, 'public'))
        # 保存
        driver.click('byid', dataoper.readxml('space', 0, 'save'))
        time.sleep(1)
        space_url = driver.currenturl()

        # 点击添加讨论区
        driver.click('bycss', dataoper.readxml('disc', 0, 'add_disc'))
        time.sleep(1)
        # 输入标题、内容，上传附件并保存
        upfile1 = os.path.abspath('../Attachement/cybozu.gif')

        driver.input('byid', dataoper.readxml('disc', 0, 'title_input'),
                                   dataoper.readxml('disc', 0, 'disc_title'))
        time.sleep(1)
        driver.input('byid', dataoper.readxml('disc', 0, 'content_input'),
                                   dataoper.readxml('disc', 0, 'content'))
        time.sleep(1)
        driver.input('byid', dataoper.readxml('disc', 0, 'disc_upfile'), upfile1)
        time.sleep(3)
        driver.click('byid', dataoper.readxml('disc', 0, 'disc_save'))
        # 获取discussion的URL
        disc_url = driver.currenturl()

    def test2_add_comment(self):
        # 提交带附件的回复
        dataoper = DataReader('QT_Space_create_discussion.xml')
        Operations().login(dataoper.readxml('login', 0, 'username'),
                              dataoper.readxml('login', 0, 'password'))
        driver.geturl(disc_url)
        time.sleep(2)
        upfile2 = os.path.abspath('../Attachement/test.txt')
        driver.input('byid', dataoper.readxml('disc', 0, 'comment_input'),
                                   dataoper.readxml('disc', 0, 'comment'))
        time.sleep(2)
        driver.input('byid', dataoper.readxml('disc', 0, 'comment_upfile'), upfile2)
        time.sleep(3)
        driver.click('byid', dataoper.readxml('disc', 0, 'comment_submit'))
        time.sleep(2)


    def test3_other_user_confirm(self):
        Operations().login(dataoper.readxml('confirm', 0, 'username'),
                              dataoper.readxml('confirm', 0, 'password'))
        time.sleep(2)
        driver.geturl(disc_url)
        time.sleep(3)
        driver.input('byid', dataoper.readxml('confirm', 0, 'comment_input'),
                                   dataoper.readxml('confirm', 0, 'comment'))
        time.sleep(2)
        driver.input('byid', dataoper.readxml('confirm', 0, 'comment_upfile'), upfile1)
        time.sleep(3)
        driver.click('byid', dataoper.readxml('confirm', 0, 'comment_submit'))
        time.sleep(2)

    def test4_delete_discssion(self):
        Operations().login(dataoper.readxml('login', 0, 'username'),
                              dataoper.readxml('login', 0, 'password'))
        time.sleep(2)
        driver.geturl(disc_url)
        time.sleep(2)
        driver.click('bycss', dataoper.readxml('delete', 0, 'droplist'))
        driver.click('byid', dataoper.readxml('delete', 0, 'delete_link'))
        driver.click('byid', dataoper.readxml('delete', 0, 'delete_yes'))
        time.sleep(2)

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
            time.sleep(2)
            driver.click('byid', dataoper.readxml('space', 0, 'droplist'))
            time.sleep(1)
            driver.click('bylink', dataoper.readxml('space', 0, 'detail'))
            time.sleep(1)
            driver.click('byid', dataoper.readxml('space', 0, 'delete_link'))
            time.sleep(2)
            driver.click('byxpath', dataoper.readxml('space', 0, 'delete_yes'))
            time.sleep(2)
        except Exception as msg:
            print msg, "Data has not been removed."
        finally:
            driver.close()


if __name__ == "__main__":
    unittest.main()