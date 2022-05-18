filename = 'pi_digits.txt' # File to open

# Open file and read each line into list lines
with open(filename) as file_object:
    lines = file_object.readlines()

# Create new empty string and concatenate each list item onto string
pi_string = ''
for line in lines:
    pi_string += line.strip() # Strip all whitespace

# Print string and length of string
print(pi_string)
print(len(pi_string))