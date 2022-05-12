# Movie Quiz Game

print("")
introq = input("Is it a lovely day for a little Movie Quiz? " )

if introq.lower() != "yes":
      quit()

print("")
print("Hurray! Let`s play!\n")
score = 0


# 1st Question
print('Which one is the best "planet" to celabrate Mother`s day on?')
answer = input('A.The Sun, B.Ton 618(black hole), C.LV-426 ')
if answer.upper() != 'C':
    print('Incorrect')
else:
    print('Correct!')
    score += 1
print("")

# 2nd Question
print('Who is the father of Luke?')
answer = input('A.Leia, B.Darth Vader, C.Jar Jar ')
if answer.upper() != 'B':
    print('Incorrect')
else:
    print('Correct!')
    score += 1
print("")

# 3rd Question
print('What should Neo follow?')
answer = input('A.A white rabbit, B.A yellow submarine, C.A pink panther ')
if answer.upper() != 'A':
    print('Incorrect')
else:
    print('Correct!')
    score += 1
print("")

# 4th Question
print('What is the ring carrier`s profession?')
answer = input('A.Be a nephew, B.Be a hobbit, C.Spartans: Auhh Auhh Auhh  ')
if answer.upper() != 'A':
    print('Incorrect')
else:
    print('Correct!')
    score += 1
print("")

# 5th Question
print('Who is the sexiest fictional character?')
answer = input('A.Gimli, B.Jabba the Hutt, C.Jessica Rabbit ')
if answer.upper() != 'C':
    print('Incorrect')
else:
    print('Correct!')
    score += 1
print("")


print('Your got ' + str(score) + ' answers right! (' + str(score/5*100) + '%)\n')

print("Thx for playing!\n")