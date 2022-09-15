#1
import random


num_dice = int(input("how many dice you want to roll?"))
sum_dice=0


for i in range (num_dice):
    ran = random.randint(1, 6)
    print('number:',ran )
    sum_dice = sum_dice + ran

print(sum_dice)

#2

input_list = []

num = (input('enter a number: '))

while num != "":
    input_list.append(float(num))
    num = (input('enter a number: '))


input_list.sort(reverse=True)
print(input_list[0:min(5, len(input_list))])

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











