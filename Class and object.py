

# class myfunc():
#     def mymob(self):
#         pass
#     def Display(self,name):
#         print("Name is :",name)
# mc = myfunc()
# mc.mymob()
# mc.Display("Vishwas")
# myfunc().Display("KKK")

# class Mypractice:
# class Mypractice():
# # Both above syntaxes will create the class.
# class Myclass():
#     def myfun(self):
#         pass
#     def display(self,name):
#         print("name is:", name)


# Difference between function and methods
# if we define functions without class then they will be identifies as function-- C Language
# if we define functions with class then they will be identifies as function--- Java
# if we define functions with class then they will be identifies as method--- Python
# Python supports both. with or without class we can use functions.

# now if we want to access above class we need to create an object
# mc = Myclass()  # Myclass() is actual object and mc is reference variable means variable which holds Myclass object
# mc.myfun()  # kuch nhi milega
# mc.display("Yusuf")  # name is: Yusuf

# Myclass().myfun()
# Myclass().display("Rahul")

# class Myclass1():
#     def m1(self):  # Instance Method - When i create a method within a class by default it is instance method
#         print("We are printing Instance Method")
#
#     @staticmethod
#     def m2(self): # Static Method
# In this self is treated as actual arguments not like instance method means
# we must have to pass the argument  while accesing this method using object.

        # print("We are printing Static Method",self)

# mc1 = Myclass1() # mc1 is instance variable which will store Myclass1 Object
# mc1.m1() # We are printing Instance Method
#
# Myclass1().m2("Anil") # We are printing Static Method with self. agar self likha hai m2 me to run hoga
# Myclass1().m2() # We are printing Static Method without self. agar self nhi likha hai to run hoga


# static method with parameters

# class Myclass():
#     def m1(self):
#         print("We are printing instance method")
#
#     @staticmethod
#     def m2(self):
#         print("We are printing static method")
# mc1 = Myclass()
# mc1.m1()
# mc1.m2("self")


# class Myclass1():
#     def m1(self):
#         print("We are printing Instance Method")
#     @staticmethod
#     def m2(): # Static Method
#         print("We are printing Static Method")
# #
# mc1 = Myclass1()
# mc1.m1()
# mc1.m2()
# Myclass1().m2("Anil")


# class Myclass1():
#     def m1(self):
#         print("We are printing Instance Method")
#     @staticmethod
#     def m2(): # Static Method
#
#         print("We are printing Static Method")
#
# mc1 = Myclass1()
# mc1.m1()
# Myclass1().m2()



### declaring variables inside the class

# class myclass():
#     a = 30
#     b = 20
#     def add(self):
#         # print(a+b)
#         print(self.a + self.b)
#     def mul(self):
#         print(self.a*self.b)
#
#     def div(self):
#         print(self.a/self.b)
#
# mc = myclass()
# mc.add()
# mc.mul()
# mc.div()


# class Myclass2:
#
#     a = 100  # Class variable
#     b = 200  # class Variable
#     def add(self):
#
#         print(a+b) # It will not add becz a and b are not defined in add method
#         print(self.a+self.b) # it will add becz self will used to access the class variables
#
#     def mul(self):
#         print(self.a*self.b)
# #
# mc2 = Myclass2()
#
# mc2.add()
# mc2.mul()



# i,j = 100,200  # Global Variables
# class Myclass3:
#     a,b= 10,20 # Class variables
#     def add(self,x,y): # x and y are local variables
#         print(x+y)
#         print(self.a+self.b)
#         print(i+j)
# mc3 = Myclass3()
# mc3.add(1000,2000)


# i,j,k = 10,20,30
# class Myclass():
#     a,b,c = 50,60,70
#     def add(self,a,b,c):
#         print(self.a+self.b+self.c)
#         print(a+b+c)
#         print(i+j+k)
#     def mul(self):
#         print(self.a*self.b*self.c)
#         print(i*j*k)
#     def sub(self):
#         print(self.a-self.b-self.c)
#         print(i-j-k)
# mc = Myclass()
# mc.add(45,45,45)
# mc.mul()
# mc.sub()


### local variables, global variables and class variables with same name

# a,b=100,200 # Global variables
# class Myclass4:
#     a,b=10,20 # Class Variables
#     def add(self,a,b): # Local Variables
#         print(a+b) # access local with normal print 3000
#         print(self.a+self.b) # access class with self keyword 30
#         print(a+b) # access local with normal print -3000
#         print(globals()['a']+globals()['b']) # access global with globals method
#
# mc4=Myclass4()
# mc4.add(1000,2000)


