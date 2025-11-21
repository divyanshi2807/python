def count(n):
    if n < 10:
        return 1
    
    return 1 + count(n // 10)
num = int(input("number: "))
print(count(num))