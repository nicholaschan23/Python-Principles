'''
Anagrams
Two strings are anagrams if you can make one from the other by rearranging the letters.

Write a function named is_anagram that takes two strings as its parameters. 
Your function should return True if the strings are anagrams, and False otherwise.

For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.
'''
def is_anagram(str1, str2):
    if len(str1) is not len(str2):
        return False
    
    alphabet = [0] * 26
    for letter in str1:
        index = ord(letter.lower()) - ord('a')
        alphabet[index] = alphabet[index] + 1
        
    for letter in str2:
        index = ord(letter.lower()) - ord('a')
        alphabet[index] = alphabet[index] - 1
        
    for letter in alphabet:
        if letter != 0:
            return False
    return True