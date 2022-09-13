#1

import random
def dice_num():
    dice_roll = random.randint(1, 6)
    return dice_roll
value= dice_num()
while value<=5:
    print("the number is:",value)

    if value==6:
        print("the number is 6!!!")
        break
    value=dice_num()
print(value)


#2
def dice_num(sides):
    dice_roll = random.randint(1, sides)
    return dice_roll
blah = int(input("number pof sides?"))
value= dice_num(blah)
while value< blah:
    print(value)

    if value==blah:

        break
    value=dice_num(blah)
print(value)
#3
def gallons(n):
    litres= n*3.785
    print(f"Amount in litres {litres:.2f}")
    return litres




while True:
    value = float(input("enter value in gallons: "))


    if value<0:
        break
    gallons(value)


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

    for num in list1:
        if num % 2 != 0:
            list1.remove(num)

    return list1


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1)
potato = list(list1)
print(potato)


#6
import math
def pizza(diameter,euro):


    r = diameter/2
    area = (math.pi * r**2)*0.0001
    result = euro/area
    print(f"the cost per square inch is {result:.2f}  euros")

    return result

diameter1= float(input("please enter the diameter of the pizza: "))
euro1= float(input("please enter the price of the pizza: "))

diameter2= float(input("please enter the diameter of other pizza:"))
euro2 = float(input("please enter the price of other pizza: "))


if pizza(diameter1,euro1)> pizza(diameter2,euro2):
    print("the other pizza is cheaper")
else:
    print("the first pizza is cheaper")
















