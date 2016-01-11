#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Python面向对象学习4
# 静态方法：需要通过修饰器"@staticmethod"来进行修饰，静态方法不需要多定义参数


class people:
	country = "china"

	# 静态方法
	@staticmethod
	def getCountry():		
		return people.country

p = people()
print p.getCountry()
print people.getCountry() 