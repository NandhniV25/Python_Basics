if __name__ == '__main__':
    N = int(input())
    l=[]
    for x in range(N):
        a=input()
        #print("test",a)
        l2=a.split(' ')
        #print(l)
        if(l2[0]=='insert'):
            l.insert(int(l2[1]),int(l2[2]))
        elif(l2[0]=='append'):
            l.append(int(l2[1]))  
        elif(l2[0]=='print'):
            print(l) 
        elif(l2[0]=='remove'):
            l.remove(int(l2[1]))
        elif(l2[0]=='sort'):
            l.sort()
        elif(l2[0]=='pop'):
            l.pop()
        elif(l2[0]=='reverse'):
            l.reverse()          