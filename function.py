#1

import random
def dice_num():
    dice_roll = random.randint(1, 6)
    return dice_roll

while dice_num()<=5:
    print("the number is:",dice_num())
    if dice_num()==6:
     break

#3
def gallons(n):
    litres= n*3.785
    return litres


value = float(input("enter value in gallons: "))

while value>0:
    value = float(input("enter value in gallons: "))
    print=("the value in litres is: ",gallons(value))
    if value<0:
        break


#4
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total


list=[2,6,5,4,8]
print(sum(list))

#5
def list(list1):
    list1 = [2, 4, 19, 13, 42, 6, 65]
    for num in list1:
        if num % 2 == 0:
            print(num, end=" ")
            return list1


list1 = [2, 4, 19, 13, 42, 6, 65]
print(list1)
(list(list1))


#6
import math
def pizza(diameter,euro):
    diameter= float(input("please enter the diameter of the pizza: "))
    euro= float(input("please enter the price of the pizza: "))

    r = diameter/2
    area = (math.pi * r**2)
    result = euro/area
    print(f"the cost per square inch is {result:.2f}  euros")

    return result

pizza()

diameter2= float(input("please enter the diameter of other pizza:"))
euro2 = float(input("please enter the price of other pizza: "))
pizza(diameter2,euro2)

if pizza()> pizza(diameter2,euro2):
    print("the other pizza is cheaper")
else:
    print("the first pizza is cheaper")















