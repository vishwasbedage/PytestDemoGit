
# class MyClass:
#     def myfunc(self):
#         pass
#
#     def display(self):
#         print("John")
#
#     def display1(self,name):
#         print(name)
#
# mc1 = MyClass()
# mc1.myfunc()
# mc1.display()
# mc1.display1("Vishu")


# class MyClass:
#     def m1(self):
#         print("THis is instnt method")        ## we can Invoke through object only
#
#     @staticmethod                    ## Static method invoke directly by class itself
#     def m2(self,num):
#         print(self,num)

# mc = MyClass()
# mc.m1()
# mc.m2(100,200)
#
# MyClass.m2(10,30)        ### we can call directly through class

i,j = 100,200
# class Myclass:
#     a,b = 10,20
#     def add(self,x,y):
#         print(x+y)         ## x y are local varibable
#         print(self.a+self.b)      ## classs variable
#         print(i+j)       ### global varible
#
# mc = Myclass()
# mc.add(1000,2000)



# class Myclass:
#     def __int__(self,eid,ename,esal):
#         self.eid = eid
#         self.ename = ename
#         self.esal = esal
#
#     def __str__(self):
#         return (self.ename,self.esal)
#
# mc = Myclass(100,"Vishwas",40000)
# print(mc)





