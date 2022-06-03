from random import randrange as r


print('Welcome to the slot machine!')
print()
balance = 100
win = 0
lose = 0


print('Your balance:', balance)


while True:
    numbers = [r(0, 10) for i in range(3)]
    while True:
        bet = input('Please, input your bet that less or equal that your balance => ').strip()
        if bet.isdigit() and 0 <= int(bet) <= balance:         
            bet = int(bet)
            break
        else:
            print('You should input number!')


    print()


    if numbers[0] == numbers[1] == numbers[2]:
        win += 1
        bet *= 10
        balance += bet
        print(*numbers)
        print()
        print('Jackpot!!! (x10 to your bet)')
        print('Your winnings =>', bet)
        print()
        print('Your balance:', balance)
        print()
    elif numbers[0] == numbers[1] or numbers[0] == numbers[2] or numbers[1] == numbers[2]:
        win += 1
        bet *= 4
        balance += bet
        print(*numbers)
        print()
        print('Double slot! You won! (x4 to your bet)')
        print('Your winnings =>', bet)
        print()
        print('Your balance:', balance)
        print()
    else:
        lose += 1
        balance -= bet
        print(*numbers)
        print()
        print('You lose :(')
        print()
        print('Your balance:', balance)
        print()


    if balance == 0:
        print('Your balance = 0, you cant continue the game')
        print('Count of winnings:', win)
        print('Count of loses:', lose)
        break


    flag = True
    while True:
        cont = input('Would you like start next round? (y/n) => ').strip().lower()
        if cont == 'y':
            flag = True
            break
        elif cont == 'n':
            flag = False
            break
        else:
            print('You should input one char - y (yes) or n (no)')


    if flag == False:
        print()
        print('Thank you for the game! See you later')
        print('Count of winnings:', win)
        print('Count of loses:', lose)
        break
    else:
        continue
