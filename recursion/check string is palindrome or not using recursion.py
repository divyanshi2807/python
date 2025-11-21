#check string is palindrome or not
def palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])


word = input("")
if palindrome(word):
    print("palindrome")
else:
    print("Not palindrome")