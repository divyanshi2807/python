A = int(input("Enter an integer A: "))
original = A

if A < 0:
    print("No")
else:
    reverse = 0
    while A > 0:
        digit = A % 10
        reverse = reverse * 10 + digit
        A = A // 10

    if original == reverse:
        print("Yes")
    else:
        print("No")
