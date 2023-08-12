# Check if a string is a palindrome
def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string


print(is_palindrome("racecar"))
print(is_palindrome("hello"))