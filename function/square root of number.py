def squarerooot(A):
    root= int(A ** 0.5)
    if root*root==A:
        return root
    else:
        return -1

num = int(input("Enter a number: "))
print(squarerooot(num))