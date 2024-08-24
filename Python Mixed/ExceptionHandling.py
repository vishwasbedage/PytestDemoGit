

# a=10
# b=20
# # print(s)
# print(a$b)




# amount = 10000
# #
# # # check that You are eligible to
# # # purchase Dsa Self Paced or not
# if(amount > 2999)
# print("You are eligible to purchase Camera")


# Python code after removing the syntax error
# string = "Python Exceptions"
#
# for s in string:
#     if (s != o:
#     print( s)



# initialize the amount variable
# marks = 10000
#
# # perform division with 0
# a = marks / 0
# print(a)


# Python code after removing the syntax error
# string = "Python Exceptions"
# #
# for s in string1:
#     if ('s' != 'o'):
#         print(s)    #NameError

# def Arith(a,b):
#     print(a+b)
#     print(a-b)
#     print(a/b)
#     print(a*b)
#     print("All Done")
#
# Arith(40,0)


# a = 5
# b = 0
# print(a / b)


# try:
#     a=5
#     b=0
#     print(a/b)
# except:
#     print("exceptioon mila hai bhai aage ka dekh")
# print("bahar ka print statemnt")


# try:
#     a=5
#     b=0
#     print(a/b)
# except:
#     print("Kuch to exception error hoga")
# print("bahar ka print statemnt")

# try:
#     a=15
#     b=5
#     print(a/b)
# except:
#     print("Kuch to exception error hoga")
# print("bahar ka print statemnt")

# try:
#     def Arith(a,b):
#             print(a+b)
#             print(a-b)
#             print(a/b)
#             print(a*b)
#             print("All Done")
#     Arith(40,0)
# except:
#     print("Exception found")
# print("bahar ka print statemnt")

#
# try:
#     x = int(input())
#     y = int(input())
#     a = int(input())
#     b = int(input())
#     c= 50
#     print(c)
#     print(x+y)
#     print(a/b)
#
# except TypeError:
#   print("Error: cannot add an int and a str")
#
# except ValueError:
#   print("Error: cannot enter  a string with x and y")
#
# except ZeroDivisionError:
#   print("Error: cannot divide any value by 0")
#



# even_numbers = [2, 4, 6, 8]
# print(even_numbers[5])

# try:
#
#   even_numbers = [2, 4, 6, 8]
#   print(even_numbers[5])
# #
# #
# except ZeroDivisionError:
#   print("Denominator cannot be 0.")
# #
# except IndexError:
#   print("Index Out of Bound.")
#
# # Output: Index Out of Bound

# Program to depict else clause with try-except
# Python 3
# Function which returns a/b
# def AbyB(a , b):
#   try:
#      c = ((a+b) / (a-b))
#   except ZeroDivisionError:
#      print ("a-b cant be 0")
#   else:
#      print (c)
#
# # Driver program to test above function
# AbyB(2.0, 3.0)
# AbyB(6.0, 3.0)
# AbyB(9.0, 9.0)

# try:
#     print('try block:-')
#     x=int(input('Enter a number: '))
#     y=int(input('Enter another number: '))
#     z=x/y
# except ZeroDivisionError:
#     print("except ZeroDivisionError block")
#     print("Division by 0 not accepted")
# except ValueError:
#   print("except ValueError block")
#   print("x or y cant be string")
#
# else:
#     print("else block")
#     print("Division = ", z)
# finally:
#     print("finally block")
#
# print ("Out of try, except, else and finally blocks." )

#

# Python program to demonstrate finally

#
# try:
#   k = 5//0 # raises divide by zero exception.
#   print(k)
#
# # handles zerodivision exception
# except ZeroDivisionError:
#   print("Can't divide by zero")
#
# finally:
#   # this block is always executed
#   # regardless of exception generation.
#   print('This is always executed')



#Python code to show how to raise an exception in Python
# num = [3,4, 5, 7]
# if len(num) > 3:
# #
#     raise Exception( f"Length of the given list must be less than or equal to 3 but It is {len(num)}" )
#
# # Program to depict Raising Exception

# try:
#   raise NameError("Hi there") # Raise Error
# except NameError:
#   print ("An exception")


# x = -1
#
# if x < 0:
#   raise Exception("Sorry, no numbers allowed less than zero")


# try:
#     x = -1
#     if x < 0:
#         raise Exception("Sorry, no numbers below zero")
#
# except:
#     print("Exception")




# try:
#     x=int(input('Enter a number upto 100: '))
#     if x > 100:
#         raise ValueError(x)
# except ValueError:
#     print(x, "is out of allowed range")
# else:
#     print(x, "is within the allowed range")

