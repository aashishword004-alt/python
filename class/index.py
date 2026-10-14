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
        a = self.sal*12
        self.sal = a
        return {
            'name' : self.name,
            'designation' : self.des,
            'salary' : self.sal
        }
        
 
    
e = int(input("Enter the How Many Record Enter by : "))
d = {}  

for i in range(e):
    no = int(input("Enter the Number : "))
    name = str(input("Enter the Name : "))
    dis = str(input("Enter the designation : "))
    sal = int(input("Enter the Salary  : "))
    emp = employee(no, name, dis, sal)
    d[no] = emp.display() 

print(d)   
