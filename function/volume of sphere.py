def sphere(r):
    volume = (4 * 3.14 * (r ** 3)) / 3
    return volume

A = float(input("Enter radius: "))
print(sphere(A))
