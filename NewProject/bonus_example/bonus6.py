# Sample list of names and surnames
names_and_surnames = ['john smith', 'jay santi', 'eva kuki']

# Capitalize names and surnames
capitalized_list = [f'{name.split()[0].capitalize()} {name.split()[1].capitalize()}' for name in names_and_surnames]

# Print the new list
print(capitalized_list)
