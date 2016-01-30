#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Python面向对象学习3


class people:
	country = "china"

	def getCountry(self):		
		return self.country


p = people()
print p.getCountry()
# print people.getCountry()  # 错误，不能通过类对象引用实例方法
