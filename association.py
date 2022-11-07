class Elevator:
    def __init__(self, top , bottom):
        self.top =top
        self.bottom = bottom
        self.current_floor= bottom



    def floor_up(self):
        self.current_floor+=1


    def floor_down(self):
        self.current_floor-=1

    def go_to_floor(self, floor):
        while self.current_floor != floor:
            if self.current_floor > floor:
                self.floor_down()
            elif self.current_floor < floor:
                self.floor_up()
            else:
                print("you are already at this floor", self.current_floor)


h = Elevator(0,10)
h.go_to_floor(5)
print("your floor number is", h.current_floor)
h.go_to_floor(10)
print("your floor is", h.current_floor)


class Building:
    def __init__(self,bottom, top, elevator_list):
        self.elevator_list= []
        for i in range(elevator_list):
            self.elevator_list.append(Elevator(bottom, top))



    def run_elevator(self, elevator_no,floor):
        print("the elevator no. ", elevator_no)
        self.elevator_list[elevator_no -1].go_to_floor(floor)


    def fire_alarm(self):
        print("FIRE FIRE FIRE!!!")
        for i in self.elevator_list:
            i.go_to_floor(i.bottom)








print(f"elevator in the building:")
building = Building(1,7,3)



#4 in class.py





