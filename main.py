from getpass import getpass


class InputException(Exception):
    pass


def validate_user_input(user_input, possible_choices):
    if user_input not in possible_choices:
        raise InputException(f'"{user_input}" is not possible. Possibilities: {", ".join(possible_choices)}')


def get_turns():
    print('Select number of turns')
    turns = int(input())
    print()

    if turns < 0:
        raise InputException('Number of turns must be greater than 0')

    return turns

def get_user_inputs(possible_choices):

    choice_first_user = f'First user choice from: {", ".join(possible_choices)}: '
    first_choice = getpass(choice_first_user)
    validate_user_input(first_choice, possible_choices)

    choice_second_user = f'Second user choice from: {", ".join(possible_choices)}: '
    second_choice = getpass(choice_second_user)
    validate_user_input(second_choice, possible_choices)

    return first_choice, second_choice


def get_winner(first_choice, second_choice):
    winners = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }

    if first_choice == second_choice:
        return 'tie'
    elif winners[first_choice] == second_choice:
        return 'player_1'
    else:
        return 'player_2'


if __name__ == '__main__':
    possible_choices = ['rock', 'paper', 'scissors']
    turns = get_turns()
    player_1_points = 0
    player_2_points = 0
    plaing_turns = 1
    pairs = list()
    while turns > 0:
        print(f'Turn {plaing_turns}')
        first_choice, second_choice = get_user_inputs(possible_choices)
        pairs.append((first_choice, second_choice))
        winner = get_winner(first_choice, second_choice)
        if winner == 'player_1':
            player_1_points += 1
        elif winner == 'player_2':
            player_2_points += 1
        turns -= 1
        plaing_turns += 1
        print()
    if player_1_points > player_2_points:
        print(f'The winner is Player 1 with {player_1_points} points!')
    elif player_1_points < player_2_points:
        print(f'The winner is Player 2 with {player_2_points} points!')
    else:
        print('It is a tie! Everyone win!')
    print('If you want to see players choices, press 1, if not press anything else')
    peek_pairs = input()
    if peek_pairs == '1':
        print(f'Game pairs: {pairs}')
    print('Thanks for the game! See you! :)')
