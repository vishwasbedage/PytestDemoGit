
def Prime(num):
    Prime = True

    for i in range(2,num):
        if (num%i ==0):
            Prime = False
            break
    if Prime:
        print("The number is Prime")
    else:
        print("The number is not Prime")

num = int(input("Enter the number"))
Prime(num)

