
# a=100
# b=50
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

#
# a=100
# b=50
# c=1000
# d=500
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(c+d)
# print(c-d)
# print(c*d)
# print(c/d)

### define the function
# def greet():
#     print('Hello World!')
# greet()
# def greet():
#     print('Hello World! inside the function')
# #
# # # call the function
# greet()
# # #
# print('Bye Bye! Outside the function')
#
# def arithmatic():
#   print(a+b)
#   print(a-b)
#   print(a*b)
#   print(a/b)
# arithmatic()  #ERROR

#
# def arithmatic(a,b):
#   print(a+b)
#   print(a-b)
#   print(a*b)
#   print(a/b)
# arithmatic(200,50)

# def my_function(fname):
#   print(fname)
#
# my_function("Yusuf")
# my_function("Priya")
# my_function("Tushar")

#
# def my_function(fname,lname):
#   print(fname," ", lname)
# #
# my_function("Yusuf","Tamboli")
#
# def my_function(fname,lname):
#   print(fname," ", lname)
#
# my_function("Yusuf")    ###TypeError: my_function() missing 1 required positional argument: 'lname'



# # function with two arguments

# def add_numbers(num1, num2):
#     sum = num1 + num2
#     print("Sum: ",sum)
# #
# # # function call with two values
# add_numbers(5, 4)

# def add(num1,num2):
#     sum = num1+num2
#     print("Sum of two num",sum)
# add(34,56)


#
# def myFun(x, y=50):
#     print("x: ", x)
#     print("y: ", y)

#
# # Driver code (We call myFun() with only 1 argument)
#
# myFun(10)
# myFun(25)
# myFun(50)
# myFun(100)
# myFun(10,20)



# def myFun(x, y=50):
#     print("x: ", x)
#     print("y: ", y)
# #
# # # Driver code (We call myFun() with a and 2 argument)
# myFun(10)
# myFun(10,20)
# myFun(100,200)
# myFun(100,500)


# def printme(fname,lname):
#     print(fname,' ',lname)
# printme(lname="Tamboli",fname="Yusuf")

# def printinfo( name, age = 35 ):
#    "This prints a passed info into this function"
#    print("Name: ", name)
#    print("Age ", age)
#
# # # Now you can call printinfo function
# printinfo( name="miki" )
# printinfo( name="miki",age=40)

# def Nameinfo(name,age=34):
#     print("Name is ",name)
#     print("age is",age)
# Nameinfo(name="Vishwas")
# Nameinfo(name="gourav",age=29)
# When the above code is executed, it produces the following result −

# def add(b,a):
#    print(a+b)
# add(a=40, b=20)
# #
# def add(b,a):
#    print(a+b)
# add(a=20, b=40)

# def printme(fname):
#   "This prints a passed string into this function"
#   print(fname)
# #
# #
# # # Now you can call printme function
# printme(fname="Yusuf")
# printme("Tushar")

# def student(firstname, lastname):
#     print(firstname, lastname)
#
#
# # Keyword arguments
# student(firstname='Yusuf', lastname='Tamboli')
# student(lastname='Tamboli', firstname='Yusuf')
# student(firstname='Tamboli', lastname='Yusuf')

# def printinfo( name, age ):
#    "This prints a passed info into this function"
#    print ("Name: ", name)
#    print ("Age ", age)
# #
# # # Now you can call printinfo function
# printinfo( age=50, name="miki" )

# def my_function(child3, child2, child1):
#   print("The youngest child is " , child3)
#   print("The Oldest child is " , child1)
#
# my_function(child1 = "Banti", child2 = "Chintu", child3 = "Sonu")




# def printme( str ):
#    "This prints a passed string into this function"
#    print (str)
#
# # Now you can call printme function
# printme()


# def printme( str1 ):
#    "This prints a passed string into this function"
#    print (str1)
#
# # Now you can call printme function
# printme("Amitabh")

