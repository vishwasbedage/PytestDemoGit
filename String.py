
# city="Ahmadabad"
# print(city)
# print(type(city))
#
# city = "Kolhapur"
# print(city)
# print(type(city))

# a = "Hello"
# b = "World"
# c=  a+b #More sensible way to write a program
# print(c) #HelloWorld
# #
# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)

# a = "Hello"
# b = "World"
# print(a+b) #HelloWorld
#
# a = "Hello"
# b = "World"
# c=  "Python"
# d=a+b+c
# print(d) #HelloWorldPython

# d = a+" "+b +" "+c
# print(d)
# a="Python"
# print(a*10)
#
# a="Python"
# print(a*4)

# print("python\t"*10)
# print("python\n"*10)

# string1= "CREDENCE"
# print(string1)
# # print(string1[0])
# print(string1[1])
# print(string1[2])
# print(string1[7])
# print(string1[8]) # IndexError: string index out of range

String = 'CREDENCEAUTOMATION'
# print(String)
# print(String[0])
# print(String[0:4])
# print(String[:5])
# print(String[5:])
# # print(String[3])
# print(String[0:3])
# print(String[0:8])
#
# print(String[8:18])
# print(String[8:12])
# print(String[8:])
#
# print(String[4:15])
#
# print(String[-2])
# print(String[-1])
# print(String[-3])
# print(String[3:-10])

# print(String[3:-16]) # NO RESULT
# print(String[3:-13]) #Result will be there
# print(String[3:-11])

# print(String[-3:1])
# print(String[-3:17])
# print(String[-3:18])
#
# print(String[-2:-5])
# print(String[-5:-2])

# print(String[0:])
# print(String[8:])
# print(String[:1])
# print(String[:8])
# print(String[-8:])
# print(String[:-8])
# print(String[1:10])
# print(String[0:8:1])
# print(String[0:8:2])
# print(String[0:8:3])
#

# print(String[-1:-12])
# # print(String[-12:-1])
# print(String[-1:-12:-2])
# print(String[-1:-12:-1])
# print(String[-12:-1:2])

# name1='Yusuf'
# print(name1[-1:-6:-1])
# print(name1[-1:-6:-2])

# Prints string in reverse
# print(String[-1:-20:-1])
# print(String[::-1])
# print(String[::-4])

# Copy string to another variable
# copy = String[:]
# print(copy)
# copy = String[0:2]
# print(copy)
# copy = String[0:8]
# print(copy)

# copy = str(String)
# print(copy)

# copy = 'Hey ' + String
# print(copy)

# String[0]= "D"  # immutable
# print(String)

text= "Credence AUTOMATIon testing"
# print(text.capitalize())
# print(text.casefold())
# print(text.lower())
# print(text.upper())
# text1="ABC"
# a="ßABc"
# print(a.casefold())
# print(a.lower())
# print(text1.islower())
# print(text1.isupper())

# First character in each word is
# titlecase and remaining titlecase
# s = 'Credence for Credence'
# print(text.title())
# yusuf
# Yusuf - title
# Yusuf -capitalize
#
# yusuF akshay
#
# Yusuf Akshay - title
# Yusuf akshay - capitalize

# First character in first
# word is titlecase
# s = 'credence For Credence'
# print(s.title())

# Third word has titlecase
# characters at middle
# s = 'Credence For CREDENCE'
# print(s.title())
# print(s.capitalize())

# # Ignore the digit 6041, hence returns True
s = '6041 Is MY number'
# print(s.title())
# print(s.capitalize())

# word has titlecase
# characters at middle
# s = 'cREDENCE IT'
# print(s.title())

# s = 'Credence For Credence'
# print(len(s))

#
# s = 'credence For Credence'
# print(len(s))
# #
# s = 'Credence For CREDENCE'
# print(len(s))
#
# s = '6041 Is My Number'
# print(len(s))
#
#
# s = 'CREDENCE'
# print(len(s))


# First character in each word is
# uppercase and remaining lowercase
# s = 'Credence For Credence'
# print(s.istitle()) #True

# First character in first
# word is lowercase
# s = 'credence For Credence' #False
# print(s.istitle())

# Third word has uppercase
# characters at middle
# s = 'Credence For CREDENCE' # False
# print(s.istitle())
# Ignore the digit 6041, hence returns True
# s = '6041 Is My Number'
# print(s.istitle())  #True

# word has uppercase
# characters at middle
# s = 'CREDENCE'
# print(s.istitle()) # False

# s1 = "Credence"
# print(s1.istitle())  # True

# a=10
# print(isinstance(a,int))
# #
# a= 10
# print(isinstance(a,complex))
# #
# a= 2+3j
# print(isinstance(a,int))
# #
# a= 2+3j
# print(isinstance(a,complex))
#
# s= "abcd"
# print(isinstance(s,str))


