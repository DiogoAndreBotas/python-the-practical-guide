import pickle

user_choice = ''

while user_choice != 'q':
    print('Please choose:')
    print('1: Write input to file')
    print('2: Output file contents')
    print('3: Write input to file (json)')
    print('4: Output file contents (json)')
    print('q: Quit')

    user_choice = input('Your choice: ')
    if user_choice == '1':
        user_input = input('Type: ')

        with open('assignment_6.txt', mode='a') as file:
            file.write(user_input)
            file.write('\n')
    elif user_choice == '2':
        with open('assignment_6.txt', mode='r') as file:
            print(file.readlines())
    elif user_choice == '3':
        user_input = {
            'input': [input('Type: ')]
        }

        with open('assignment_6.p', mode='wb') as file:
            file.write(pickle.dumps(user_input))
    elif user_choice == '4':
        with open('assignment_6.p', mode='rb') as file:
            print(pickle.loads(file.read()))
