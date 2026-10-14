# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:44:01 2026

@author: Administrator
"""

class account():
    def __init__(self,acno,actyp,bal):
         self.account_number = acno
         self.Type = actyp
         self.balance = bal
         
    def display(self):
      d ={}
      d[self.account_number] = {'Type':self.Type,"Balance":self.balance}
      print(d)
      
    def withdraw(self,amount):
        balance = self.balance - amount
        if amount > self.balance:
             print("Not Enough Balance")
        else: 
            self.balance = balance
    def deposit(self,amount):
         balance = self.balance + amount
         self.balance = balance

         
bn = account(2165454, 'Saviing', 5000)
bn.deposit(10000)
bn.display()
