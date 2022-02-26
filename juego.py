# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 01:39:39 2022

@author: nicol
"""
import random


nro_azar = random.randint(0,100)
nro_participante = int(input("Elija el nro:"))
while (nro_azar != nro_participante):
  if( nro_azar > nro_participante):
    print("Elegir un nro Mayor")
  else: 
    print("Elegir un nro Menor")
  nro_participante = int(input("Elija el nro:"))

print(f"Ganaste! el nro era {nro_azar}")
