'''
Solution to the first exercise.

args:
    string: alphanumeric characters

returns:
   sum of the numeric digits in the alphanumeric string

Example:
>>> numericSum("h3l1o w07ld!")
>>> 11
'''

def numericSum(string):
    # Track the total
    total = 0
    for char in string:
        # The characters in the string are also of type string.
        # To tell whether a character is a number, try converting it to an integer.
        try:
            char = int(char)
        # If it cannot be converted to an integer, it is not a number.
        # Skip the character.
        except ValueError:
            continue
        # If the character was successfully converted to an integer, add it to the total.
        total += char
    
    return total

# Test the function with various input strings

def testNumericSum():
    strings = ["", "3", "k", "h3l10", "2023", "h3l1o w07ld!"]
    for input in strings:
        output = numericSum(input)
        print('input:', input, 'output:', output)
    return

# Run the tests

testNumericSum()
