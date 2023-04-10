def minion_game(s):
    ss="Draw"
    k=0
    st=0
    l=len(s)
    for x in range(l):
        if s[x]=='a' or s[x]=='e' or s[x]=='i' or s[x]=='o' or s[x]=='u'or s[x]=='A' or s[x]=='E' or s[x]=='I' or s[x]=='O' or s[x]=='U':
            k+=l-x
        else:
            st+=l-x
    if k > st:
        print( "Kevin "+str(k))
    elif st > k:
        print( "Stuart "+str(st))
    else:
        print( ss)

if __name__ == '__main__':
    s = input()
    minion_game(s)