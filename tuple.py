#1

season =("spring", "summer", "autumn", "winter")
(first, second , third, forth)= season
month_num = int(input("enter the number of month (1-12)"))
mon_list =[[3,4,5] , [6,7,8],[9,10,11],[12,1,2]]

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




