# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 11:40:47 2026
Find out he higested price of the vehicle available for rent
@author: ex409_28
"""
v= {
    101: ["Swift", "Car", 1800, "Available"],
    102: ["Activa", "Scooter", 700, "Rented"],
    103: ["Creta", "Car", 2500, "Available"],
    104: ["Bullet", "Bike", 1200, "Available"]
    }

high = sorted(v.items(),key=lambda x : x[1][2],reverse=True)

print(high[0])