N = int(input("Enter an integer N: "))
count = 0

if N == 0:
    count = 1
else:
    if N < 0:
        N = -N

    while N > 0:
        N = N // 10
        count += 1

print("Number of digits:", count)
