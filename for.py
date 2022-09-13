#1
import random


num_dice = int(input("how many dice you want to roll?"))
sum_dice=0

for sum_dice in range (num_dice):
    print('dice:',sum_dice ,'number:', random.randint(1, 6))
    sum_dice +=1

#2
num= int(input('enter a number: '))
input_list=[]
input_list.append(num)



while True:
       print(num)
       if num =="":
           break
           for num in range(5):
               input_list.append(num)
               input_list.sort(reverse=True)



print(input_list)


#3
n= int(input("enter a number to check prime:"))
answer= False
if n>1:
    for i in  range (2,n//2):
        if n%i==0:
            answer= True
            break

if answer:
    print(n,"is not a prime number.")
else:
    print(n, "is a prime number.")

#4
city =[]
for i in range(5):
   city_name= input("enter the name of a city: ")
   city.append(city_name)

for x in range (len(city)):
    print(city[x])











