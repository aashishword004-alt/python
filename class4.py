# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 11:50:53 2026

@author: ex409_28


4)	Consider the list of STATES that contains its Lok Sabha and Rajya Sabha seats as below:

    Create a menu driven program to find following data. Create user defined functions
•	Total number of seats in all given states.
•	Display the list in descending order of their Lok Sabha seats.
•	States having Least number of Rajya Sabha Seats
"""
from functools import reduce
state =   {"MP": (29, 11), "UP": (80, 31), "TN": (39, 18) 
          ,"MH": (48, 19) ,"GJ": (26, 11), "RJ": (25, 10),
          "HP": (4, 3) }
d={k:sum(v) for k,v in state.items()}
seat = sorted(d.items(),key=lambda x : x[1],reverse=True)
print(seat)
 
 
total = reduce(lambda x,y :x+y ,{k:sum(v) for k,v in state.items()}.values())
print(total)

    