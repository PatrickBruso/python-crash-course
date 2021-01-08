motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# change element in list
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles[0] = 'honda'

# append new element to end of list
motorcycles.append('ducati')
print(motorcycles)

# creating lists with append
motorcycles2 = []
motorcycles2.append('harley')
motorcycles2.append('yamaha')
motorcycles2.append('ninja')

print(motorcycles2)

# inserting elements into list
motorcycles.insert(0, 'harley')
print(motorcycles)

# remove element from list
del motorcycles[0]
print(motorcycles)

# 'pop' an item from end of list but keep to use
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print(f"The last motorcyle I owned was a {popped_motorcycle.title()}.")

# set a position with 'pop' to remove any item
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# removing an item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")