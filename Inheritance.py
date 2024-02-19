
### 1. Single inheritance: When only child class inherits from only one parent class, it is called single inheritance

# class A:
#     def m1(self):
#         print("this method is from parent class A")
# a1 = A()
# a1.m1()

# class B(A):
#     print("this method is from class B")
#
# b1 = B()
# b1.m1()


# class A:
#     def m1(self):
#         print("This m1 method is from Parent class A")
#
# a1=A()
# a1.m1()  # Parent class object call m1
#
# class B(A):
#     pass
# b1=B()
# b1.m1() # Child class object call m1


# class A:
#     def m1(self):
#         print("This m1 method is from Parent A")
# class B(A):
#     def m2(self):
#         print("This m2 method is from Parent B")
# # aobj=A()
# # aobj.m1()  # Parent class object call m1
# bobj=B()
# bobj.m2() # Child class object call child method m2
# bobj.m1() # Child class object call parent method m1


# class Parent:
#     def flats(self,type1,type2):
#         print("Parent ka flat hai Delhi me",type1)
#         print("unka pune bhi flat hai ",type2)
# class Child(Parent):
#     def Unemployed (self):
#         print("Mera kuch nahi hai")
#         print("But Parent ka sab mera hai")

# c = Child()
# c.Unemployed()
# c.flats('1BHK','2BHK')


# class A:
#     a,b=100,200
#     def m1(self):
#         print(self.a+self.b)
#
# class B(A):
#     x,y=10,20
#     def m2(self):
#         print(self.x + self.y)
#
# bobj=B()
# bobj.m2()
# bobj.m1()

#########################################################################################

### 2. Multilevel inheritance: When we have a child and grandchild relationship.

# class A:
#     a,b = 100,200
#     def m1(self):
#         print(self.a+self.b)
# class B(A):
#     x,y = 10,20
#     def m2(self):
#         print(self.x+self.y)
# class C(B):
#     i,j = 3,4
#     def m3(self):
#         print(self.i+self.j)

# aobj = A()
# aobj.m1()
# aobj.m2() ## Invalid

# bobj = B()
# bobj.m1()
# bobj.m2()
# bobj.m3()  ## Invalid

# cobj = C()
# cobj.m1()
# cobj.m2()
# cobj.m3()



# class A: # dadaji = 300 rs
#     a,b=100,200
#     def m1(self):
#         print(self.a+self.b)
# #
# class B(A): # papa 30 rs, dadaji ka 300 bhi display kr sakta hai
#     x,y=10,20
#     def m2(self):
#         print(self.x + self.y)
# #
# class C(B): # grand son 3, papaji ke 30 rs aur dadaji ke 300 rs dispaly kr sakta hai
#     i,j=1,2
#     def m3(self):
#         print(self.i + self.j)
# # aobj=A()
# # aobj.m1()
# # aobj.m2() # invalid
# # aobj.m3() # invalid
# #
# # bobj=B()
# # bobj.m2()
# # bobj.m1()
# # bobj.m3() # invalid
# # #
# cobj=C()
# cobj.m3()
# cobj.m2()
# cobj.m1()


# class A():
#     def m1(self):
#         print("This is m1 method of Parent A")
# class B(A):
#     def m2(self):
#         print("This is m2 method of Child B")
# class C(A):
#     def m3(self):
#         print("This is m3 method of GrandChild C")
# # b1=B()
# # b1.m1()
# # b1.m2()
# # b1.m3() # invalid
# c1=C()
# c1.m1()
# c1.m3()
# c1.m2()  # invalid

##############################################################################################

### 3. Hierarchical inheritance = More than one derived class are created from a single base.

# class A():
#     def m1(self):
#         print("This is m1 method of Parent A")
# class B(A):
#     def m2(self):
#         print("This is m2 method of Child B")
# class C(A):
#     def m3(self):
#         print("This is m3 method of GrandChild C")
# b1=B()
# b1.m1()
# b1.m2()
#
# c1=C()
# c1.m1()
# c1.m3()
#c1.m2()  # invalid

