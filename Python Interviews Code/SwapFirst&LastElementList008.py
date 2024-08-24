
# mylist = [10,20,60,40,30,70]
# print("Before SWap")
# print(mylist)
#
# mylist[0],mylist[-1] = mylist[-1],mylist[0]
# print("After Swap")
# print(mylist)

##----------------------------------------

# mylist = [10,20,60,40,30,70]
# print("Before SWap")
# print(mylist)
#
# first = mylist.pop(0)
# last = mylist.pop(-1)
#
# mylist.insert(0,last)
# mylist.append(first)
# print("After SWap")
# print(mylist)

##----------------------------------------

# myList = [10, 20, 65, 86, 34, 12]
# print("Before swap")
# print(myList)
#
# temp = myList[0]
# myList[0] = myList[-1]
# myList[-1] = temp
#
# print("After swap")
# print(myList)

##----------------------------------------

# myList = [10, 20, 65, 86, 34, 12]
# print("Before swap")
# print(myList)
#
# get = (myList[-1], myList[0])
# myList[0], myList[-1] = get
#
# print("After swap")
# print(myList)

# ---------------------approach 5---------------------
# myList = [10, 20, 65, 86, 34, 12]
# print("Before swap")
# print(myList)
#
# start, *middle, end = myList
# myList = [end, *middle, start]
# print("After swap")
# print(myList)





