#def fun1(n):
   #print("hello")
   #eturn n*(n+1)/2

#print(fun1(10))

#def fun2(n):
    #sum = 0
    #for i in range(1, n+1):
        #sum += i
        #print("hello")
    #return sum
#print(fun2(10))

def fun3(n):
    sum = 0
    for i in range(1, n+1):
      for j in range(1,i+1):
        print("hello")
        sum += 1
      print("hello")  
    return sum
print(fun3(10))  