# def printme( str1,str2 ):
#    "This prints a passed string into this function"
#    print (str1," ",str2)
#
# # Now you can call printme function
# printme("Amitabh","Shenshah")
# printme("Ranbir","Rockstar")

# def printme(str1,str2):
#     print(str1," ",str2)
# printme("Vishwas","Rockstar")
# printme("Raj","king")

# def greet(a,b):
#     print(a + b)
#     print(a - b)
#     print(a * b)
#     print(a / b)
# greet(100,50)
# greet(1000,500)
# greet(10,5)

# def nameAge(name, age):
#     print("Hi, I am", name)
#     print("My age is ", age)


# You will get correct output because argument is given in order

# print("Case-1:")
# nameAge("Suraj", 27)

# # You will get incorrect output because
# # argument is not in order
# print("\nCase-2:")
# nameAge(27, "Suraj")


# def numbers(*a):
#     print(a)
# numbers(10,20,30,40,10,20,30,40,10,20,30,40)


# def myFun(a):
#   for i in a:
#      print(i)
# myFun('Hello Welcome to GeeksforGeeks')

# def myintro(a):
#     for i in a:
#         print(i,end="")
# myintro("Hello My Name is Vishwas")



# Python program to illustrate
# *args for variable number of arguments
# def myFun(*a):
#   for i in a:
#      print(i)
#
#
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# def numbers(*b):
#   print(b)
# numbers(10,20,30)
# #
#
# def numbers(*b):
#   print(b)
# numbers(10,"Yusuf","Mumbai","Pune")


# def numbers(**y):
#   print(y)
# numbers(a=10,b=20,c=30)


# def numbers(**b):
#   print(b)
# numbers(eid=10,name="Yusuf",newadd="Mumbai",oldadd="Pune")

# def empInfo(**Details):
#     print(Details)
#
# empInfo(id = 101,name ="Vishwas",addr ="Kolhapur",mob = 8796182196)

# def empInfo(**Details):
#     for key,value in Details.items():
#         print(key,value)
# empInfo(id = 101,name ="Vishwas",addr ="Kolhapur",mob = 8796182196)

# def myFun(**abc):
#     for key, value in abc.items():
#        print(key,value)
#
# # Driver code
# myFun(name='Yusuf', Age=31, Salary=50000)
#

# def numbers(a,*b):
#     print(a)
#     print(b)
#
# numbers(10,20,30)


# def numbers(a,*b):
#   c=a
#   for i in b: # i in b=30
#     c=c+i #20+30
#     print(c)
# numbers(20,30)

# def numbers(a,*b):
#
#   c=0
#   for i in b: # i in b=20,30
#     c=c+i
#     print(c)
# numbers(10,20,30)

# def numbers(a,*b):
#
#   for i in b: # i in 20,30
#     c=a+i
#     print(c)
# numbers(10,20,30)

# def numbers(*b):
#
#   c=0
#   for i in b:
#     c=c+i
#     print(c)
# numbers(10,20,30)


# fruits = ["apple", "banana", "cherry"]
# def my_function(fruits):
#   for x in fruits:
#       print(x)
#
# my_function(fruits)



# def arith(a,b):
#   def sub(c,d):
#     print(c-d)
#   sub(100,50)
#   print(a+b)
# arith(1000,500)



# def f1():
#   s = 'I love Automation'
#   print("before inner function - I hate Automation")
#   def f2():
#     print(s)
#
#   f2()
#   print("after inner fun - Outside funct statemnet")
#
# # Driver's code
# f1()
#
#

# return Statemnet
# def add(a,b):
#     c=a+b
#     print(c)
# add(20,10)

# def add(a,b):
#     c=a+b
#     print(c)
# print(add(20,10))


# def add(a,b):
#     c=a+b
#     print(c)
#     return c
# print(add(20,10))

# def add(a,b):
#     c=a+b
#     return c
# print(add(20,10))

# def add(a,b):
#     c=a+b
#     d=a-b
#     e=a*b
#     f=a/b
#     return c,d,e,f
# print(add(20,10))





