def arm(num):
    count=len(num)
    armstrong=0
    print(count)
    for x in range(count):
        armstrong = pow(int(num[x]),3) + armstrong
    print("armstrong",armstrong)
    if armstrong==int(num):
        print("true")
    else:
        print("false")
n1=input("enter num1")
arm(n1)