##############################################################################################3

###4. Multiple inheritances: When a child class inherits from multiple parent classes, it is called multiple
# inheritances

# class A():
#     def m1(self):
#         print("This is m1 method from A")
# class B():
#     def m2(self):
#         print("This is m2 method from B")
#
# class C(A,B):
#     def m3(self):
#         print("This is m3 method from C")

# aobj = A()
# aobj.m1()
# aobj.m2()  ## invalid
# aobj.m3()  ## invalid

# bobj = B()
# bobj.m2()

# cobj = C()
# cobj.m1()
# cobj.m2()
# cobj.m3()


# class A():
#     def m1(self):
#         print("This is m1 method of Father A")
# class B():
#     def m2(self):
#         print("This is m2 method of Mother B")
# class C(A,B):
#     def m3(self):
#         print("This is m3 method of Only child C")
#
# a1=A()
# a1.m1()
# a1.m2() #invalid
# a1.m3() #invalid
# #
# b1=B()
# b1.m1() #invalid
# b1.m2()
# b1.m3() #invalid
#
# c1=C()
# c1.m1()
# c1.m2()
# c1.m3()


### 5. Hybrid inheritances

# class A():
#     def m1(self):
#         print("This is m1 method of Parent A")
# class B(A):
#     def m2(self):
#         print("This is m2 method of Child B")
#
# a1=A()
# a1.m1()
# a1.m2()
#
# b1=B()
# b1.m1()
# b1.m2()


### The super() Method in Python Inheritance

# class A:
#     def m1(self):
#         print("This m1 method is from Parent A")
# class B(A):
#     def m1(self):
#         print("This m1 method is from Child B")
# b1=B()
# b1.m1() # Child class object call m1   override by parent class


### if we need to access the superclass method from the subclass, we use the super() method.

# class A():
#     def m1(self):
#         print("This is m1 method of Parent A")
# class B(A):
#     def m2(self):
#         print("This is m2 method of Child B")
#         super().m1()
# bobj=B()
# bobj.m2()


# class A:
#     def m1(self):
#         print("This m1 method is from Parent A")
# class B(A):
#     def m1(self):
#         print("This m1 method is from Child B")
#         super().m1()
# b1=B()
# b1.m1() # Child class object call m1



### 2. to invoke the parent class variables
# class A:
#     a,b=100,200
#     def m1(self):
#         print(self.a+self.b)
# class B(A):
#     i,j=10,20
#     def m2(self,x,y):
#         print(x+y) # local variable
#         print(self.i + self.j) # child class variables
#         print(self().a + self().b) # parent class variables
# bobj=B()
# bobj.m2(10,200)


# class A:
#     a,b=100,200
#     def m1(self):
#         print(self.a+self.b)
# class B(A):
#     a,b=10,20
#     def m2(self,a,b):
#         print(a+b) # local variable
#         print(self.a + self.b) # child class variables
#         print(self.a+self.b) # parent class variables run nhi hoga  ## its takes as child class variables
# bobj=B()
# bobj.m2(10,200)


# class A:
#     a,b=100,200
#     def m1(self):
#         print(self.a+self.b)
# class B(A):
#     a,b=10,20
#     def m2(self,a,b):
#         print(a+b) # local variable
#         print(self.a + self.b) # child class variables
#         print(super().a+super().b) # parent class variables
# bobj=B()
# bobj.m2(10,200)



# a,b= 10000,20000
#
# class A:
#     a,b=100,200
#     def m1(self):
#         print(self.a+self.b)
#
#
# class B(A):
#     a,b=10,20
#     def m2(self,a,b):
#         print(a+b) # local variable 300
#         print(self.a + self.b) # child class variables 30
#         print(self.a + self.b) # Child class variables 30
#         print(super().a + super().b) # parent class variables 300
#         print(a+b) # local variables 300
#         print(globals() ['a'] + globals() ['b']) # global variables
# bobj=B()
# bobj.m2(100,200)



