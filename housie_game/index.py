import random

print('Welcome to the game of housie. Hope you have fun !!! ')

# number of players to generate cards
game_check = False
while True:

    players = input('Please enter the number of players : ')

    if players.isdigit() is True:
        players = int(players)
        if players < 2:
            print("There should be atleast 2 players to play the game. ")
        else:
            game_check = True
        break
    else:
        print("Please enter a valid number")


if game_check is True:
    # housie card generator for players
    cards = {}
    housie_range = range(1, 101)
    for player_num in range(1, players + 1):
        cards[f'player_{player_num}'] = random.sample(housie_range, 15)

    for player, card in cards.items():
        print('\n')
        print(player)
        print(*card[:5], sep=" ")
        print(*card[5:10], sep=" ")
        print(*card[10:], sep=" ")
        print('\n')


# zaldi5 check
def zaldi5_check(housie_numbers):
    check = False
    for player, card in cards.items():
        intersection = list(set(housie_numbers) & set(card))
        if len(intersection) == 5:
            check = True
            break
    if check is False:
        return check, None, []
    return check, player, intersection

# subset check
def subset_check(list1, list2):
    return set(list1).issubset(set(list2))

# row check
def row_check(row_number, housie_numbers):
    check = False
    for player, card in cards.items():
        if row_number == 1:
            row = card[:5]
            if subset_check(row, housie_numbers) is True:
                check = True
                break
        elif row_number == 2:
            row = card[5:10]
            if subset_check(row, housie_numbers) is True:
                check = True
                break
        elif row_number == 3:
            row = card[10:]
            if subset_check(row, housie_numbers) is True:
                check = True
                break

    if check is False:
        return check, None, []
    return check, player, row

# row check
def full_housie_check(housie_numbers):
    check = False
    for player, card in cards.items():
        if subset_check(card, housie_numbers) is True:
            check = True
            break

    if check is False:
        return check, None, []
    return check, player, card



if game_check is True:
    all_numbers = list(housie_range)
    random.shuffle(all_numbers)
    popped_housie_numbers = []
    players_zaldi5_check = False
    player_first_row_check = False
    player_second_row_check = False
    player_third_row_check = False
    player_full_housie_check = False

while game_check:

    current_housie_num = all_numbers.pop()
    print(f"The current housie number is {current_housie_num}")
    popped_housie_numbers.append(current_housie_num)

    if len(popped_housie_numbers) >=5:

        # zaldi5 check
        if players_zaldi5_check is False:
            players_zaldi5_check, zaldi5_player, intersection = zaldi5_check(popped_housie_numbers)
            if zaldi5_player is not None:
                print(f'Congrats to {zaldi5_player} on finishing zaldi5 !!!')
                print(f'Zaldi5 numbers are {intersection}')

        # first row check
        if player_first_row_check is False:
            player_first_row_check, row1_player, row1 = row_check(1, popped_housie_numbers)
            if row1_player is not None:
                print(f'Congrats to {row1_player} on finishing Row 1 !!!')
                print(f'Row 1 numbers are {row1}')

        # second row check
        if player_second_row_check is False:
            player_second_row_check, row2_player, row2 = row_check(2, popped_housie_numbers)
            if row2_player is not None:
                print(f'Congrats to {row2_player} on finishing Row 2 !!!')
                print(f'Row 2 numbers are {row2}')
        
        # third row check
        if player_third_row_check is False:
            player_third_row_check, row3_player, row3 = row_check(3, popped_housie_numbers)
            if row3_player is not None:
                print(f'Congrats to {row3_player} on finishing Row 3 !!!')
                print(f'Row 3 numbers are {row3}')


    # full housie check
    if len(popped_housie_numbers) >=15:
        player_full_housie_check , full_housie_player, card = full_housie_check(popped_housie_numbers)
        if full_housie_player is not None:
            print(f'Congrats to {full_housie_player} on finishing game !!!')
            print(f'card numbers are {card}')
            game_check= False





    text = input('Housie input : ')
    if text != "next":
        game_check= False
        


print('Thanks for playing the game')