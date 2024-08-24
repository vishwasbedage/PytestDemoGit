
mylist = ['kiran','dhiraj','chotu','gotya','dhiraj','vishwas','kiran']
element = 'vishwas'
flag = False
for elements in mylist:
    if elements == element:
        flag = True
        break
if flag:
    print(f"{element} is present")
else:
    print(f"{element} is not present")




