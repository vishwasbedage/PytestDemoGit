
## List Declaration
# list1 = [1,2,"Python",True,15.9,"Program"]
# list2 = ["anny","riya","dhiraj","Suraj","Program"]
#
# print(list1)
# print(list2)
#
# print(type(list1))
# print(type(list2))



# CredenceT1819= [101,"Yusuf",90000,"Pune","CSE"]
# list1 = [1, 2, "Python", "Program", 15.9]
# list2 = ["Amy", "Ryan", "Henry", "Emma"]
# list3 = [101,102,103]
# a=10
# # #
# # # # printing the list
# print(CredenceT1819)
# print(list1)
# print(list2)
# print(list3)
# print(a)
# # #
# # # # printing the type of list
# print(type(CredenceT1819))
# print(type(list1))
# print(type(list2))
# print(type(list3))
# print(type(a))
#

# list1 = [12, 14, 16, 18, 20]
# print(list1)
# print(list1*5)
#
# list1= (list1*5) # it will update list1 becz LISTS are Mutable Data Type.
# print(list1)

# ct18 = list1 * 5
# print(ct18)
# print(type(list1))
# print(type(ct18))
#
# list1 = [12, 14, 16, 18, 20]
# list2 = [9, 10, 32, 54, 86]
# print(list1)
# print(list2)
# #
# # # concatenation operator +
# list3 = list1 + list2
# print(list3)

# list1 = [12, 14, 16, 18, 20, 23, 27, 39, 40]
# # # # finding length of the list
# print(len(list1))


# list1 = [100, 200, 300, 400, 500]
# # true will be printed if value exists
# # and false if not
#
# print(600 in list1)
# print(700 in list1)
# print(1040 in list1)
# #
# print(300 in list1)
# print(100 in list1)
# print(500 in list1)
# #
# print(600 not in list1)
# print(700 not in list1)
# print(1040 not in list1)
# #
# print(300 not in list1)
# print(100 not in list1)
# print(500 not in list1)



# a = [ 1, 2, "Ram", 3.50, "Rahul", 5, 6 ]
# b = [ 1, 2, 5, "Ram", 3.50, "Rahul", 6 ]
# print(a == b)
# # # #
# a = [ 1, 2, "Ram", 3.50, "Rahul", 5, 6]
# b = [ 1, 2, "Ram", 3.50, "Rahul", 5, 6]
# print(a == b)

# List Slicing



# emplist = [101,"Yusuf",90000,"Pune","CSE"]
# print(emplist[0])
# print(emplist[1])
# print(emplist[2])
# print(emplist[3])
# print(emplist[4])
# print(emplist[5])
# print(emplist[6])

# my_list = [1, 2, 3, 4, 5]
# # #
# print(my_list[:])
# print(emplist[:])
# print(emplist[0:])
# print(emplist[2:])
# print(emplist[:3])
# print(emplist[2:4])
# print(emplist[::1])
# print(emplist[::2])
# print(emplist[::3])
# print(emplist[::4])
# print(emplist[::5])

# negative indexing example
# print(emplist[-1])
# print(emplist[-2])
# print(emplist[-3])
# print(emplist[-4])
# print(emplist[-5])

# print(emplist[-3:])
# print(emplist[:-3])
# print(emplist[-3:-1])
# print(emplist[::-1])
#
# print(emplist[::-2])
# print(emplist[::-3])
# print(emplist[::-4])
# print(emplist[::-5])

# Lst = [50, 70, 30, 20, 90, 10, 60, 90]
# #
# # # Display list
# print(Lst[-7::1])
# print(Lst[-7::-1])
# print(Lst[7::-1])
# print(Lst[7::-1])
# print(Lst[1:5])

# List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# #
# # # Show original list
# print("\nOriginal List:\n", List)
# #
# print("\nSliced Lists [3:9:2] : ")
# #
# # # Display sliced list
# print(List[3:9:2])
# # #
# # # # Display sliced list
# print(List[::2])
# # #
# # # # Display sliced list
# print(List[::])

# emplist = [101,"Yusuf",90000,"Pune","CSE"]
# print(emplist)
# emplist[2]= 190000
# emplist[3]= "Solapur"
# print(emplist)



