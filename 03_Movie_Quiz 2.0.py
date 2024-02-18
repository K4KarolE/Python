''' Movie Quiz Game - with dictionary '''

print("\n")
introq = input("Is it a lovely day for a little Movie Quiz? " )

if introq.strip().lower() not in  ['yes', 'y']:
      quit()

print("")
print("Hurray! Let`s play!\n")
score = 0

quiz_dic = {
    '1': {
        'question': 'Which one is the best "planet" to celabrate Mother`s day on?',
        'options': ['A. The Sun', 'B. Ton 618(black hole)', 'C. LV-426'],
        'correct_answer': 'C'
      },
    '2': {
        'question': 'Who is the father of Luke?',
        'options': ['A. Leia', 'B. Darth Vader', 'C. Jar Jar'],
        'correct_answer': 'B'
      },
    '3': {
        'question': 'What should Neo follow?',
        'options': ['A. A white rabbit', 'B. A yellow submarine', 'C. A pink panther'],
        'correct_answer': 'A'
      },
    '4': {
        'question': 'What is the ring carrier`s profession?',
        'options': ['A. Be a nephew', 'B. Be a hobbit', 'C. Spartans: Auhh Auhh Auhh'],
        'correct_answer': 'B'
      },
    '5': {
        'question': 'Who is the sexiest fictional character?',
        'options': ['A. Gimli', 'B. Jabba the Hutt', 'C. Jessica Rabbit'],
        'correct_answer': 'C' 
      }
    }


for item in quiz_dic:

  print(quiz_dic[item]['question'])
  for option in quiz_dic[item]['options']:
    print(option)
  answer = input().strip().upper()

  if answer != quiz_dic[item]['correct_answer']:
    print('Incorrect\n')
  else:
    print('Correct!\n')
    score += 1


questions_amount = len(quiz_dic.keys())
print(f'Your got {score} answers right! ({int(score/questions_amount*100)}%)\n')
print("Thx for playing!\n")