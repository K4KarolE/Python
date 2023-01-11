# Movie Quiz Game

import random, time

questions_list = ['Which one is the best "planet" to celabrate Mother`s day on?',
                  'Who is the father of Luke?',
                  'What should Neo follow?',
                  'What is the ring carrier`s profession?',
                  'Who is the sexiest fictional character?' ]

options_list = ['A.The Sun, B.Ton 618(black hole), C.LV-426 ',
                'A.Leia, B.Darth Vader, C.Jar Jar ',
                'A.A white rabbit, B.A yellow submarine, C.A pink panther ',
                'A.Be a nephew, B.Be a hobbit, C.Spartans: Auhh Auhh Auhh  ',
                'A.Gimli, B.Jabba the Hutt, C.Jessica Rabbit ']

answers_list = ['C', 'B', 'A', 'B', 'C']

score = 0
def question(questions_list, options_list, answers_list):
    random_number = questions_list.index(random.choice(questions_list))
    print(questions_list[random_number])
    answer = input(options_list[random_number])
    if answer.upper() == answers_list[random_number]:
        print('Correct')
        choice = 1
    else:
        print('Incorrect!')
        choice = 0
    questions_list.pop(random_number)
    answers_list.pop(random_number)
    options_list.pop(random_number)
    return choice

for i in range (1,6):
    if question(questions_list, options_list, answers_list) == 1:
        score += 1


print('Your got ' + str(score) + ' answers right! (' + str(score/5*100) + '%)\n')

print("Thx for playing!\n")

time.sleep(5)