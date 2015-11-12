#coding=utf-8
'''
Created on 2015年8月12日

QT_Operations 用来存放具体操作功能块，如登录，退出等

@author: QLLU
'''
import time
#import win32api
#import win32con
 
from WebDriver import WebDriver

class Operations(object):
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

        WebDriver().click("byname", "username")
        time.sleep(3)
        WebDriver().clear('byname','username')
        WebDriver().input('byname','username',userName)
        time.sleep(1)
        WebDriver().clear('byname','password')
        WebDriver().input('byname','password',passwd)
        time.sleep(1)
        WebDriver().click("byclass", "login-button")
        time.sleep(2)
        # WebDriverFunction().geturl("https://qatest01.cybozu.cn")
        # time.sleep(2)

    def logout(self):
        '''
        退出登录
        '''
        WebDriver().geturl("https://qatest01.cybozu.cn/logout")

        