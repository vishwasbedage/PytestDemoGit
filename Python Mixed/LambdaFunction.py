
### Basic Syntax
## Regular function
# def add(x,y):
#     return x+y
#
# ## Equivalent lambda function
# lambda_add = lambda x,y:x+y
#
# ## Using both function
# result_regular_add = add(5,9)
# result_lambda_add = lambda_add(10,20)
#
# print("Regular function result :",result_regular_add)
# print("Lambda function result :",result_lambda_add)

## 2 Sorting with Lambda
## List of Tuples
students = [("Alice",25),("Bob",30),("Charlie",22)]
sorted_students = sorted(students,key=lambda student:student[1])

print("Sorted students by age",sorted_students)



