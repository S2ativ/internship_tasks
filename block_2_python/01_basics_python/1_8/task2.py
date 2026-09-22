balans = 0

while True:
    print('--- Меню ---')
    print('1) Пополнить')
    print('2) Снять')
    print('3) Баланс')
    print('4) Выход')
    
    command = input('Выберите действие(1-4 или название): ')

    if command in ['1', 'пополнить']:
        upgrade = int(input('Введите сумму для пополнения: '))
        balans += upgrade
        print(f'Счет пополнен на {upgrade}. Текущий баланс: {balans}')

    elif command in ['2', 'снять']:
        downgrade = int(input('Введите сумму для снятия: '))
        if balans >= downgrade:
            balans -= downgrade
            print(f'Со счета снято {downgrade}. Текущий баланс: {balans}')
        else:
            print('Неостаточно средств на балансе.Операция отменена.')

    elif command in ['3', 'баланс']:
        print(f'Текущий баланс: {balans}')

    elif command in ['4', 'выход']:
        print('Выход из программы.Спасибо за использование нашего сервиса!')
        break

    else:
        print('Неизвестная команда!Пожалуйста, выберите пункт из меню.')