#1

season =("spring", "summer", "autumn", "winter")
(first, second , third, forth)= season
month_num = int(input("enter the number of month (1-12): "))
mon_list =[[3,4,5],[6,7,8],[9,10,11],[12,1,2]]

if month_num in mon_list[0]:
    print(first)
elif month_num in mon_list[1]:
    print(second)
elif month_num in mon_list[2]:
    print(third)
elif month_num in mon_list[3]:
    print(forth)
else:
    print("invalid month number")


#2
names = set()
while True:
    name = (input("Enter a name: "))
    if name == "":
        for i in names:
            print(i)
        break

    nameToCompare = name in names
    if nameToCompare:
        print("already exists")
    else:
        print("New name")
        names.add(name)

#3
blah= {}
while True:
    airport= int(input("enter a number \n1. enter airport \n2. fetch the information  \n3. quit\n"))
    if airport ==1:
        airport_name = input("enter the airport name")
        icao_code = input("enter the ICAO code")
        print("INFO SAVED!!!")
        blah[icao_code]=airport_name
    elif airport ==2:
        icao_code= input("enter the ICAO code")
        if icao_code in blah:
         print(f"THE AIRPORT IS: {blah[icao_code]}")
    elif airport ==3:
        break
    else:
        print("wrong info")