# def add(a,b):
#     c=a+b
#     print(c)
#     return c  # c ki 30 value add function store ki hai
# result= add(100,50)
# print(result)

#
# def add(a,b):
#     c=a+b
#     print(c)
#     return c  # c ki 150 value add function ne apne andar store ki hai
# print(add(100,50)) #return value ko print krneke liye without variable print kiya using print statemnet
# result= add(100,50) #return value ko print krneke liye variable result banaya
# print(result)


# def add(a,b):
#     return a+b
# print(add(20,10))


# Defining a function without return statement
# def square(num):
#   num ** 2
# #
# #
# # # Calling function and passing arguments.
# print("Without return statement")
# print(square(50))
# #
#
# Defining a function with return statement

# def square(num):
#   return num ** 2
#
# # Calling function and passing arguments.
# print("With return statement")
# print(square(50))
#
#
# printing a output with print Statement
# def square(num):
#   print(num ** 2)
#
# print("Without return statement But with Print Satement")
# square(50)

#

# def arithmatic(a,b):
#
#   c=a+b
#   d=a-b
#   e=a*b
#   f=a/b
#   return c,d,e,f
#
# print(arithmatic(20,10))
#
#
# def arithmatic(a,b):
#
#   c=a+b
#   d=a-b
#   e=a*b
#   f=a/b
#   return c,d,e,f
#
# result= (arithmatic(20,10))
# print(result)

# def my_function(x):
#    return 5 * x
#
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

# def my_function(x):
#     c=5 * x
#
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))
#

# def find_square(num):
#     result = num * num
#     return result
#
# # function call
# square = find_square(3)
#
# print('Square:',square)


#simple Program for Function

# def greet():
#     print("Hello")
# greet()
#
# def greet():
#     print("Hello")
#     greet()  # Recursive function call
# greet() # normal function call
#

# def count(num):
#     if (num<0):
#         print("Stop")
#     else:
#         print(num)
#         count(num-1) #recursive fun call
# count(5)
# 5
# 4
# 3
# 2
# 1

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(3))


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# num = int(input("Enter a number: "))
# print(factorial(num))

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(5))
#

# def fib(n) :
#     if n==0:
#         return 0
#     elif n ==1 :
#         return 1
#     else :
#         return fib(n-1) + fib(n-2)
# num = int(input("Enter a number: "))
# print(fib(num))


# Function for nth Fibonacci number
# def Fibonacci(n):
#
#   # Check if input is less than 0 then it will
#   # print incorrect input
#   if n < 0:
#      print("Incorrect input")
#
#   # Check if n is 0
#   # then it will return 0
#   elif n == 0:
#      return 0
#
#   # Check if n is 1,2
#   # it will return 1
#   elif n == 1 or n == 2:
#      return 1
#
#   else:
#      return Fibonacci(n-1) + Fibonacci(n-2)
# # Driver Program
# print(Fibonacci(6))


#Without recursion solvinmg fibonacci question

# def fib(n):
#     previsouno=0
#     preprevisouno =1
#
#     print(previsouno)
#     print(preprevisouno)
#     for i in range(2,n):
#         c= previsouno+preprevisouno
#         previsouno = preprevisouno
#         preprevisouno = c
#         print(previsouno+preprevisouno)
# fib(10)


# def fib(n):
#     previsouno=0
#     preprevisouno =1
#     if (n==1):
#         print(preprevisouno)
#     elif(n==0):
#         print(previsouno)
#     else:
#
#         print(previsouno)
#         print(preprevisouno)
#         for i in range(2,n):
#              c= previsouno+preprevisouno
#              previsouno = preprevisouno
#              preprevisouno = c
#              print(previsouno+preprevisouno)
# fib(1)



# def myFun(**kwargs):
#     for key, value in kwargs.items():
#        print(key,value)
#
#
# # Driver code
# myFun(name='Yusuf', Age=31, Salary=50000)
