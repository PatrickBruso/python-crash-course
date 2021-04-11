favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# looping through the dictionary
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# looping through keys in dictionary
for name in favorite_languages.keys():
    print(name.title())

# looping through keys is default
for name in favorite_languages:
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# looping through keys in a particular order (alphabetical)
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# looping through values
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# using set function to not print repeat values
print("Set of languages:")
for language in set(favorite_languages.values()):
    print(language.title())

# you can create your own sets
languages = {'python', 'ruby', 'python', 'c'}