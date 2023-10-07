# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 17:45:38 2022

@author: bezbakri
"""

import json
import random

def main():
    with open("dataset_v2.json", "r") as f:
        restaurant_list = json.load(f)
        cleaned_restaurant_list = []
        for i in range(len(restaurant_list)):
            try:
                if restaurant_list[i]["area"] == "Campustown":
                    cleaned_restaurant_list.append(restaurant_list[i])
            except:
                pass
        print(cleaned_restaurant_list[random.randint(0,len(cleaned_restaurant_list) - 1)])
    
if __name__ == "__main__":
    main()