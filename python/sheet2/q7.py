A = int(input("Enter a positive integer A: "))
i = 1
odd_sum = 0
while i <= A:
    if i % 2 != 0:
        odd_sum += i
    i += 1
print("Sum of odd numbers:", odd_sum)
