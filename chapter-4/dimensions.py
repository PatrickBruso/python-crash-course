# tuple is an immutable list
dimensons = (200, 50) # this is a tuple
print(dimensons[0])
print(dimensons[1])

# can loop over a tuple like a list
for dimenson in dimensons:
    print(dimenson)

# to change a tuple you assign a new value to the variable
print("Original dimensons:")
for dimenson in dimensons:
    print(dimenson)

dimensons = (400, 100)
print("\nModified dimensons:")
for dimenson in dimensons:
    print(dimenson)