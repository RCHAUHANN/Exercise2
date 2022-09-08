import math

#1
n=1
while n<=1000:
    if n%3==0:
        print(str(n))
    n=n+1

#2
inch = float(input("please enter a number in inches"))
cm= inch*2.54

while inch>=0:
    print("the value in centimeters is: " + str(cm))
else:
    print("NO NEGATIVE VALUE")



#3
largest = 0
smallest = 0

while True:
    num = input("Enter a number: ")
    if num =="":
     break
    if largest == 0 or num >= largest: largest = num
    else: largest= largest
    if smallest == 0 or num <= smallest: smallest = num
    else: smallest= smallest

print("Maximum is " ,largest)
print("Minimum is ",smallest)

#4

import random
rannum= random.randint(1, 10)
guess=0
while guess!= rannum:
   guess= input("guess a number from 1-10: ")
   print(rannum)
   if int(guess)==rannum:
      print("CORRECT!!")
      break
   elif int(guess)>rannum:
      print("Too high")
   else :
      print("too low")


#5
print("Enter your username and password")
count =0
while count<6:
    username=input("enter username:")
    password= input("enter password")
    if password=="rules" and username=="python":
        print("access granted. WELCOME!")
        break
    else:
        print("ACCESS DENIED.please try again")
        count +=1

#6
import math
n=0
counter=0
while True:
    N = int(input("enter the amount to generate"))
    while counter<= N:
        x= random.uniform(-1, 1)
        y=random.uniform(-1, 1)
        if x**2 + y**2<1:
            n+=1
    pi_approx =(4*n)/N
    print("the approximation of pi is "+str(pi_approx))
    break



