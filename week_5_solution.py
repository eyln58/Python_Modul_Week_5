# Question1

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2
    

#Question 2 
class School:
    def __init__(self, name , foundation_year):
        self.name = name
        self.foundation_year = foundation_year
        self.students = []
        self.teachers = []

    def add_new_student(self , student_name , student_class):   
        self.students.append((student_name , student_class))
        print(f"{student_name} isimli ogrenci {student_class} sinifina eklendi.")

    def add_new_teacher(self, teacher_name , branch):
        self.teachers.append((teacher_name, branch))
        print(f"{teacher_name} isimli ogretmen, {branch} bransina eklendi.")

    def view_student_list(self):
        print("The list of the students:")
        for student_name, student_class in self.students:
            print(f"Name : {student_name} , Class : {student_class}\n")

    def view_teacher_list(self): 
        print("The list of the teachers:")
        for teacher_name, branch in self.teachers:
            print(f"Name : {teacher_name} , Branch : {branch}\n")


# Question 3

class Shape():
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Rectangle(Shape):
    
    def calculate_area(self):
        print (self.width * self.height)

class Square(Shape):
    def calculate_area(self):
        print( self.width * self.width)


#Question 4

class vehicle:
    def __init__ (self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def view_vehicle_info (self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"
class off_road_vechicle (vehicle):
    def __init__ (self, brand, model, year, four_wheel_drive):
        super().__init__(brand, model, year)
        self.four_wheel_drive = four_wheel_drive
    def view_vehicle_info (self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Four wheel drive: {self.four_wheel_drive}"
class SportCar (vehicle):
    def __init__ (self, brand, model, year, max_speed):
        super().__init__(brand, model, year)
        self.max_speed = max_speed
    def view_vehicle_info (self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Max speed: {self.max_speed}"
    

# Question 5

# Q5
class Customer:
    def __init__(self,name,surname,tc_identification,phone):
        self.name = name
        self.surname=surname
        self.tc_identification=tc_identification
        self.phone=phone

    def display_information(self):
        return f"Musteri Bilgileri: {self.name} {self.surname} {self.tc_identification} {self.phone}"
    
class Account(Customer):
    def __init__(self, name, surname, tc_identification, phone,customer, account_number,balance):
        super().__init__(name, surname, tc_identification, phone)
        self.customer=customer
        self.account_number=account_number
        self.balance=balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance
    def money_check(self,amount):
        if self.balance - amount <=0:
            print(f"Hesabinizdaki bakiyeniz {self.balance} . Cekmeniz icin yeterli bakiye hesabinizda yoktur.")
        else:
            self.balance -= amount
        return 
    def display_balance(self):
        return f" Hesap Bakiyesi: {self.balance}"
