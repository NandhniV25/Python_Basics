def cube(n):
    sum=0
    for x in range(1,n+1):
        sum = pow(x,3) + sum
    print("sum of cube of",n,"=",sum)
n = int(input("Enter number = "))
cube(n)