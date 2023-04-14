s=input()
prev=s[0]
count=1
for x in range(1,len(s)):
    if s[x]==s[x-1]:
        count+=1  
    else:
        print("(",count,", ",prev,")",end=" ",sep="")
        prev=s[x]
        count=1
print("(",count,", ",prev,")",sep="")