from random import randint

player_name = 'чел'
player_level = 5
player_hp = 100 + player_level
player_xp = 9
player_money = 10

while True:
    print('-------------------------------------------')
    print('0 - уйти')
    print('1 - Начать сражение')
    print('2 - сыграть в кости')
    print('3 - пойти в дикси')
    print('-------------------------------------------')
    option = input('Введите номер ответа и нажмите Enter: ')
    if option == '1':

        enemy_name = 'анти чел'
        enemy_level = 1
        enemy_hp = 100 + player_level
        enemy_xp = 0

        print(player_name, 'Против', enemy_name, '!')
        while True:
            player_attack = randint(0, 10) + player_level
            input('нажми Enter что бы бить ')
            enemy_hp -= player_attack
            print(player_name, 'ударил', enemy_name, 'на', player_attack, 'жизней')
            print('у', enemy_name, 'стало', enemy_hp, 'жизней')
            if player_hp <= 0:
                print(player_name, 'проиграл')
              
                break
            
            enemy_attack = randint(0, 10) + enemy_level
            player_hp -= enemy_attack
            print(enemy_name, 'ударил', player_name, 'на', enemy_attack, 'жизней')
            print('у', player_name, 'стало', player_hp, 'жизней')
            if enemy_hp <= 0:
                print(enemy_name, 'проиграл')
                player_xp += enemy_level
                player_money += enemy_level
                print(player_name, 'получил', enemy_level, 'опыта')
                print('y', player_name, player_xp, 'опыта')
                if player_xp % 10 == 0 :
                    player_level += player_xp // 10
                    player_xp += enemy_level % 10
                    print( ' уровень игрока = ' , player_level )
                    print('у игрока', player_money, 'монет')
                    break

    elif option == '2':
        while True:
            if player_money <= 0:
                print('у тебя слишком мало денег')
                break
            print('играем')
            print('У', player_name, player_money, 'монет')
            print('1- уйти')
            print('2- ставлю')
            ig = input('ставишь или нет? ')
            if ig == '2':
                bet = int(input('сколько ставить? '))
                if bet > player_money:
                    print('у тебя нет столько')
                    continue
                if bet <= 0:
                    print('ставка не засчитана, нужно больше 0')
                    continue
                player_score = randint(2, 12)
                enemy_score = randint(2, 12)
                print(player_name, 'выбросил', player_score)
                print('противник выбросил', enemy_score)
                if player_score > enemy_score:
                    player_money += bet
                    print(player_name, 'победил')
                elif player_score < enemy_score:
                    player_money -= bet
                    print('ротивник победил')
                else:
                    print('ничья')
            if ig == '1':
                break

    elif option == '3':
        print(player_name, 'оказался в дикси')
        print('0- уйти')
        print('1- купить шаурму по акции за 3 монеты')
        op = input('Введите номер варианта ')
        if op == '1':
            print('да')
    elif option == '0':
        print('чел ушёл')
        break

print('ИГРА ОКОНЧЕНА!')
