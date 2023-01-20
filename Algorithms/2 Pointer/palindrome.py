def is_palindrome(s):
    left = 0 
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        