

def ends_with_4(num):
    return num % 10 == 4

number = 124
if ends_with_4(number):
    print(f"{number} ends with 4")
else:
    print(f"{number} does not end with 4")

