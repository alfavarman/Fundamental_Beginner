answer1 = input('what is 2+2: ')
score = 0
try:
    if float(answer1) == 4:
        score += 1
        print(f'correct you got {score} point! Lets try again.')
    else:
        print(f'Incorrect You have {score} points.')
    answer2 = input('whats 5+7: ')
    if int(answer2) == 12:
        score += 1
        print(f'correct you got {score} point! Lets try again.')
    else:
        print(f'Incorrect You have {score} points.')
    answer3 = input('whats 5-2: ')
    if int(answer3) == 3:
        score += 1
        print(f'correct you got {score} point! Lets try again.')
    else:
        print(f'Incorrect You have {score} points.')
    answer4 = input('whats 5*2: ')
    if int(answer4) == 10:
        score += 1
        print(f'correct you got {score} point!')
    else:
        print(f'Incorrect You have {score} points.')

    print(f'thank you. Your total score is {score}')
except:
    ValueError
    print("Invalid input. Please type numbers")

