#write a recursive function to find  x raised to the power n
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)
x = int(input("Enter base:"))
n = int(input("Enter exponent:"))
print( power(x,n))