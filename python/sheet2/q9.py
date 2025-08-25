N = int(input("Enter an integer N: "))
sum_digits = 0

if N < 0:
    N = -N

while N > 0:
    digit = N % 10
    sum_digits += digit
    N = N // 10

print("Sum of digits:", sum_digits)
