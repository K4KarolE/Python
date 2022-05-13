
while True:
    try: 
        answer = int(input('Guess the amount of characters: '))
    except ValueError:
        print('Invalid answer')
        continue
    else:
        break

txt = "50800"

x = txt.isdigit()

print(x)