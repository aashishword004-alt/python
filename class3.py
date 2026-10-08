# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 11:47:56 2026
        }
Here students are getting marks of 3 subjects in 2 attempts of 
test in a form of tuple
a)	Find out the maximum marks obtained in all the three subjects
b)	Find out the average marks of the all the students

@author: ex409_28
"""

stud = {
        1: {"name":'Amit', "age":23,"marks": [(10,15,12), (11,12,13)]},               
        2: {"name":'Bhumi',"age":22,"marks": [(13,15,11), (10,10,13)]},             
        3: {"name":'Bharat',"age":23,"marks": [(12,12,14), (13,14,15)]},
        }
mark = []


mark=list(map(lambda x:x[1]["marks"],stud.items()))
print(mark)   
im=[x for t in mark for x in t]
print(im)
first = sorted(im,key=lambda x : x[0],reverse=True)
print(first[0][0])
print(first[0][0])
sec = sorted(im,key=lambda x : x[1],reverse=True)
print(first[0][1])