'''
Palindrome
A string is a palindrome when it is the same when read backwards.

For example, the string "bob" is a palindrome. So is "abba". But the string "abcd" is not a palindrome, because "abcd" != "dcba".

Write a function named palindrome that takes a single string as its parameter. 
Your function should return True if the string is a palindrome, and False otherwise.
'''
def palindrome(string):
    for i in range(0, int (len(string)/2)):
        if string[i] is not string[len(string) - 1 - i]:
            return False
    return True