# class A():
#     def __init__(self):
#         print("This is constructor of parent A")
# class B(A):
#     def __init__(self):
#         print("This is constructor of parent B")
#         super().__init__() # calls the parent call consrtuctor
#         A.__init__(self)  # calls the parent call consrtuctor
# bobj=B()


### Polymorphism in Python

# Python program to demonstrate in-built polymorphic functions

# # len() being used for a string
# print(len("geeks"))
#
# # len() being used for a list
# print(len([10, 20, 30]))

### i.e same function used for different types

### Examples of user-defined polymorphic functions:

# A simple Python function to demonstrate Polymorphism

# def add(x, y, z = 0):
# 	return x + y+z
#
# # Driver code
# print(add(2, 3))
# print(add(2, 3, 4))



# class India():
#   def capital(self):
#      print("New Delhi is the capital of India.")
#
#   def language(self):
#      print("Hindi is the most widely spoken language of India.")
#
#   def type(self):
#      print("India is a developing country.")
# # #
# class USA():
#   def capital(self):
#      print("Washington, D.C. is the capital of USA.")
#
#   def language(self):
#      print("English is the primary language of USA.")
#
#   def type(self):
#      print("USA is a most highest economy country.")
#
# obj_ind = India()
##obj_ind.language()
##obj_ind.type()
##obj_ind.capital()

# obj_usa = USA()

# for country in(obj_ind,obj_usa):
#     country.capital()
#     country.type()
#     country.language()


### Method overriding

# class Bird:
#     def intro(self):
#         print("There are many types of birds.")
#     def flight(self):
#         print("Most of the birds can fly but some cannot.")
# class sparrow(Bird):
#     def flight(self):
#         print("Sparrows can fly.")
# class ostrich(Bird):
#     def flight(self):
#         print("Ostriches cannot fly.")
#
#
# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()
# #
# obj_bird.intro()
# obj_bird.flight()
# # # #
# obj_spr.intro()
# obj_spr.flight()
# # #
# obj_ost.intro()
# obj_ost.flight()
#


# class Animal:
#   def speak(self):
#      raise NotImplementedError("Subclass must implement this method")
#
# class Dog(Animal):
#   def speak(self):
#      return "Woof!"
#
# class Cat(Animal):
#   def speak(self):
#      return "Meow!"
# # #
# # # # Create a list of Animal objects
# animals = [Dog(), Cat()]
# # #
# # # Call the speak method on each object
# for animal in animals:
#   print(animal.speak())



# method Overriding
# class Parent():
#     # Constructor
#     def __init__(self):
#         self.value = "Inside Parent"
#
#     # Parent's show method
#     def show(self):
#         print(self.value)

# # Defining child class
# class Child(Parent):
#
#     # Constructor
#     def __init__(self):
#         self.value = "Inside Child"
#
#     # Child's show method
#     def show(self):
#         print(self.value)
#
#
# # Driver's code
# obj1 = Parent()
# obj2 = Child()
#
# obj1.show()
# obj2.show()




# # Method Overloading

# First product method.Takes two argument and print their product
# def product(a, b):
#     p = a * b
#     print(p)
#
# # Second product method Takes three argument and print their product
# def product(a, b, c):
#     p = a * b * c
#     print(p)

# Uncommenting the below line shows an error
# product(4, 5)


# This line will call the second product method
# product(4, 5, 5) # --- Overload krna


# Function to take multiple arguments
# Function to take multiple arguments
# def add(datatype, *args):
#
#   # if datatype is int initialize answer as 0
#   if datatype == 'int':
#      answer = 0
#
#   # if datatype is str initialize answer as ''
#   if datatype == 'str':
#      answer = ' '
#
# #   # Traverse through the arguments
#   for x in args:
#      # This will do addition if the arguments are int. Or concatenation if the arguments are str
#      answer = answer + x

