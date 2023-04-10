def merge_the_tools(s, k):
    n=len(s)
    for x in range (0,n,k):
        print(rem_dupi(s[x:x+k]))
def rem_dupi(s):
    ans=""
    for x in range(len(s)):
        if s[x] not in ans:
            ans+=s[x]
    return ans


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)