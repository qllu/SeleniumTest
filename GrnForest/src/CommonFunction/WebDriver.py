#coding=utf-8
'''
Created on 2015年8月12日

WebDriverHelp用来存放所有页面操作用到公用方法

@author: QLLU
'''
import logging
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
global G_WEBDRIVER, G_BROWSERTYTPE,driver
 
class WebDriver(object):
    '''
    本类主要完成页面的基本操作，如打开指定的URL，对页面上在元素进行操作等
    '''
 
    def  __init__(self,btype="close",atype="firefox",ctype="local"):
        """
        根据用户定制，打开对应的浏览器
        @param bType: 开关参数，如果为close则关闭浏览器
        @param aType:打开浏览器的类型，如chrome,firefox,ie等要测试的浏览器类型
        @param cType:打开本地或是远程浏览器： local,本地；notlocal：远程
        """
        global driver
        if(  btype == "open" ):
            if(atype == "chrome"):
                if(ctype == "local"):
                    driver = webdriver.Chrome()

                elif(ctype == "notlocal"):
                    print "打开远程的chrome"
                    driver = webdriver.Remote(command_executor='http://10.60.1.186:4444/wd/hub',
                                              desired_capabilities=webdriver.DesiredCapabilities.CHROME)
                    # driver.maximize_window()

            elif(atype == "ie"):
                if(ctype == "local"):
                    driver = webdriver.Ie()

                elif(ctype == "notlocal"):
                    print "打开远程的IE"
                    driver = webdriver.Remote(command_executor='http://10.60.1.186:4444/wd/hub',
                                              desired_capabilities=webdriver.DesiredCapabilities.INTERNETEXPLORER)
                    # driver.maximize_window()

            elif(  atype == "firefox" ):
                if(ctype == "local"):
                    driver = webdriver.Firefox()
                    driver.maximize_window()

                elif(ctype == "notlocal"):
                    print "打开远程的Firefox"
                    driver = webdriver.Remote(command_executor='http://10.60.1.186:4444/wd/hub',
                                              desired_capabilities=webdriver.DesiredCapabilities.FIREFOX)
                    # driver.maximize_window()
                                  
        self.driver = driver
 
    def open(self, url, type):
        """
        定制测试URL，可分为单机版、云版
        @param logintype: 指定测试的URL： onpre:单机版测试地址，cloud:云版测试地址
        """
        try:
            garoon = "/g/"
            sys_common = "/g/system/common_list.csp?"
            sys_app = "/g/system/application_list.csp?"
            person_set = "/g/personal/common_list.csp?"
            jljin = "http://jljin.cybozu-dev.com"
            qatest01 = "https://qatest01.cybozu.cn"

            if(url == "jljin"):
                self.driver.get(jljin)

            elif(url == "qatest01"):
                if type == "slash":
                    self.driver.get(qatest01)
                elif type == "g":
                    garoon_url = qatest01 + garoon
                    self.driver.get(garoon_url)
                elif type == "sys_common":
                    sys_common_url = qatest01 + sys_common
                    self.driver.get(sys_common_url)
                elif type == "sys_app":
                    sys_app_url = qatest01 + sys_app
                    self.driver.get(sys_app_url)
                elif type == "person_set":
                    person_set_url = qatest01 + person_set
                    self.driver.get(person_set_url)
            else:
                print '路径错误！'
            self.driver.implicitly_wait(1)
        except NoSuchElementException:
            print '您选择的测试地址出错！！'

    def testurl(self, url):
        if(url == "jljin"):
            return "http://jljin.cybozu-dev.com"
        elif(url == "qatest01"):
            return "http://qatest01.cybozu.cn"
        elif(url == "qllu"):
            return "http://qllu.cybozu-dev.com"
        else:
            print "url错误"

    def geturl(self,url):
        '''
        打开指定的网址
        @param url: 要打开的网址
        '''
        self.driver.get(url)

    def currenturl(self):
        return self.driver.current_url

    def max_window(self):
        self.driver.maximize_window()
              
    def  close(self):
        '''
        关闭浏览器
        '''       
        self.driver.close()


    def refresh(self):
        '''
        页面刷新
        '''
        self.driver.refresh()

    def is_element_present(self, findby, elmethod):
        # 判断页面元素是否存在
        try:
            if(findby == 'byid'):
                self.driver.find_element_by_id(elmethod)
            elif(findby == 'byname'):
                self.driver.find_element_by_name(elmethod)
            elif(findby == 'byxpath'):
                self.driver.find_element_by_xpath(elmethod)
            elif(findby == 'bylink'):
                self.driver.find_element_by_link_text(elmethod)
            elif(findby == 'byclass'):
                self.driver.find_element_by_class_name(elmethod)
            elif(findby == 'bycss'):
                self.driver.find_element_by_css_selector(elmethod)
        except NoSuchElementException: return False
        return True

    def screenshot(self, file_path):
        self.driver.get_screenshot_as_file(file_path)

    def drag_and_drop(self, css_element, css_target):
        # driver = self.driver
        element = self.driver.find_element_by_css_selector(css_element)
        target = self.driver.find_element_by_css_selector(css_target)
        action = ActionChains(self.driver).drag_and_drop(element, target)
        time.sleep(3)
        action.perform()


    def click_and_move(self, elemet_css, target_css):
        # driver = self.driver
        element = self.driver.find_element_by_css_selector(elemet_css)
        target = self.driver.find_element_by_css_selector(target_css)
        action = ActionChains(self.driver).click_and_hold(element).move_to_element(target)
        time.sleep(3)
        action.click().perform()

    def switch_to_frame(self,elmethod):

        #切换到新页面
        xf = self.driver.find_element_by_css_selector(elmethod)
        self.driver._switch_to.frame(xf)

    def switch_to_frame_out(self):
        self.driver._switch_to.default_content()

    def open_new_window(self, elmethod):
        '''
        Open the new window and switch the handle to the newly opened window.
        Usage:
        driver.open_new_window()
        '''
        driver = self.driver
        original_windows = driver.current_window_handle
        driver.find_element_by_css_selector(elmethod).click()
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                driver._switch_to.window(handle)

    def findby(self,findby,elmethod):
        '''
        通过定制定位方法，在对应的项目上执行单击操作
        @param findby: 定位方法，如：byid,byname,byclassname,byxpath等
        @param elmethod: 要定位元素的属性值 ，如：id,name,class name,xpath，text等
        '''
        if(findby == 'byid'):
            return self.driver.find_element_by_id(elmethod)
        elif(findby == 'byname'):
            return self.driver.find_element_by_name(elmethod)
        elif(findby == 'byxpath'):
            return self.driver.find_element_by_xpath(elmethod)
        elif(findby == 'bylink'):
            return self.driver.find_element_by_link_text(elmethod)
        elif(findby == 'byclass'):
            return self.driver.find_element_by_class_name(elmethod)
        elif(findby == 'bycss'):
            return self.driver.find_element_by_css_selector(elmethod)

    def click(self,findby,elmethod):
        '''
        通过定制定位方法，在对应的项目上执行单击操作
        @param findby: 定位方法，如：byid,byname,byclassname,byxpath等
        @param elmethod: 要定位元素的属性值 ，如：id,name,class name,xpath，text等
        '''
        if(findby == 'byid'):
            self.driver.find_element_by_id(elmethod).click()
        elif(findby == 'byname'):
            self.driver.find_element_by_name(elmethod).click()
        elif(findby == 'byxpath'):
            self.driver.find_element_by_xpath(elmethod).click()
        elif(findby == 'bylink'):
            self.driver.find_element_by_link_text(elmethod).click()
        elif(findby == 'byclass'):
            self.driver.find_element_by_class_name(elmethod).click()
        elif(findby == 'bycss'):
            self.driver.find_element_by_css_selector(elmethod).click()         
            
    def clear(self,findby,elmethod):
        '''
        通过定制定位方法，在输入框中输入值
        @param findby: 定位方法，如：byid,byname,byclassname,byxpath等
        @param elmethod: 要定位元素的属性值 ，如：id,name,class name,xpath等
        '''
        if(findby == 'byid'):
            self.driver.find_element_by_id(elmethod).clear()
        elif(findby == 'byname'):
            self.driver. find_element_by_name(elmethod).clear()
        elif(findby =='byclass'):
            self.driver.find_element_by_class_name(elmethod).clear()
        elif(findby == 'byxpath'):
            self.driver.find_element_by_xpath(elmethod).clear()          
      
    def input(self,findby,elmethod,value):
        '''
        通过定制定位方法，在输入框中输入值
        @param findby: 定位方法，如：byid,byname,byclassname,byxpath等
        @param elmethod: 要定位元素的属性值 ，如：id,name,class name,xpath等
        @param value: 要给文本框输入的值
        '''
        if(findby == 'byid'):
            self.driver.find_element_by_id(elmethod).send_keys(value)
        elif(findby == 'byname'):
            self.driver.find_element_by_name(elmethod).send_keys(value)
        elif(findby =='byclass'):
            self.driver.find_element_by_class_name(elmethod).send_keys(value)
        elif(findby == 'byxpath'):
            self.driver.find_element_by_xpath(elmethod).send_keys(value)

    def select(self,findby,select,selectvalue):
        '''
        通过定制定位方法和要选择项的文本，选择指定的项目
        @param findby:定位方法，如：byid,byname,byclassname等
        @param select: 要执行选择操作的下拉框句柄
        @param selectvalue: 下拉框中要选择项的文本     
        '''      
        if(findby == 'byid'):
            select = Select(self.driver.find_element_by_id(select))
        elif(findby =='byname'):
            select = Select(self.driver.find_element_by_name(select))
        elif(findby =='byclass'):
            select = Select(self.driver.find_element_by_classname(select))                 
        select.select_by_visible_text(selectvalue)

    def is_selected(self,findby,elmethod):
        if(findby == 'byid'):
            return self.driver.find_element_by_id(elmethod).is_selected()
        elif(findby == 'byname'):
            return self.driver.find_element_by_name(elmethod).is_selected()
        elif(findby == 'byxpath'):
            return self.driver.find_element_by_xpath(elmethod).is_selected()
        elif(findby=='byclass'):
            return self.driver.find_element_by_class_name(elmethod).is_selected()
        elif(findby=='bycss'):
            return self.driver.find_element_by_css_selector(elmethod).is_selected()
        elif(findby== 'bylink'):
            return self.driver.find_element_by_link_text(elmethod).is_selected()

    def gettext(self,findby,elmethod):
        '''
        通过定制定位方法，获取指定元素的文本
        @param findby: 定位方法，如：byid,byname,byxpath等
        @param elmethod: 要定位元素的属性值 ，如：id,name,xpath等
        @return: 返回获取到的元素文本
        '''
        if(findby == 'byid'):
            return self.driver.find_element_by_id(elmethod).text
        elif(findby == 'byname'):
            return self.driver.find_element_by_name(elmethod).text
        elif(findby == 'byxpath'):
            return self.driver.find_element_by_xpath(elmethod).text
        elif(findby=='byclass'):
            return self.driver.find_element_by_class_name(elmethod).text
        elif(findby=='bycss'):
            return self.driver.find_element_by_css_selector(elmethod).text
        elif(findby== 'bylink'):
            return self.driver.find_element_by_link_text(elmethod).text

    def getlog(self, filelog):
        logging.basicConfig(
            filename = filelog,
            level = logging.INFO,
            format = '[%(asctime)s %(levelname)s] %(message)s',
            datefmt = '%Y%m%d %H:%M:%S')
        logging.info('debug log')
