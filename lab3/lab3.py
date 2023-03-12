# Q1.Answer:
# class Rectangle:
#     wageth=0
#     height=0
#     def area(self,w,h):
#         self.wageth=w
#         self.height=h
#         area= w*h
#         print("area of rectangle where wageth= %d, and height= %d is: %d" % (w, h, area))

# rect = Rectangle()
# rect.area(5,5)

# -------------------------------------------------------------------------
# Q2.Answer: 
# import math
# class Circle:
#     radius=0
#     def circumference(self,r):
#         self.radius=r
#         c = math.pi*2*r
#         cir =  "circumference of Circle where radius= %.2f is: %.2f" % (r,c)
#         print(cir) 
        
# circle = Circle()
# circle.circumference(5)


# -------------------------------------------------------------------------
# Q3.Answer: 

# class Employee:
#     name=""
#     age=0
#     salary=0    
#     def raise_salary(self,per,salary):
#         self.salary = salary
#         salar=(salary*(per/100))+salary
#         sal =  "salary after raising by percentage of = %.2f is: %.2f" % (per,salar)
#         print(sal) 
# emp = Employee()
# emp.raise_salary(10,5000)

# -------------------------------------------------------------------------
# Q4.Answer: 

# class Book:
#     title=""
#     author=""
    
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
        
#     def display(self):
#         print("the book title is: " +self.title)
#         print("the author of the book is: " +self.author)
        
# b1=Book("torab","mostafa")
# b1.display()

# -------------------------------------------------------------------------
# Q5.Answer: 

# class Car:
#     make=""
#     model=""
#     year=2005
#     mileage=0
#     def __init__(self,make,model,year,mileage):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.mileage=mileage
        
#     def drive(self,perc):
#         mile=(self.mileage)+perc
#         print("your mile age increased by value = %.2f and your total mileage is = %.2f" %(perc,mile))
        
# c1=Car("daweo","lanos",2010,20)
# c1.drive(10)

# -------------------------------------------------------------------------
# Q6.Answer: 

# class Person:
#     name=""
#     age=0
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print("constructor")
#         print(self.name)
#         print(self.age)
#     def __del__(self):
#         print("destructor")
# p1=Person("mostafa",25)
# del p1

# -------------------------------------------------------------------------
# Q7.Answer: 

# class BankAccount:
#     account_number=""
#     balance=0
#     def __init__(self,account_number,balance):
#         self.account_number=account_number
#         self.balance=balance
#         print("constructor start")
#         print("your account id is: %s" %self.account_number)
#         print("your balance in your account is: %.2f " %self.balance)
#     def __del__(self):
#         print("destructor: object is destroyed")

# b1=BankAccount("011",5000.500)
# del b1

# -------------------------------------------------------------------------
# Q8.Answer: 

# class Vehicle:
#     speed=0.0
#     def __init__(self,speed):
#         self.speed=speed
#         print("vehicle constructor")
    
# class Car(Vehicle):
#     brand=''
#     def __init__(self,speed,brand):
#         self.brand=brand
#         Vehicle.__init__(self, speed)

#     def display(self):
#         print(self.speed)
#         print(self.brand)

# c1= Car(120.50,"BMW")
# c1.display()

# -------------------------------------------------------------------------
# Q9.Answer: 

# class Animal:
#     name=''
#     def __init__(self,name):
#         self.name=name
#         print(self.name)
# class Pet:
#     owner=''
#     def __init__(self,owner):
#         self.owner=owner
#         print(self.owner)
# class Dog(Animal,Pet):
#     breed=''
#     def __init__(self,breed,name,owner):
#         self.breed=breed
#         print(self.breed)
#         Animal.__init__(self,name)
#         Pet.__init__(self,owner)
        
# d1=Dog('rex','ali','hasky')

# -------------------------------------------------------------------------
# Q11.Answer: 

# class Person:
#     name=''
#     def __init__(self,name):
#         self.name=name
#         print("person constructor")
#         print(self.name)
# class Employee(Person):
#     salary=0.0
#     def __init__(self,salary,name):
#         self.salary=salary
#         print("Employee constructor")
#         print(self.salary)
# class Manger(Employee):
#     dept=''
#     def __init__(self,salary,dept,name):
#         self.dept=dept
#         print("Manger constructor")
#         Person.__init__(self,name)
#         Employee.__init__(self,salary,name)
#         print(self.dept)
        
# m1=Manger("mostafa",5000.200,"sw")

# -------------------------------------------------------------------------
# Q12.Answer: 
# import math
# class Shape:
#     color=""
#     def area(self):
#         pass  

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (math.pi) * self.radius ** 2

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height


# c = Circle(5)
# print("Circle area:", c.area()) 

# r = Rectangle(3, 4)
# print("Rectangle area:", r.area()) 
# -------------------------------------------------------------------------
# Q14.Answer:

# class BankAccount:
#     __balance=0
#     def __init__(self,balance):
#         print(self.__balance)
        
#     def  get_balance(self):
#         print(" get_balance")
#         print(self.__balance)
        
#     def deposit(self):
#         amount = float(input("Enter amount to be deposited: "))
#         self.__balance += amount
#         print("\n Amount Deposited:", amount)
        
#     def withdraw(self):
#         amount = float(input("Enter amount to be withdrawn: "))
#         if self.__balance >= amount:
#             self.__balance -= amount
#             print("\n You Withdrew:", amount)
#         else:
#             print("\n Insufficient balance  ")  

# s = BankAccount(5000)
# s.deposit()
# s.withdraw()
# s.get_balance()
# -------------------------------------------------------------------------
# Q15.Answer:
from abc import ABC, abstractmethod
class Animal:
    @abstractmethod
    def speak():
        pass
        
class Dog(Animal):
    def speak(self):
        print("dog sound")

class Cat(Animal):
    def speak(self):
        print("cat sound")

d1=Dog()
c1=Cat()
d1.speak()
c1.speak()
# -------------------------------------------------------------------------
# Q16.Answer:

# class Calc:
#     @classmethod
#     def add(cls,x,y):
#         return x + y
    
# print(Calc.add(1,2))


