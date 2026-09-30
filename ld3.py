# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:00:42 2026

@author: ex409_28
"""


d = { 101:{'roll' : 1 ,'name' : 'Ashish','City' : 'Ahmedabad'},
     102:{'roll' : 2 ,'name' : 'Rohan','City' : 'Rajkot'},
     103:{'roll' : 3 ,'name' : 'Jay','City' : 'Vadodara'},
     104:{'roll' : 4 ,'name' : 'Manav','City' : 'Mahesana'},
     105 :{'roll' : 5 ,'name' : 'Jaydeep','City' : 'Amreli'}}

city = list(map(lambda x : x[1]['City'],d.items()))

print(city)