
# Different types of tuples
# Empty tuple
# my_tuple = ()
# print(my_tuple)
# Tuple having integers
 
# my_tuple = (2,4,6,8)
# print(my_tuple)
# print(type(my_tuple))

# tuple with mixed datatypes
# my_tuple = (1, "Hello", 3.4)
# print(my_tuple)

# nested tuple
# my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
# print(my_tuple)

# var1 = ("Hello") # string
# var2 = ("Hello",) # tuple
# print(var1)
# print(var2)
# print(type(var1))
# print(type(var2))


# a = (1,2,1,3,1,3,1,2,1,4,1,5,1,5)
# print(a.count(1))
# print(a.index(5))
# abc=("Yusuf","Amit","Pooja","raj", "Pritesh","Priya","Yusuf")
# print(abc.count("Yusuf"))
# print(abc.index("Yusuf"))
# print(abc.index("Yusuf",1,7))
# print(abc.index("Yusuf",-7,-1))
# print(abc.index("Yusuf",-1,-7))



# my_tuple= (101,"Yusuf",90000,"Pune","CSE")
# print(my_tuple)
# print(type(my_tuple))
#
# my_tuple1 = ()
# print(my_tuple1)
# print(type(my_tuple1))

# my_tuple2 = (1, 2, 3)
# print(my_tuple2)
#
# # tuple with mixed datatypes
# my_tuple3 = (1, "Hello", 3.4)
# print(my_tuple3)

# # nested tuple
# my_tuple4 = ("mouse", [8, 4, 6], (1, 2, 3))
# my_tuple5 = ("Abc", (8, 4, 6), ["yusuf","Amit"])
# #
# print(my_tuple4)
# print(my_tuple5)

# My_tuple = 1,2,3
# print(My_tuple)
# print(type(My_tuple))




# My_list = 1,2,3
# print(My_list)
# print(type(My_list))

# #
# my_tuple = 1, "Hello", 3.4
# print(my_tuple)
# # #
# abc = 1, "Hello", 3.4
# print(abc)
#
# var1 = ("Hello")
# print(type(var1))  # <class 'str'>
# #
# # # Creating a tuple having one element
# var2 = ("hello",)
# print(type(var2))  # <class 'tuple'>
# #
# # # Parentheses is optional
# var3 = "hello",
# print(type(var3))  # <class 'tuple'>
# # #
# add_one_ele_tuple= (105,)
# print(type(add_one_ele_tuple))
#

# tuple1 = (101, 102, 103)
# tuple2=  (104, 105, 106)
# tuple3= tuple1+tuple2
# print(tuple3) # Prints (101, 102, 103, 104, 105, 106)
#
# tuple1 = (101, 102, 103) + (104, 105, 106)
# print(tuple1)
# Prints (101, 102, 103, 104, 105, 106)
#
# T = ('red', 'green', 'blue') + (1, 2, 3)
# print(T)
# # Prints ('red', 'green', 'blue', 1, 2, 3)
#
# print(tuple1+T)
# # Prints (101, 102, 103, 104, 105, 106, 'red', 'green', 'blue', 1, 2, 3)
#
# tuple2=tuple1+T
# print(tuple2)
# # Prints (101, 102, 103, 104, 105, 106, 'red', 'green', 'blue', 1, 2, 3)

# T = ('red') * 3  # ye string hai
# print(T)

# T = ('red',) * 3
# print(T)
# # Prints ('red', 'red', 'red')
#
# T = ('red', 'Green')
# T1= (T * 3)
# print(T1)
#
# T = ('red', 'Green')
# T= (T * 3)
# print(T)
#
# T = ('red', 'Green')
# print((T * 3))


# # Prints ('red', 'Green', 'red', 'Green', 'red', 'Green')

# T = ('red', 'green', 'blue')
# print("red" in T)
# print("red" not in T)
# print("yellow" in T)
# print("yellow" not in T)



# tuple1 = (12, 14, 16, 18, 20, 23, 27, 39, 40)
# # # # finding length of the tuple
# print(len(tuple1))

# T = ('red', 'green', 'blue')
# T[0] = 'black' # Its a immutable data type -- hence error
# print(T)

# tuple1 = (0, 1, 2, 3)
# tuple1[0] = 4
# print(tuple1)

# T = ('red', 'green', 'blue', 'yellow', 'black')
# # #
# print(T[0])
# # # # Prints red
# # #
# print(T[2])
# # # # Prints blue
# # #
# print(T[-1])
# # # # Prints black
# print(T[-2])
# # # Prints yellow

# tup1 = ('physics', 'chemistry', 1997, 2000);
# tup2 = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100,110,120 );
# print ("tup1[0]: ", tup1[0])
# print ("tup2[1:5]: ", tup2[1:5])
# print ("tup2[1:5:1]: ", tup2[1:5:1])
# print ("tup2[1:5:2]: ", tup2[1:5:2])
# #
# print ("tup2[1:10:2]: ", tup2[1:10:2])

#
T = ('a', 'b', 'c', 'd', 'e', 'f')
#
# print(T[2:5])
# # # Prints ('c', 'd', 'e')
# #
# print(T[0:2])
# # # Prints ('a', 'b')
#
# #
# print(T[3:-1])
# # Prints ('d', 'e')
#
# tuple1 = (0 ,1, 2, 3)
# print(tuple1[1:])
# print(tuple1[::-1])
# print(tuple1[2:4])

