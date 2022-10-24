#1
name =input("enter your name:")
print("hello,"+name+".")

import math
import random

#2
radius= input("enter a number:")
r= float(radius)
area= math.pi * r * r
print("the area of the circle is:"+str(area))

#3
length = input("enter a length:")
width = input("enter a width:")
l= float(length)
w= float(width)
perimetr= 2*(l+w)
area2= l*w
print("the perimeter is :"+str(perimetr)+" the area is :"+str(area2))

#4
x,y,z = input(" please enter 3 numbers").split()
int1= int(x)
int2= int(y)
int3= int(z)
sum= int1+int2+int3
product= int1*int2*int3
avg= sum/3
print(" the sum is: "+str(sum)+" the product is: "+str(product)+" the average is: "+str(avg))

#5

talent= input("enter the talent:")
pound= input("enter the pounds:")
lot= input ("enter the lots:")
talentg= 20*32*13.3* float(talent)
poundg= 32*13.3*float(pound)
lotg= 13.3*float(lot)
result= talentg+poundg+lotg
kg= int(result/1000)
grams = result -kg *1000
print("The weight in modern units: "+str(kg)+" kg and "+ f"{str(grams):.6}"+ " grams")

#6
print(str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)))
print(str(random.randint(1,6))+str(random.randint(1,6))+str(random.randint(1,6))+str(random.randint(1,6)))



