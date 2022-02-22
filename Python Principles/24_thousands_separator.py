'''
Thousands separator
Write a function named format_number that takes a non-negative number as its only parameter.

Your function should convert the number to a string and add commas as a thousands separator.

For example, calling format_number(1000000) should return "1,000,000".
'''
def format_number(num):
    temp = str(num)
    if (len(temp) <= 3):
        return str(num)
        
    start = len(temp) % 3
    output = ""
    if (start != 0):
        output += temp[0:start] + ","
    for i in range(start, len(temp), 3):
        output += temp[i:i + 3] + ","
    return output[:-1]

'''
# DIY solution
def format_number(n):
    result = ""
    for i, digit in enumerate(reversed(str(n))):
        if i != 0 and (i % 3) == 0:
            result += ","
        result += digit
    return result[::-1]

# built-in solution
def format_number(n):
    return "{:,}".format(n)
'''