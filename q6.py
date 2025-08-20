A = int(input("Enter a positive integer A: "))
i = 1
even_sum = 0
while i <= A:
    if i % 2 == 0:
        even_sum += i
    i += 1
print("Sum of even numbers:", even_sum)
