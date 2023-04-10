def pattern(n):
    for x in range(n):
        for y in range(n-x-1):
            print(" ",end="")
        for z in range(x+1):
            print("* ",end="")
        print("")
    for x in range(n-1):
        for i in range(x+1):
            print(" ",end="")
        for v in range(n-x-1):
            print("* ",end="")

        print("")
n = 10
pattern(n)
