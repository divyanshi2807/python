#using recursion print numbers from 1 to n
def number(n):
    if n==0:
        return
    number(n-1)
    print(n)
n=int(input("number:"))
print(number(n))