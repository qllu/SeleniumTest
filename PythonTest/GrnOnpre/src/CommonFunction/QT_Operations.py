#coding=utf-8
'''
Created on 2015年8月12日

QT_Operations 用来存放具体操作功能块，如登录，退出等

@author: QLLU
'''
import time
#import win32api
#import win32con
 
from WebDriverHelp import WebDriverHelp
 
class QT_Operations(object):
    '''
    Grn相关操作
    '''

    def login(self,userName,passwd):
        '''
        从首页直接登录
        @param userName: 用户名
        @param passwd:密码
        @param type1:指示登录方式，1为从主页登录，2，从登录页登录
        '''

        WebDriverHelp().clickitem('byname', '_account')
        time.sleep(3)
        WebDriverHelp().clearvalue('byname','_account')
        WebDriverHelp().inputvalue('byname','_account',userName)
        time.sleep(1)
        WebDriverHelp().clearvalue('byname','_password')
        WebDriverHelp().inputvalue('byname','_password',passwd)
        time.sleep(1)
        WebDriverHelp().clickitem("byname", "login-submit")
        time.sleep(2)


    def logout(self):
        '''
        退出登录
        '''
        WebDriverHelp().refresh()
        WebDriverHelp().clickitem('bycss', 'span')
        WebDriverHelp().clickitem('byid', 'com-header-logout-link')
        