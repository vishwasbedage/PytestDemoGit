import calendar

## 01
# print("Hello")

## 02

# num1 = float(input("Enter The Value"))
# num2 = float(input("Enter The Value"))
#
# sum_result = num1 + num2
# print(f"sum of two values:",sum_result)

## 03

# num1 = float(input("Enter The First Number"))
# num2 = float(input("Enter the second number"))
#
# if num2 == 0:
#     print("Error:division by zero is not allowd")
# else:
#     div_result = num1/num2
#     print("Division by two numbers is:",div_result)

### 04 Write a Python program to find the area of a triangle.

# base = float(input("length of the base of triangle"))
# height = float(input("Height of triangle"))
#
# area = 0.5 * base * height
#
# print("The Area of Triangle is :",area)


## 05 Write a Python program to swap two variables

# num1 = input("Enter the  first number")
# num2 = input("Enter the second number")
#
# print(f"Original values are:a={num1},b={num2}")
#
# ## swap the values using temporary variable
#
# temp = num1
# num1 = num2
# num2 = temp
#
# print(f"swapped values are:a={num1},b={num2}")

## Write a Python program to swap two variables without temp variable.

# a = 5
# b = 10
# # Swapping without a temporary variable
# a, b = b, a
# print("After swapping:")
# print("a =", a)
# print("b =", b)


## 06 Write a Python program to display calendar.

# import calendar
# year = int(input("Enter the year"))
# month = int(input("Enter the month"))
#
# cal = calendar.month(year,month)
# print(cal)


## 07 Write a Python program to solve quadratic equation.
# The standard form of a quadratic equation is:
# where
# a, b and c are real numbers and
# The solutions of this quadratic equation is given by:
# 𝑎𝑥2 + 𝑏𝑥 + 𝑐 = 0
# 𝑎 ≠ 0
# (−𝑏 ± (𝑏2 − 4𝑎𝑐)1/2)/(2𝑎)

# import math
#
# a = int(input("Enter coeffient of a"))
# b = int(input("Enter coeffient of b"))
# c = int(input("Enter coeffient of c"))
#
# disciminate = b ** 2 - 4*a*c
#
# if disciminate>0:
#     root1 = (-b+ math.sqrt(disciminate))/ (2*a)
#     root2 = (-b- math.sqrt(disciminate))/  (2*a)
#     print(f"root1 :{root1}")
#     print(f"root2 :{root2}")

# elif disciminate == 0:
#     root = -b/(2*a)
#     print(f"root:{root}")
# else:
#  # Complex roots
#  real_part = -b / (2*a)
#  imaginary_part = math.sqrt(abs(disciminate)) / (2*a)
#  print(f"Root 1: {real_part} + {imaginary_part}i")
#  print(f"Root 2: {real_part} - {imaginary_part}i")

### Write a Python Program to Check if a Number is Positive, Negative or Zero.

# num = float(input("enter a number"))
# if num>0:
#     print("Positive number")
# elif num == 0:
#     print("Zero Number")
# else:
#     print("Negative number")


### Write a Python Program to Check if a Number is Odd or Even.

# num = int(input("Enter The number"))
#
# if num%2 == 0:
#     print("This is even number")
# else:
#     print("This is odd number")


### Write a Python Program to Check Leap Year.




