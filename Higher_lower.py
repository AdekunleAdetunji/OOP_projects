import random

suit_tuple = ('King', 'Hearts', 'Clubs', 'Diamond')  # Card category identifiers
rank_tuple = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9',
              '10', 'Jack', 'Queen', 'King')  # Variants of each card category


def selector(deck, stages):
    sample = random.sample(deck, stages)
    return sample


deck_field = [{'rank': rank, 'value': value + 1, 'suit': suit} for suit in suit_tuple
              for value, rank in enumerate(rank_tuple)]  # The possible combination of cards in the deck
rounds = 8
while True: #  Allows for playing multiple game
    print('Welcome to the game of Higher&Lower, hope you have fun')
    print()

    samples = selector(deck_field, rounds)  # Card samples to begin game round with
    reference_card = random.sample(samples, 1)[0]  # The first card element from the sample
    reference_card_rank = reference_card['rank']
    reference_card_suit = reference_card['suit']
    reference_card_value = reference_card['value']
    score = 50
    for stage in range(0, rounds):  # Loop to begin the game process
        print(f'The reference card is one of suit {reference_card_suit} with rank ' +
              f'{reference_card_rank} with relevance score {reference_card_value}.')

        prompt = input('Please enter L or H if the next card is higher or lower than the ' +
                       'previous card: ')

        next_card = samples[stage]
        next_card_value = next_card['value']
        next_card_rank = next_card['rank']
        next_card_suit = next_card['suit']

        if prompt.lower() == 'l' and next_card_value < reference_card_value:
            print("You got it right!")
            print()
            score += 20

        elif prompt.lower() == 'h' and next_card_value > reference_card_value:
            print('You got it right!')
            print()
            score += 20

        else:
            print('Sorry you got it wrong :(')
            print()
            score -= 15

        reference_card_rank = next_card['rank']
        reference_card_value = next_card['value']
        reference_card_suit = next_card['suit']
    print(f'Your score for this round is: {score}')
    print()
    #  Prompt to continue replay game
    continuation_prompt = input('Enter Y to continue the game or any key to quit: ')
    if continuation_prompt.lower() != 'y':
        break
