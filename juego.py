# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 01:39:39 2022

@author: nicol
"""
import random


MIN_NUMBER = 0
MAX_NUMBER = 100

    
def input_number_user():
    while True:
        try:
            value = int(input("Elija el nro: "))
            if (value < MIN_NUMBER or value > MAX_NUMBER):    
                print("Nro fuera de rango\n")
                continue
        except ValueError:
            print("Nro no valido\n")
            continue
        else:
            return value
            break

random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
input_number = input_number_user()

count_error = 0
while (random_number != input_number):
    count_error = count_error + 1
    if (random_number > input_number):
        print("Elegir un nro Mayor\n")
    else: 
         print("Elegir un nro Menor\n")
    input_number = input_number_user()

print()
print("********************************")
print(f"Ganaste! el nro era {random_number}")
print(f"Cantidad de intentos: {count_error}")
print("********************************")


