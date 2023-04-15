from collections import namedtuple
n=int(input())
arr = input().split()
student=namedtuple("marklist", arr)
sum=0
for x in range(n):
    i=student( * (input().split()) )
    sum=sum+int(i.MARKS)
print(format(sum/n,".2f"))