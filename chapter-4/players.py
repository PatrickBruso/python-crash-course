players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])

# can omit first index to start from beginning
print(players[:4])

# same for the ending
print(players[2:])

# use negative index to output last three players on list
print(players[-3:])

# looping through a subset of elements in a list
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())