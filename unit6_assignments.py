# FizzBuzz Unit 6 assignments
from math import sqrt

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

# Assignment 6.7 - Fibonacci sequence: find the first number of the Fibonacci sequence that has n digits
def big_fibonacci(n):

    # initial starting members of the Fibonacci sequence 
    n1 = 1
    n2 = 1

    while len(str(n2)) < n: # if we are still below the number of digits, continue calculating the next member of Fibonacci sequence
        sum = n1 + n2 # calculating the next member
        n1 = n2
        n2 = sum
    
    return n2

# Assignment 6.8 - FizzBuzz: for numbers from 1 to 1000
# print 'Fizz' if n divisible by 3,
# print 'Buzz' if n divisible by 5,
# print 'FizzBuzz' if n divisible by both 3 and 5
# print the number itself if it's not divisible by either 3 or 5
def fizz_buzz():
    for n in range(1, 1001):
        s = "" # initial string
        if n % 3 == 0:
            s += "Fizz" # adding 'Fizz' if n divisible by 3
        if n % 5 == 0:
            s += "Buzz" # adding 'Buzz' if n divisible by 5
        if s == "":
            s = str(n) # if s is still empty it is not divisible by 3 or 5
        print(s)

# Assignment 6.9 - Prime Number Test: test if the number n is prime (divisible only by 1 and itself)
def is_prime(n):
    # input validation check
    if n < 2:
        print("A number has to be greater than 1 to be prime!")
        return None

    # time warning (digits limit is over 15)
    if len(str(n)) > 15:
        print("This is a large number, it might take quite a long time to process")

    # quick optimization for the first prime numbers below 100
    for d in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
        if n == d:
            return True
        if n % d == 0:
            return False
    
    # brute force solution with light optimization:
    # given the optimization above the range can safely be from 11 to the approximate square root of the original number
    for d in range(11, int(sqrt(n))+1):
        if n % d == 0:
            return False
    
    return True