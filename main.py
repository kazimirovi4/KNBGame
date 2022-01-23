import random


while True:
    # user_input = input()
    user_action = input('Сделай свой выбор - камень, ножницы или бумага: ')
    possible_actions = ['камень', 'ножницы', 'бумага']
    computer_action = random.choice(possible_actions)
    print(f'\nВы выбрали {user_action}, компьютер выбрал {computer_action}\n')

    if user_action == computer_action:
        print(f'Оба выбрали {user_action} - ничья!!!')
    elif user_action == 'камень':
        if computer_action == 'ножницы':
            print('Камень бьет ножницы. Вы победили')
        else:
            print('Бумага оборачивает камень! Вы проиграли!')
    elif user_action == 'ножницы':
        if computer_action == 'камень':
            print('Камень бьет ножницы. Вы проиграли')
        else:
            print('Ножницы режут бумагу! Вы победили!')
    elif user_action == 'бумага':
        if computer_action == 'ножницы':
            print('Ножницы режут бумагу! Вы проиграли!')
        else:
            print('Бумага оборачивает камень! Вы победили!')

    play_again = ''
    play_again = input('Сыграем еще? (д/н): ')
    if play_again.lower() != 'д':
        break