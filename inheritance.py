class Publication:
    def __init__(self,name):
        self.name = name





class Book(Publication):
    def __init__(self,name,author, page_count):
        super().__init__(name)
        self.author= author
        self.page_count= page_count

    def print_info(self):

        print(f"{self.name},{self.author}, {self.page_count}, ")

class Magazine(Publication):
    def __init__(self,name,chief_editor):
        super().__init__(name)
        self.chief_editor=chief_editor

    def print_info(self):

        print(f"{self.name}, {self.chief_editor}")


pubs =[]
pubs.append(Magazine("donald duck", "aki hyyppa"))
pubs.append(Book("Compartment No. 6", "Rosa Liksom",192))

for pub in pubs:
    pub.print_info()


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


class ElectricCar(Car):
    def __init__(self,reg_num,max_speed,battery):
        super().__init__(reg_num, max_speed)
        self.battery= battery


    def print_travDist(self):
        print("travelled distance is "+ str(self.dist))



class GasolineCar(Car):
    def __init__(self,reg_num,max_speed, tank):
        super().__init__(reg_num,max_speed)
        self.tank =tank


    def print_travDist(self):
        print("travelled distance is "+ str(self.dist))


elec_car = ElectricCar("ABC-15",180,52.5)
gas_car = GasolineCar("ACD-123" , 165, 32.7)
elec_car.accelerate(80)
gas_car.drive(3)
gas_car.accelerate(120)
gas_car.drive(3)
elec_car.print_travDist()
gas_car.print_travDist()




