rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    if i == 1:
        print("*")
    else:
        print("*" + " _" * (i - 1) + " *")