# emplist[-1] = "Entc"
# print(emplist)

#
# emplist[1:3] = ["Poonam",98000]
# print(emplist)
# #
# emplist[1:3] = [98000,"Poonam"]
# print(emplist)

# emplist[-3:-1] = [80000,"Kolhapur"]
# print(emplist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# print(thislist)
# # #
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)
# #
# thislist = ["apple", "banana", "cherry"]
# print(thislist)
# # # # # #
# # #
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# # print(thislist)
# # thislist[1:3] = ["watermelon"]
# # print(thislist)
# #
# thislist[2:4] = ['a', 'b', 'c', 'd']
# print(thislist)   # ['apple', 'banana', 'a', 'b', 'c', 'd']
# thislist[:-1] = []
# print(thislist)



#
# # Initialize list
# List1 = ["Yusuf", 2, 3, 4, 5, 6, 7, 8, 9]
# List2 = ["Tushar",11,12,13,14,15]
# # #
# # # # Show original list
# print("\nOriginal List1:\n", List1)
# print("\nOriginal List2:\n", List2)
# #
# List3=List1+List2
# print("\nConcatinated List3:\n",List3)
#
# print("\nSliced Lists: ")
# #
# # # Creating new List
# newList = List1[:3] + List2[3:]
# print(newList)
#
# newList = List1[0:1] + List2[0:1]
# #
# # # # Display sliced list
# print(newList)
# #
# # # Changing existing List
# List = List1[::2] + List2[1::2]
# #
# # # Display sliced list
# print(List)

#####------------------------------------------------------------------------


### Updating list by append
# animals list

# animal = ["cat","dog","rabbit"]
#
# animal.append("Fox")
# print("Unpdated List:",animal)


# animals = ['cat', 'dog', 'rabbit']
# # Add 'guinea pig' to the list
# animals.append(dog)
# print('Updated animals list: ', animals)


# animals = ['cat', 'dog', 'rabbit']
# # list of wild animals
# wild_animals = ['tiger', 'fox']
# # appending wild_animals list to animals
# animals.append(wild_animals)
# print('Updated animals list: ', animals)

###----------------------------------------------------------------
#### copy
# mixed list
# my_list = ['cat', 0, 6.7]
# # copying a list
# new_list = my_list.copy()
# print('Copied List:', new_list)

###List copy using =
# We can also use the  = operator to copy a  list.
# For example,
# old_list = [1, 2, 3]
# new_list = old_list
#
# print(new_list)

###-------------------------------------------------------
# shallow copy using the slicing syntax
# mixed list
# list = ['cat', 0, 6.7]
#
# # copying a list using slicing
# new_list = list[:]
#
#
# # Adding an element to the new list
# new_list.append('dog')

# Printing new and old list
# print('Old List:', list)
# print('New List:', new_list)

####-----------------------------------------------------------

# 4.count()
#
# Definition and Usage
# The count() method returns the number of elements with the specified value.
#
# Syntax
# list.count(value)


# create a list
# numbers = [2, 3, 5, 2, 11, 2, 7]
# # check the count of 2
# count = numbers.count(2)
# print('Count of 2:', count)
#
# num = [1,2,3,3,4,5,5,5,6,7,8,6,4,3]
# count = num.count(5)
# print(count)


# vowels = ["a","e","i","o","u"]
#
# count = vowels.count("e")
# print(count)


# 5. extend()
# The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
# Example
# create a list
# odd_numbers = [1, 3, 5]
# # create another list
# numbers = [1, 4]
# # add all elements of prime_numbers to numbers
# numbers.extend(odd_numbers)
# print('List after extend():', numbers)
#
# numbers.append(odd_numbers)
# print(numbers)

# Example 2: Add Elements of Tuple and Set to List
# languages list
# languages = ['French']
#
# # languages tuple
# languages_tuple = ('Spanish', 'Portuguese')
#
# # languages set
# languages_set = {'Chinese', 'Japanese'}
#
# # appending language_tuple elements to language
# languages.extend(languages_tuple)
# print('New Language List:', languages)

# appending language_set elements to language
# languages.extend(languages_set)
#
#
# print('Newer Languages List:', languages)


