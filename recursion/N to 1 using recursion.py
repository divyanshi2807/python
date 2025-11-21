def number(n):
    if n == 0:
        return
    print(n)
    number(n - 1)

n = int(input("number:"))
number(n)