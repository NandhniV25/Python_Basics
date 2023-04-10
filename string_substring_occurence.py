def count_substring1(string, sub_string):
    l=len(string)
    l1=len(sub_string)
    c=0
    for x in range(l-l1+1):
        all_equal=True
        for y in range(l1):
            if (string[x+y]!=sub_string[y]):
                all_equal=False
        if all_equal:
            c+=1
    return c
def count_substring(string, sub_string):
    l=len(string)
    l1=len(sub_string)
    c=0
    for x in range(l-l1+1):
        if string[x:x+l1] == sub_string:
                c+=1
    return c
def count_substring3(string, sub_string):
    l=len(string)
    l1=len(sub_string)
    c=0
    for x in range(l-l1+1):
        if match_with_substring(string,sub_string,x):
                c+=1
    return c
def match_with_substring(string,sub_string,x):
    l1=len(sub_string)
    for i in range(l1):
        if string[x+i]!=sub_string[i]:
            return False
    return True
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)