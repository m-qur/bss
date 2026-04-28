import random
import time 
import math

bees=1
honey=0
pollen=0
tool_strength=1
capacity_strength=1

def loop():
    global pollen
    global bees
    global honey
    global tool_strength
    global capacity_strength
    print("What would you like to do?\n1) Collect Pollen\n2) Convert Honey\n3) Visit Shop")
    action = int(input(''))
    if action == 1:
        print(f"Current pollen: {pollen}")
        time.sleep(5)
        pollen += (50*tool_strength)
        print(f"Collected {50*tool_strength} pollen\nTotal Pollen: {pollen}/{capacity_strength*50}")
    if action == 2:
        print("Converting pollen...")
        time.sleep((pollen/(25*capacity_strength)))
        honey += pollen
        pollen = 0
        print(f"Pollen converted! Honey: {honey}")
    loop()
print("Welcome!\n")
loop()

