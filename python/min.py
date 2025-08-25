A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
C = int(input("Enter third number: "))

if A <= B and A <= C:
    minimum = A
elif B <= A and B <= C:
    minimum = B
else:
    minimum = C

print("Minimum is:", minimum)