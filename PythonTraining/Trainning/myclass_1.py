#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Python面向对象学习1


class Person:
    def __init__(self, name, salary):
        self.NAME = name
        self.SALARY = salary

    def sayName(self):
        print "Hello %s, Welcom!" % self.NAME

    def ask(self):
        print "Hey %s, how much money do you make?" % self.NAME
        if self.SALARY:
            print "%s, very good!" % self.SALARY

p = Person("Jerry", "20000")
p.sayName()
p.ask()