# a,b = 100,200
# class MyCal():
#     a,b = 10,20
#     def m1(self,a,b):
#         print(a+b)
#         print(self.a+self.b)
#         print(globals()['a']+globals()['b'])
# mc = MyCal()
# mc.m1(3,4)


## creating multiple objects for same class
# class Myclass5:
#     def add(self,x,y):
#         print(x+y)
# mc5= Myclass5()
# mc6= Myclass5()
#
# mc5.add(1000,2000)
# mc6.add(4000,2000)


# class Myclass5:
#     def add(self,x,y):
#         print(x+y)
#     def display(self):
#         print("Hello")
# mc5= Myclass5()
# mc6= Myclass5()
#
# mc5.add(1000,2000)
# mc5.display()
# mc6.add(1000,2000)
# mc6.display()

## named and nameless objects

# class Myclass5:
#     def add(self, x, y):
#         print(x + y)
#
#     def display(self):
#         print("Hello")
#
#
# mc5 = Myclass5()  # Named Object mc5
#
# mc5.add(1000, 2000)  # Named Object mc5 accessing the add method from class
# mc5.display()  # Named Object mc5 accessing the display method from class
#
# Myclass5().add(1000, 2000)  # Nameless Object accessing the add method from class
# Myclass5().display()  # Nameless Object accessing the display method from class


## how to check memory locations of objects
# class Myclass5:
#     def add(self,x,y):
#         print(x+y)
#     def display(self):
#         print("Hello")
# mc5= Myclass5()
# mc6= Myclass5()
#
# mc5.add(1000,2000)
# mc5.display()
# mc6.add(1000,2000)
# mc6.display()
#
# print(id(mc5))
# print(id(mc6))


### Constructor
### Syntax of constructor declaration : 
### def __init__(self):
      # body of the constructor


# class MyTeam():
#     def __init__(self,name):
#         print("Our Team Lead is :",name)
#
# mc = MyTeam("Vishwas")
# MyTeam("Vishwas")


# class Myclass7():
#
#     def __init__(self):
#         print("This is without Parameter Constructor")
# #
# #
# Myclass7() # without defining objecct
# mc7=Myclass7() # with defoined obj
# mc7.__init__() #with defoined obj   but if we pass argument then shows missing argument error



# class Myclass10():
#     def __init__(self,name):
#         print(name)
# mc10=Myclass10("Abhi")


# class Myclass10():
#     name="Amit"  #class variable
#     def __init__(self,name): # local Variable
#         print(name)
#         print(self.name)
# #
# mc10=Myclass10("Abhi")


# class Myclass8:
#     def values(self,val1,val2): # val1 and val2 are local variables
#         print(val1)
#         print(val2)
#     def add(self):
#         # print(val1+val2)  # cant print becz val1 and val2 are part of values method
# mc8=Myclass8()
# mc8.values(10,20)
# mc8.add()


# class Myclass8:
#     def values(self,val1,val2): # val1 and val2 are local variables
#         print(val1)
#         print(val2)
#         self.val1=val1  # val1 become class variable
#         self.val2=val2  # val2 become class variable
#     def add(self):
#         print(self.val1+self.val2)  # cant print becz val1 and val2 are part of values method
# mc8=Myclass8()
#
# #
# mc8.values(10,20)
# mc8.add()


# class Myclass8:
#     def __init__(self,val1,val2): # val1 and val2 are Parameterized Constructor  local variables
#
#         print(val1)
#         print(val2)
#         self.val1=val1  # val1 become class variable
#         self.val2=val2  # val2 become class variable
#     def add(self):
#         print(self.val1+self.val2)  # cant print becz val1 and val2 are part of values method
# mc8=Myclass8(10,20)
#
# mc8.add()


## How to call current class method in another method

# class Myclass9:
#     def m1(self):
#         print("This is m1 method")
#         self.m2(100) # yahase maine self ka use krke m2 ko bulaya
#     def m2(self,a):
#         print("This is m2 method and value of argument is:",a)
# m9=Myclass9()
# #
# m9.m1()


# This is m1 method
# Tis is m2 method and value of argument is: 100

# class emp:
#     def __init__(self,eid,ename,esal): # local varaible
#         self.eid = eid
#         self.ename = ename
#         self.esal = esal
#     def display(self):
#         print("Empid: {} Empname:{} Empsal:{}".format(self.eid,self.ename,self.esal))
# e1=emp(10,"Yusuf",60000)
#
# e1.display()


# class consdemo():
#     def __init__(self,a,b):
#         print(a)
#         print(a)
# cd1= consdemo(10,20)








