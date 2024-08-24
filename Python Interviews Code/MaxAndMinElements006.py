#-------------------------Find Maximum Element in Array----------------------

arr = [10,3,5,70,50,4,33]
max = arr[0]

for i in range(0,len(arr)):
    if arr[i] > max:
        max = arr[i]
print(max)

#-------------------------Find Minimum Element in Array----------------------

arr = [20,30,42,60,2,6,3]
min = arr[0]

for i in range(0,len(arr)):
    if arr[i] < min:
        min = arr[i]
print(min)



