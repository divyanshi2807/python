
N = int(input("enter a num: "))
if N < 1:
    print("Please enter a natural number greater than 0.")
else:
    sum = N * (N + 1) // 2
    print("Sum of natural numbers from 1 to", N, "is:", sum)