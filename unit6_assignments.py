# FizzBuzz Unit 6 assignments

# Assignment 6.4 - my_range() function that returns the same output as list(range(m, n))
def my_range(m, n):
    
    range = []
    
    # if range is 0 or negative, just return an empty array
    if m >= n:
        return range

    # fill in the 'range' array with ever increasing m values while m is less than n
    while m < n:
        range.append(m)
        m += 1

    return range

# Assignment 6.5 - Color Hex Codes
# Function 1 - Converting decimals in the range from 0 to 255 to HEX codes
def to_hex(decNum):
    if decNum < 0 or decNum > 255:
        print("The number is out of range (0-255)!")
        return "" # check for valid input range
    
    # array of hex digits
    hexDigits = "0123456789abcdef"

    # calculating each hex digit
    digit1 = hexDigits[decNum // 16] # integer division
    digit2 = hexDigits[decNum % 16]  # remainder

    hexNum = ""

    if digit1 == "0":
        hexNum = digit2 # if the first digit is 0 then get rid of it
    else:
        hexNum = digit1 + digit2

    return hexNum

# Function 1 variation for the second assignment
# Converts decimal number (in the range 0 - 255) to hex

# Difference from the function above is that this function
# returns hex value rendered with a leading "0"

def doubleDigit_hex(decNum):
    if decNum < 0 or decNum > 255:
        print("The number is out of range (0-255)!")
        return "" # check for valid input range
    
    # array of hex digits
    hexDigits = "0123456789abcdef"

    # calculating each hex digit
    digit1 = hexDigits[decNum // 16] # integer division
    digit2 = hexDigits[decNum % 16]  # remainder

    return digit1 + digit2

# Function 2 - Converting an RGB color code from decimal to HEX
def hex_color(red, green, blue):
    if red < 0 or green < 0 or blue < 0 or red > 255 or green > 255 or blue > 255:
        print("Decimal amount(s) out of range (0 - 255)!")
        return "" # valid input range check

    hexColor = "#" +  doubleDigit_hex(red) + doubleDigit_hex(green) + doubleDigit_hex(blue)

    return hexColor

# Assignment 6.6 - Reverse an array
def my_reverse(l):
    r = []

    for item in l:
        r.insert(0, item)

    return r

# Assignment 6.7 - Fibonacci sequence: find the first number of the Fibonacci sequence that has l digits
def big_fibonacci(l):

    # initial starting members of the Fibonacci sequence 
    n1 = 1
    n2 = 1

    while len(str(n2)) < l: # if we are still below the number of digits, continue calculating the next member of Fibonacci sequence
        sum = n1 + n2 # calculating the next member
        n1 = n2
        n2 = sum
    
    return n2

