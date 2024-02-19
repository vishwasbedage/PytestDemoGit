
#
# a=10
# b=20
# print(s)
# print(a+b)




# amount = 10000
#
# # check that You are eligible to
# # purchase Dsa Self Paced or not
# if(amount > 2999)
# print("You are eligible to purchase Camera")


# Python code after removing the syntax error
# string = "Python Exceptions"
#
# for s in string:
#     if (s != o:
#     print(s)



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
#     Arith(50,0)
# except:
#     print("Excection found")


# x = int(input())
# y = int(input())
# a=  int(input())
# b=  int(input())
# try:
#   z = x + y
#   print(z)
#   c = a / b
#   print(c)
#
# except TypeError:
#   print("Error: cannot add an int and a str")
#
#
# except ZeroDivisionError:
#   print("Error: cannot divide any value by 0")




# even_numbers = [2, 4, 6, 8]
# print(even_numbers[5])

# try:
#
#     even_numbers = [2, 4, 6, 8]
#     print(even_numbers[5])
#
#
# except ZeroDivisionError:
#     print("Denominator cannot be 0.")
#
# except IndexError:
#     print("Index Out of Bound.")
#
# # Output: Index Out of Bound

# Program to depict else clause with try-except
# Python 3
# Function which returns a/b
# def AbyB(a , b):
#   try:
#      c = ((a+b) / (a-b))
#   except ZeroDivisionError:
#      print ("b cant be 0")
#   else:
#      print (c)
#
# # Driver program to test above function
# AbyB(2.0, 3.0)
# AbyB(3.0, 3.0)
# AbyB(6.0, 6.0)

# try:
#     print('try block')
#     x=int(input('Enter a number: '))
#     y=int(input('Enter another number: '))
#     z=x/y
# except ZeroDivisionError:
#     print("except ZeroDivisionError block")
#     print("Division by 0 not accepted")
# except ValueError:
#   print("except ValueError block")
#   print("y cant be string")
#
# else:
#     print("else block")
#     print("Division = ", z)
# finally:
#     print("finally block")
#     x=0
#     y=0
# print ("Out of try, except, else and finally blocks." )
#
#

# Python program to demonstrate finally

# No exception Exception raised in try block
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
#

