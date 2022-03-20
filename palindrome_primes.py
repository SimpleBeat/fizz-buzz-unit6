# FizzBuzz Unit 6 Assignment 6.11 - Find Palindrome Primes
# Find all five-digit prime numbers which are palindromes

# function checks if a number is a prime and returns True if it is or False if it's not
def is_prime(n):
    # light optimization (the most common divisors checked first)
    for d in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
        if n % d == 0:
            return False
    # brute force approach with light optimization (the range is safely shortened)
    for d in range(97, n//2):
        if n % d == 0:
            return False
    return True

# function checks if a five-digit number is a palindrom (reads from left to right the same as from right to left)
# IMPORTANT: this function works only for five-digit numbers and assumes the input is one
def is_palindrome(n):
    if n[0]==n[4] and n[1]==n[3]:
        return True # in a five-digit palindrome first and fifth digits are equal, as well as second and fourth
    return False

# Intro
print("Hello!")
print("This is FizzBuzz Academy Unit 6 assignment 'Find Palindrome Primes'")
print("This app will find all five-digit prime numbers which are palindromes.")
print("Let's start!")

# empty array of prime palindromes
prime_palindromes = []

# brute force approach
for num in range(10000, 100000):
    if is_prime(num):
        if is_palindrome(str(num)):
            prime_palindromes.append(num)
print()
print("Here are all the five-digit prime palindromes:")
print(prime_palindromes)
print()