        
if __name__ == '__main__':
    s = input()
    l=len(s)
    for x in range(l):
        if (s[x].isalnum()):
            print("True")
            break
    else:
        print("False")
    for x in range(l):
        if (s[x].isalpha()):
            print("True")
            break
    else:
        print("False")
    for x in range(l):
        is_equal=False
        if (s[x].isdigit()):
            print("True")
            break
    else:
        print("False")
    for x in range(l):
        if (s[x].islower()):
            print("True")
            break
    else:
        print("False")
    for x in range(l):
        if (s[x].isupper()):
            print("True")
            break
    else:
        print("False")
    