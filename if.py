#1
length = float(input("what is the length of your zander?"))
result= 42-length
if length>= 42:
    print("you can catch the fish")

else:
    print("oh no! the fish is "+str(result)+" cm below the limit")
    print("release the fish!")

#2
cabin = input("please give your cabin preference:(LUX,A,B,C)")
if cabin == "LUX":
    print("upper-deck cabin with a balcony")
elif cabin =="A":
    print("above the car deck, equipped with a window.")
elif cabin == "B":
    print("windowless cabin above the car deck.")
elif cabin == "C":
    print("windowless cabin below the car deck.")
else:
    print("Invalid cabin class")

#3

gender = input("What is your gender?(male/female")


if gender== "male":
    hemo = float(input("What is your hemoglobin?"))
    if hemo <134:
        print("your hemoglobin is low ")
    elif 134<=hemo<167:
        print("your hemoglobin is normal")
    elif hemo> 167:
        print("your hemoglobin is high")
if gender == "female":
    hemo = float(input("What is your hemoglobin?"))
    if hemo<117:
        print("your hemoglobin is low ")
    elif 117 <= hemo < 155:
        print("your hemoglobin is normal")
    elif hemo > 155:
        print("your hemoglobin is high")

#4
year= int(input("please enter a year"))
if year% 4==0:
    print("it is a leap year")
    if year% 100==0:
       print("it is a leap year")
    if year% 400==0:
       print("it is a leap year")
else:
    print("it's not a leap year")