String='CredenceAutomation Testing By Yusuf Sir'
#
# print(String.count('u'))
# print(String.count('u',1,10))
# print(String.count('u',10,20))
# print(String.count('Sir'))
# print(String.count('u',9,20))
#
# print(String.endswith("Sir"))
# print(String.endswith("r"))
# print(String.endswith("ing"))
# print(String.endswith("sting"))
#
# print(String.find('A'))
# print(String.find('Aut'))
# print(String.find('Autom'))
# print(String.find('Automation'))
# print(String.find('e'))
# print(String.find('E'))

# text="CREDENCEAUTOMATION"
# print(text.find('A',0))
# print(text.find('A',11))
# print(text.find('A',2,3))





String= "CREDENCEAUTOMATION"
# print(String.index('A'))
# print(String.find('A'))
# print(String.find('Z'))
# print(String.index('Z'))
# print(String.index('A',1))
# print(String.index('A',9))
# print(String.index('A',10))
# print(String.index('A',20,30))


# String1="Credence"
# print(String1.isalnum()) #-- True
# # #
# String1="123ACS"
# print(String1.isalnum()) #-- True
# #
# String1 = 'Credence Automation 123 TesTiNG'
# print(String1.isalnum()) #—false becz of space
# #
# String1 = 'Credence_Automation_TesTiNG'
# print(String.isalnum())  #— false becz of _
#
# String1="Credence"
# print(String1.isalnum())
#
# String = 'Credence_Automation_TesTiNG'
# String1="Credence"
# print(String.isalpha())
# print(String1.isalpha())


# a = "123456789"
# print(a.isdecimal())
# # #
# # # # contains alphabets
# s = "12credence34"
# print(s.isdecimal())
# # #
# # # # contains numbers and spaces
# s = "12 34"
# print(s.isdecimal())
#
#
# s = "12345"
# print(s.isnumeric())
# #
# # # contains alphabets
# s = "12credence34"
# print(s.isnumeric())
# #
# # # contains numbers and spaces
# s = "12 34"
# print(s.isnumeric())
#
# s = "12345"
# print(s.isdigit())
# #
# # # contains alphabets
# s = "12credence34"
# print(s.isdigit())
#
# # contains numbers and spaces
# s = "12 34"
# print(s.isdigit())
#
# s = "0123"
# print(s.isnumeric())
#
# # # contains alphabets
# s = "0123"
# print(s.isdigit())
# #
# # # contains numbers and spaces
# s = "0123"
# print(s.isdecimal())
#
#
#
#
#
#
# s = "2²"
# print(s.isnumeric())
# #
# # # contains alphabets
# s = "2²"
# print(s.isdigit())
# #
# # # contains numbers and spaces
# s = "2²"
# print(s.isdecimal())
#
#
#
# s = "ↁ"
# print(s.isnumeric())
# #
# # # contains alphabets
# # s = "ↁ"
# print(s.isdigit())
# #
# # # contains numbers and spaces
# # s = "ↁ"
# print(s.isdecimal())


# string = "grrks FOR grrks"
#
# # replace all instances of 'r' (old) with 'e' (new)
# new_string = string.replace("r", "e" )
# print(string)
# print(new_string)
# print(string.replace("r","e"))
#
# string = "geeks for geeks \ngeeks for geeks"
#
# print(string)
#
# # Prints the string by replacing only
# #  occurrence of Geeks
# print(string.replace("geeks", "Yusuf"))

# Replace only a certain number of Instances using replace() in Python
# In this example, we are replacing certain numbers of words. i.e. “ek” with “a” with count=3.
#
# string = "geeks for geeks geeks geeks geeks"
#
# # Prints the string by replacing
# # e by a
# print(string.replace("e", "a"))
#
# # Prints the string by replacing only
# # 3 occurrence of ek by a
# print(string.replace("ek", "i", 3))

# Python program to demonstrate the use of
# swapcase() method

string = "gEEksFORgeeks"
# #
# # # prints after swapping all cases
# print(string)
# print(string.swapcase())
# #
# string = "geeksforgeeks"
# print(string.swapcase())
# #
# string = "GEEKSFORGEEKS"
# print(string.swapcase())

# String = "Credence"
# print("$".join(String))
# print(",".join(String))
# print(" ".join(String))
#
# s1 = 'abc'
# s2 = '123'
#
# # each element of s2 is separated by s1
# # '1'+ 'abc'+ '2'+ 'abc'+ '3'
# print('s1 ko join kiya s2 ke sath:', s1.join(s2))
# print('abc name ke string  ko join kiya s2 ke sath:', "abc".join(s2)) # above 2 lines have same meaning.
# # #
# # # # each element of s1 is separated by s2
# # # # 'a'+ '123'+ 'b'+ '123'+ 'b'
# print('s2 ko join kiya s1 ke sath:', s2.join(s1))
# print('123 ko join kiya s1 ke sath:', "123".join(s1))



