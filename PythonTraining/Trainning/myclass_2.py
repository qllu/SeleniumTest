#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Python面向对象学习2
# http://www.cnblogs.com/dolphin0520/archive/2013/03/29/2986924.html


class people:
	country = "china"

	@classmethod
	def getCountry(self):		
		return self.country

	@classmethod
	def setCountry(self, country):
		self.country = country

p = people()
print p.getCountry()  # 可以用过实例对象引用
print people.getCountry()  # 可以用类对象引用

p.setCountry("japan")
print p.getCountry()
print people.getCountry()
