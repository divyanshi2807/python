#sum of first n natural number
def count(n):
    if (n==1):
        return 1
    else:
        return n+count(n-1)
n=int(input()) 
print(count(n))