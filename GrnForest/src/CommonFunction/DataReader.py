#coding=utf-8
'''
Created on 2015年8月12日

DataOperations用来存放所有数据操作，用来读取xml中的测试数据

@author: QLLU
'''
# import MySQLdb
from xml.dom import minidom
global DOC,CONN
 
class DataReader(object):
    '''
    数据读取相关操作
    '''
 
    def __init__(self,filename):
        '''
        初始化xml文档
        '''
        global DOC, CONN
        DOC = minidom.parse('../TestData/' + filename) #使用相对路径
        # DOC = minidom.parse('E:\\Workspace\\Python-Workspace\\PythonTest\\src\\\TestData\\' + filename)

    def readxml(self,ftagname,num,stagname):
        '''
        从指定的文件中中读取指定节点的值
        @param ftagname:起始节点的名称，如：project
        @param num:取与起始节点相同的第num个节点
        @param stagname: 起始节点下的二级节点
        @return: 返回二级节点的值
        '''          
        root = DOC.documentElement
        message=root.getElementsByTagName(ftagname)[num]
        return message.getElementsByTagName(stagname)[0].childNodes[0].nodeValue

   
    def readxml_attribute(self,ftagname,num,stagname,attributeName):
        '''
        从all_case.xml文件中读取节点的属性值
        @param ftagname:起始节点的名称，如：project
        @param num:取与起始节点相同的第num个节点
        @param stagname: 起始节点下的二级节点
        @param attributeName: 二级节点的属性名
        @return:返回二级节点指定的属性值       
        '''
      
        root = DOC.documentElement
        message=root.getElementsByTagName(ftagname)[num]
        return message.getElementsByTagName(stagname)[0].getAttribute(attributeName)