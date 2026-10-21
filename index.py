# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 13:46:30 2026

@author: Administ"""


class employee():
    
    def __init__(self,no,name,des,sal):
           self.no=no
           self.name=name
           self.des=des
           self.sal=sal
    def display(self):
        print('Employee No is  : ' ,self.no)
        print('Employee Name  is : ' ,self.name)
        print('Designation  : ' ,self.des)
        print('Salary   : ' ,self.sal)

d1 = employee(1,'Ashish','AI/ML Engineer',700000)
d1.display()
 

z = "hello world"
y = "welcome!"

a = len("hello world") + len("welcome!")
print(a)