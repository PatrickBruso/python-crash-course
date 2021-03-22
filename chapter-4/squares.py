# example of list comprehension
squares = [value**2 for value in range(1, 11)]
print(squares)

# counting to 20
for number in range(1, 21):
    print(number)

# summing a million
millions = list(range(1, 1000001))
print(min(millions))
print(max(millions))
print(sum(millions))

# print odds
odds = list(range(1, 21, 2))
print(odds)

# multiples of three
threes = [value * 3 for value in range(3, 31)]
print(threes)

# first 10 cubes
cubes = [value**3 for value in range(1, 11)]
print(cubes)