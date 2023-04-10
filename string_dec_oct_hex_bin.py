def print_formatted(n):
    l = len(bin(n).lstrip("0b"))
    for x in range(1,n+1):
        print(str(x).rjust(l, " "),end=" ")
        print(oct(x).lstrip("0o").rjust(l, " "),end=" ")
        print(hex(x).lstrip("0x").upper().rjust(l, " "),end=" ")
        print(bin(x).lstrip("0b").rjust(l, " "),end="\n")
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)