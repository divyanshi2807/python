A = int(input("Enter base A: "))
B = int(input("Enter exponent B: "))
result = 1
i = 0

while i < B:
    result = result * A
    i += 1

print("Result:", result)
