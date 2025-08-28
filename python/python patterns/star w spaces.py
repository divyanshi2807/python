a = int(input("Enter number of rows: "))
b = int(input("Enter number of columns: "))
for i in range(a):
    if b > 1:
        print("* " + "_ " * (b - 2) + "*")
    else:
        print("*")
