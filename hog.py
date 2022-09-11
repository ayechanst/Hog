import random

player1 = 0
player2 = 0
player3 = 0
player4 = 0

def dice_roller():
    roll = random.randint(1, 6)
    return roll
        
def play_round(player): 
    global player1
    global player2
    global player3
    global player4
    roll = dice_roller()
    print('You\'ve rolled a', roll)
    temp_total = roll
    if roll > 1:
        choice = input('Would you like to roll again? y = yes n = no: ')
        while choice == 'y':
            roll = dice_roller()
            if roll == 1:
                temp_total = 1
                break
            else:
                print('You rolled a', roll)
                temp_total += roll
            choice = input('Would you like to roll again? y = yes n = no: ')
    if temp_total == 1:
        print('You rolled a 1')
    if player == 1:
        player1 += temp_total
    elif player == 2:
        player2 += temp_total
    elif player == 3:
        player3 += temp_total
    elif player == 4:
        player4 += temp_total
    else:
        print('Invalid player')

def determine_winner():
    if player1 >= 100:
        return 1
    elif player2 >= 100:
        return 2
    elif player3 >= 100:
        return 3
    elif player4 >= 100:
        return 4
    else:
        return 0
    
def play_game():
    current_player = 1
    winner = determine_winner()
    while winner == 0:
        if current_player == 1:
            print('The turn belongs to player 1')
            play_round(1)
            current_player += 1
        elif current_player == 2:
            print('The turn belongs to player 2')
            play_round(2)
            current_player += 1
        elif current_player == 3:
            print('The turn belongs to player 3')
            play_round(3)
            current_player += 1
        elif current_player == 4:
            print('The turn belongs to player 4')
            play_round(4)
            current_player = 1
        else:
            print('ERROR')
    if winner == 1:
        print('Player 1 has won!')
    elif winner == 2:
        print('Player 2 has won!')
    elif winner == 3:
        print('Player 3 has won!')
    else: 
        print('player 4 has won!')

play_game()