# my_tuple = ('c', 'r', 'e', 'd', 'e', 'n', 'c', 'e')
# # # elements beginning to end
# print(my_tuple) # Prints ('c', 'r', 'e', 'd', 'e', 'n', 'c', 'e')
# print(my_tuple[:]) # Prints ('c', 'r', 'e', 'd', 'e', 'n', 'c', 'e')


# T = ('red', 'green', 'blue')
# print(T)
# del T # pura tuple delete krega
# print(T)

#
# tuple3 = ( 0, 1)
# del tuple3
# print(tuple3)

# t = ('red', 'green', 'blue')
# del(t[0])
# print(t)
# Tuple not Supports deletion Updation ---IMMutable

# a = ['red', 'green', 'blue']
# del a[0]
# print(a)
# #List Supports deletion Updation ---Mutable


T = ('red', 'green', 'blue', 'cyan')  #Packing
(a, b, c, d) = T   # Unpacking
# #
# print(a)
# # # Prints red
# #
# print(b)
# # # Prints green
# #
# print(c)
# # # Prints blue
# #
# print(d)
# # # Prints cyan

# T = ('red', 'green', 'blue', 'cyan')  #Packing
# (a, b, c) = T   # Unpacking
# print(a)

# T = ('red', 'green', 'blue')  #Packing
# (a, b, c, d) = T   # Unpacking
# print(a)


# a = (1,2,1,3,1,3,1,2,1,4,1,5,1,5)
#
# abc=("Yusuf","Amit","Pooja","raj", "Pritesh","Priya","Yusuf")
# print(abc.count("Yusuf"))
# print(abc.index("Yusuf"))
# print(abc.index("Yusuf",1,7))
# print(abc.index("Yusuf",-7,-1))
# print(abc.index("raj",-7,-1))
# print(abc.index("Amit",-7,-1))
#
# print(abc.index("Yusuf",-1,-7))

# tup = (22, 3, 45, 4, 2.4, 2, 56, 890, 1)
# # #
# print(max(tup))
# print(min(tup))
# print(sum(tup))
#
# tup2 = ("Yusuf","yusuf")
#
# print(max(tup2))
# print(min(tup2))

# abc = (5, 2, 24, 3, 1, 6, 7)
# print(sorted(abc))
# print(type((sorted(abc))))  # List me ayaga
#
# print(tuple(sorted(abc)))
# print(type(tuple(sorted(abc)))) # Tuple me ayaga ---syntax thoda hard hai but yad rkhna hoga
# #
#
# a = tuple(sorted(abc))
# print('Sorted Tuple :', a)
# print(type(a))



# abc = (5, 2, 24, 3, 1, 6, 7)
# print(sorted(abc, reverse= True))
# print(type(sorted(abc,reverse= True))) # List me ayaga


# abc = (5, 2, 24, 3, 1, 6, 7)
# # print(tuple(sorted(abc, reverse=True)))
# # print(type((tuple(sorted(abc, reverse=True)))))
# #
# sorted_abc = tuple(sorted(abc, reverse=True))
# print('Sorted Tuple :', sorted_abc)
# print(type(sorted_abc))

# ct1819tuple=(10,30,40,20,100,80,90)
# print(sorted(ct1819tuple))
# print(type(sorted(ct1819tuple)))

# ct1819tuple=(10,30,40,20,100,80,90)
# # print(tuple(sorted(ct1819tuple)))
# # print(type(tuple(sorted(ct1819tuple))))
#
# print(tuple(sorted(ct1819tuple, reverse=True)))


# a_list = [1,2,3,4,5]
# print(a_list)
# print(type(a_list))  # list
#
# b_tuple = tuple(a_list)
# print(b_tuple)
# print(type(b_tuple)) #tuple
#


# a_list = tuple(a_list)
# print(a_list)
# print(type(a_list))

# a="Yusuf"
# print(a)
# print(type(a))
# a=tuple(a)
# print(a)
# print(type(a))

#
# a="Yusuf"
# print(a)
# print(type(a))
# a=list(a)
# print(a)
# print(type(a))
#
# a=str(a)
# print(a)
# print(type(a))


# x = ("apple", "banana", "cherry")
# print(x)
# # #
# x= list(x)
# print(x)
# # #
# x[1]="kiwi"
# print(x)
# # #
# x=tuple(x)
# # #
# print(x)
# # #
# print(type(x))

# x = ("apple", "banana", "cherry")
# y = list(x)
# y.append("orange")
# print(y)
# x = tuple(y)
# print(x)


# x = ("apple", "banana", "cherry")
# y = ("orange",)
# x += y
# print(x)

# x = ("apple", "banana", "cherry")
# y = list(x)
# del y[0]
# # print(y)
# x = tuple(y)
# print(x)

# tuple1 = (5, 3, 20, 8, 4, 4, 6, 2)
# print(tuple1)
# print(type(tuple1))
# #
# # #change tuple to list
# list1 = list(tuple1)
# print(list1)
# print(type(list1))
# #
# # #update list
# list1[2] = 63
# print(list1)
# print(type(list1))
# #
# # #change back list to tuple
# tuple1 = tuple(list1)
# #
# print(tuple1)
# print(type(tuple1))

# tuple1 = (5, 3, 2, 8, 4, 4, 6, 2)
#
# #change tuple to list
# list1 = list(tuple1)
#
# #remove an item from list
# list1.remove(8)
#
# #change back list to tuple
# tuple1 = tuple(list1)
#
# print(tuple1)





