# Simple example of writing a file 

filename = 'chapter-10/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n") # Add mewline character to put next write on new line.
    file_object.write("I love creating new games.\n")