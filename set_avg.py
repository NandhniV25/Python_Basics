def average(arr):
    s=set(arr)
    l=len(s)
    sum=0
    for x in s:
        sum+=x
    avg=sum/l
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)