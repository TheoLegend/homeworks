from math import sqrt
number=int(input("enter no to check prime or not"))

if number>1:
    for i in range(2,int(sqrt(number))+1):
        if(number%i==0):
            print("it is no prime")
            break
    else:
                    print("no is prime")

else:
    print("no i not prime")                