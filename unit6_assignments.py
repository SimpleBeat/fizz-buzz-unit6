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
