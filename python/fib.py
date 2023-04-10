def fib(num):
    for x in range(num):
        a=[0,1]
        if num<=0:
            print("incorrect input")
        if num>2:
            for y in range(2,num):
                a.append(a[y-1]+a[y-2])
        print("fib of {0} th term is {1}".format( num,a[num-1]))
        return a
n = int(input("enter num= "))
print(fib(n))