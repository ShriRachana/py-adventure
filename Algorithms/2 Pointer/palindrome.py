"""
Write a function that takes a string s as input and checks whether it’s a palindrome or not.
Note: A phrase, word or sequence is a palindrome that reads the same backwards as forwards.
Constraints:
1 . 1<= s.length <= (2*10^5)
2. The string won’t have any spaces and will only consist of ASCII characters.
"""
def is_palindrome(s):
    left = 0 
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left = left + 1
        right = right - 1
    return True

#Driver Code

def main():
    test_cases = ["RACECAR", "A", "ABC", "ABCBA", "ABBA", "1221", "12"]
    for i in range (len(test_cases)):
        print("Test Case #", i + 1)
        print("\tThe input string is '", test_cases[i], "' and the length of the string is ", len(test_cases[i]), ".", sep='')
        print("\tIs it a palindrome?.....", is_palindrome(test_cases[i]))

if __name__ == '__main__':
    main()

        