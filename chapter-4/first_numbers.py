# use range function to print list of numbers
for value in range(1, 5):
    print(value)

# use list function to put range of numbers into a list
numbers = list(range(1, 6))
print(numbers)

# list only even numbers using the third argument
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# get list of first 10 square numbers
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# better code for above
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# examples of functions for working with numbers
digits = list(range(1, 10))
digits.append(0)
print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))