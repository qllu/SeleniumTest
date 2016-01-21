# -*- coding: utf-8 -*-
import os
import os.path
import time
rootdir = '../src/'
filelists = []

# 遍历文件
def getFile(rootdir):
    global filelists
    for parent,dirnames,filenames in os.walk(rootdir):
        for dirname in dirnames:
            getFile(os.path.join(parent,dirname)) # 嵌套
        for filename in filenames:
            #print 'filename is:'+ filename
            filelists.append(os.path.join(parent,filename))

# 统计一个文件的行数
def countLine(fname):
    count = 0
    for file_line in open(fname).xreadlines():
        if file_line != '' and file_line != '': # 过滤掉空行
            count += 1
    print fname + '.....' , count
    return count

if __name__ == '__main__' :
    startTime = time.clock()
    getFile(rootdir)
    totalline = 0
    for filelist in filelists:
        totalline = totalline + countLine(filelist)
    print 'totalline:',totalline
    print 'done:%0.2f second' % (time.clock() - startTime)