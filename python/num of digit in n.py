n=int(input("enter a number"))
digit_count = 0
if (n == 0):
    digit_count = 1
else:
    while (n > 0):
        digit_count += 1
        n //= 10

print("Number of digits:", digit_count)