def square(n):
    sum=0
    for x in range(1,n+1):
        sum = pow(x,2) + sum
    print("sum of square of",n,"=",sum)
n = int(input("Enter number = "))
square(n)