#  print(answer)
# Integer
# add('int', 5, 6)

# String
# add('str', 'Hi ', 'Geeks')


#### Abstraction in Python

# Python program demonstrate abstract base class work
from abc import ABC, abstractmethod

# class Car(ABC):
#     def mileage(self):
#         pass
#
# class Tesla(Car):
#     def mileage(self):
#         print("The mileage is 30kmph")
#
# class Suzuki(Car):
#     def mileage(self):
#         print("The mileage is 25kmph ")
#
# class Duster(Car):
#     def mileage(self):
#         print("The mileage is 24kmph ")
#
# class Renault(Car):
#     def mileage(self):
#         print("The mileage is 27kmph ")
#
#     # Driver code
#
# t = Tesla()
# t.mileage()
#
# r = Renault()
# r.mileage()
#
# s = Suzuki()
# s.mileage()
#
# d = Duster()
# d.mileage()


### 1 Public Member
## Public data members are accessible within and outside of a class. All member variables of the class
# are by default public.

# class Employee:
#     # constructor
#     def __init__(self, name, salary, project):
#         # data members
#         self.name = name
#         self.salary = salary
#         self.project = project
# #
# #     # method
# #     # to display employee's details
#     def show(self):
#         # accessing public data member
#         print("Name: ", self.name, 'Salary:', self.salary)
# #
# #     # method
#     def work(self):
#         print(self.name, 'is working on', self.project)
#
# # # creating object of a class
# emp = Employee('Jessa', 8000, 'NLP')
# #
# # # calling public method of the class
# emp.show()
# emp.work()
#


### 2 Private Member
# We can protect variables in the class by marking them private. To define a private variable add two
# underscores as a prefix at the start of a variable name.Private members are accessible only within the
# class, and we can’t access them directly from the class objects.

# class Myclass():
#     __a = 10
#     def display(self):
#         print(self.__a)
#     def show(self):
#         print(self.__a)
# obj = Myclass()
# obj.display()
# obj.show()

# class Employee:
#     # constructor
#     def __init__(self, name, salary):
#         # public data member
#         self.name = name
#         # private member
#         self.__salary = salary
#
# # creating object of a class
# emp = Employee('Jessa', 10000)
#
# # accessing private data members
# print('Salary:', emp.__salary)




# class myclass():
#     __a=10
#     def display(self):
#         print(self.__a)
# obj=myclass()
# obj.display()


# class myclass():
#     def __display(self):
#         print("This is private method")
#     def show(self):
#         print("This is public method")
#         self.__display()
# obj=myclass()
# # obj.__dispaly() we cant access private method outside the class
# obj.show()


### Protected Member
# Protected members are accessible within the class and also available to its sub-classes.
# To define a protected member, prefix the member name with a single underscore_.
# Protected data members are used when you implement inheritance and want to allow data members access
# to only child classes.

# class A():
#     def _m1(self):
#         print("This is Protected Method M1")
# class B(A):
#     def _m2(self):
#         print("This is Protected Method M2")
#         super()._m1()
# b1=B()
# b1._m2()


# class myclass():
#     __a=10
#     def display(self):
#         print(self.__a) # a se bulavoge to nhi ayaga
# obj=myclass()
# obj.display()



# class myclass():
#     def __display(self):
#         print("This is private method")
#     def show(self):
#         print("This is public method")
#         self.__display() #-- display lete to nhi ata isiliye __ lena jaruri hai
# obj=myclass()
# # obj.__dispaly() we cant access private method outside the class
# obj.show()


# Protected example
# class Company():
#     _project= "banking"
#
# class Employee(Company):
#     def __init__(self, name):
#         self.name = name
#         Company.__init__(self)
#
#     def show(self):
#         print("Employee name :", self.name)
#         # Accessing protected member in child class
#         print("Working on project :", self._project)
#
# c = Employee("Jessa")
# c.show()

