character = ['¬', '£', '$', '%', '&', '#', '@', '?', '=', '+']

charset = list(set(character)) 

print(charset[2])

character.remove(charset[2])

print(character)