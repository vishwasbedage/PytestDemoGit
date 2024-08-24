
# a = 40
# b = 50
# print("Before Swapping --> ",a,b)
# temp = a
# a = b
# b = temp
#
# print("After Swapping -->", a,b)

####--------------------------------------------------------------------------------

# a = 50
# b = 60
# print("Before Swapping",a,b)
#
# a,b = b,a
# print("After Swapping",a,b)

#### -------------------------------------------------------------------

# mylist = [1,2,3,4,5,6]
# mylist1 = []
# for i in mylist:
#     mylist1.append([i**2, i**3])
#
# print(mylist1)

### ---------------------------------------------------------------------

# x = lambda n:[n**2,n**3]
# Mlist = [1,2,3,4,5]
# print(list(map(x,Mlist)))

###3 ----------------------------------------------------

def sumDigit(s):
    num = 0
    sum_num = ""
    sum_chr = ""
    for char in s:
        if char.isdigit():
            num = num + int(char)
            sum_num = sum_num + char + ','
        elif char.isalpha():
            sum_chr = sum_chr + char
    new_str = sum_num[:-1]
    print(num)
    print(new_str)
    print(sum_chr)

s = "Cre3d5e6n8c9e"
sumDigit(s)














