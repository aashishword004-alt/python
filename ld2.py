# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 11:48:40 2026

@author: ex409_28
"""

std = {1 : ['Ashish', 'Ahmedabad',46,54,80],
       2 :  ['Rohan', 'Surat',40,55,91],
       3 : ['Jay', 'Rajkot',87,40,87],
       4 : ['Aman', 'Vadodara',58,89,87],
       5 : ['Parth', 'Mahesana',54,57,87]}

city = list(map(lambda x : x[1][1] , std.items()))
v = list(map(lambda x : x[1] , std.values()))
k = list(map(lambda x : x , std.keys()))

print(city)
print(k)
print(v)