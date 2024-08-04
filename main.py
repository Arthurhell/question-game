questions = [
    {
        'Question': 'How much is 2 + 2?',
        'Options': ['1', '3', '4', '5'],
        'Answer': '4',
    },
    {
        'Question': 'How much is 5 * 5',
        'Options': ['25', '55', '10', '51'],
        'Answer': '25',
    },
    {
        'Question': 'How much is 10 / 2',
        'Options': ['4', '5', '2', '1'],
        'Answer': '5',
    },
]

howManyHits = 0

for question in questions:
    print('Question: ', question['Question'])
    print()

    options = question['Options']
    for i, option in enumerate(options):
        print(f'{i})', option)
    print()

    choose = input('Choose one option: ')

    gotItRight = False
    chooseInt = None
    howManyOptions = len(options)

    if choose.isdigit():
        chooseInt = int(choose)

    if chooseInt is not None:
        if chooseInt >= 0 and chooseInt < howManyOptions:
            if options[chooseInt] == question['Answer']:
                gotItRight = True
                
    print()

    if gotItRight:
        howManyHits += 1
        print("You got It!")
    else:
        print("You are Wrong!")
    
print(f'You got {howManyHits} hits from {len(questions)} questions!')