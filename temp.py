# -*- coding: utf-8 -*-
"""
1)	marks = {"Amit": 78, "Bela": 92, "Chirag": 65, "Divya": 88}
List out the students who have scored more than 80 marks in descending order

"""
marks = {"Amit": 78, "Bela": 92, "Chirag": 65, "Divya": 88}
    
ans = sorted((filter(lambda x : x[1] > 80 ,marks.items())))
print(ans)