# Python extend() Vs append()
# If you need to add an element to the end of a list, you can use the append() method.
# a1 = [1, 2]
# a2 = [1, 2]
# b = (3, 4)
# a1.extend(b)
# print(a1)
# #
# a2.append(b)
# print(a2)


# 6.index()
#
# The index() method returns the index of the specified element in the list.
# Example
# animals = ['cat', 'dog', 'rabbit', 'horse']
# # get the index of 'dog'
# index = animals.index('dog')
# print(index)


### Example 3: Working of index() With Start and End Parameters
# alphabets list
# alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']
#
# # index of 'i' in alphabets
# index = alphabets.index('e')   # 1
#
# print('The index of e:', index)
#
# # 'i' after the 4th index is searched
# index = alphabets.index('i', 4)   # 6
#
# print('The index of i:', index)

# # 'i' between 3rd and 5th index is searched
# index = alphabets.index('i', 3, 5)   # Error!
#
# print('The index of i:', index)


# 8.pop()
# The pop() method removes the item at the given index from the list and returns the removed item.
# Example
# create a list of prime numbers
# prime_numbers = [2, 3, 5, 7]
# # remove the element at index 2
# removed_element = prime_numbers.pop(2)
# print('Removed Element:', removed_element)
# print('Updated List:', prime_numbers)


# Example 1: Pop item at the given index from the list
# programming languages list
# languages = ['Python', 'Java', 'C++', 'French', 'C']
# # remove and return the 4th item
# return_value = languages.pop(3)
# print('Return Value:', return_value)
# # Updated List
# print('Updated List:', languages)


# 9.remove()
# The remove() method removes the first matching element (which is passed as an argument) from the list.
# Example
# create a list
# prime_numbers = [2, 3, 5, 7, 9, 11]
# # remove 9 from the list
# prime_numbers.remove(9)
#
# # Updated prime_numbers List
# print('Updated List: ', prime_numbers)


# Example 2: remove() method on a list having duplicate elements
# If a list contains duplicate elements, the remove() method only removes the first matching element.
# animals list
# animals = ['cat', 'dog', 'dog', 'guinea pig', 'dog']
#
# # 'dog' is removed
# animals.remove('dog')
# # Updated animals list
# print('Updated animals list: ', animals)


# 11.sort()
# The sort() method sorts the items of a list in ascending or descending order.
# Example
# prime_numbers = [11, 3, 7, 5, 2]
#
# # sorting the list in ascending order
# prime_numbers.sort()
# print(prime_numbers)


# sort() Syntax
# The syntax of the sort() method is:
# list.sort(key=..., reverse=...)
# Alternatively, you can also use Python's built-in sorted() function for the same purpose.
# sorted(list, key=..., reverse=...)
# Note:The simplest difference between sort() and sorted() is: sort() changes the list directly and doesn't
# return any value, while sorted() doesn't change the list and returns the sorted list.

# sort() Parameters
# By default, sort() doesn't require any extra parameters. However, it has two optional parameters:
# reverse - If True, the sorted list is reversed (or sorted in Descending order)
# key - function that serves as a key for the sort comparison

# sort() Return Value
# The sort() method doesn't return any value. Rather, it changes the original list.
# If you want a function to return the sorted list rather than change the original list, use sorted().

# Example 1: Sort a given list
# vowels list
# vowels = ['e', 'a', 'u', 'o', 'i']
# # sort the vowels
# vowels.sort()
# # print vowels
# print('Sorted list:', vowels)

### Descending order
# The sort() method accepts a  reverse parameter as an optional argument.
# reverse = True sorts the list in the descending order.
# list.sort(reverse=True)
# Alternatively for sorted(), you can use the following code.
# sorted(list, reverse=True)

# Example 2: Sort the list in Descending order
# vowels = ['e', 'a', 'u', 'o', 'i']
# # sort the vowels
# vowels.sort(reverse=True)
# # # print vowels
# print('Sorted list (in Descending):', vowels)



# vowels = ['e', 'a', 'u', 'o', 'i']
# print("Orginal list ",vowels)
#
# vowels.sort()
# print("Orignal list after sort ascending order ",vowels)
#
# vowels.sort(reverse=True)
# print("original list sorted reverse descinding oredr", vowels)


