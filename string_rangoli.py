def mul_str(char,len): 
    s=""
    for x in range(len):
        s+=char
    return s
def common(x,n):
    print(mul_str('-',2*(n-x-1))+alpha(x,n)+mul_str('-',2*(n-x-1)))
def alpha(x,n):
    s=""
    for y in range(x):
        s+=chr(n-y+96)+'-'
    s+=chr(n-x+96)
    for z in range(x,0,-1):
        s+='-'+chr(n-z+96+1)
    #s=s[:-1]
    return s
def print_rangoli(n):
    for x in range(n):
        common(x,n)
    for x in range(n-2,-1,-1):
        common(x,n)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
	
----------------------
def common(x,n):
    print(alpha(x,n).center(4*n-3,'-'))
def alpha(x,n):
    s=""
    for y in range(x):
        s+=chr(n-y+96)+'-'
    s+=chr(n-x+96)
    for z in range(x,0,-1):
        s+='-'+chr(n-z+96+1)
    return s
def print_rangoli(n):
    for x in range(n):
        common(x,n)
    for x in range(n-2,-1,-1):
        common(x,n)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)