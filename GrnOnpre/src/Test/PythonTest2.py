#!/usr/bin/env python
#encoding: utf-8

import unittest

class mytest(unittest.TestCase):

    #具体的测试用例，一定要以test开头
    def test1(self):
        global  var
        var = 1
        print "var1:", var

    def test2(self):
        print "var2:", var


if __name__ =='__main__':
    unittest.main()
