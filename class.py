import random


class Car:
    def __init__(self,reg_num, max_speed, current_speed =0, dist =0):
        self.reg_num = reg_num
        self. max_speed = max_speed
        self.current_speed= current_speed
        self.dist = dist

    def accelerate(self, speed):
        self.current_speed += speed
        if self.current_speed> self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed <0:
            self.current_speed =0

        return speed

    def drive(self, hours):
        self.dist += hours * self.current_speed





"""car = Car("ABC-123",142)

print(f"the registration number of the car is {car.reg_num} and the max speed is"
      f" {car.max_speed} the current speed and distance travelled are {car.current_speed}"
      f" {car.dist}")
print(car.current_speed)
car.accelerate(30)
print(car.current_speed)
car.accelerate(70)
print(car.current_speed)
car.accelerate(50)
print(f"the speed of the car now is {car.current_speed}")
car.accelerate(-200)
print(f"after emergency brake the speed is {car.current_speed}")

car.accelerate(60)
car.dist= 2000
print(f"the distance travelled is {car.dist} km and the speed is {car.current_speed}")

car.drive(1.5)
print(f"the distance in 1.5h is {car.dist}")
"""
#4
car_list =[]

for i in  range(10):
    car_list.append(Car("ABC-"+ str(i+1), random.randint(100, 200)))


travelled_max=0
while travelled_max < 10000:
    for car in car_list:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        travelled_max= max(car.dist, travelled_max)


for car in car_list:
    print(f"{car.reg_num} : {car.max_speed}, {car.dist}")
print(f"the winner was able to travel:{travelled_max}")








