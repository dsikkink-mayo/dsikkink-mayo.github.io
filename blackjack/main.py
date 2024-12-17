import art
import random

main = False
active_hand = True
user_playing = True
user_hand_viable = True

dealer_playing = True


green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
cyan = '\033[96m'
bold = '\033[1m'
end_format = '\033[0m'
big_line = '-------------------------------------------------------------'

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal():
    return random.choice(cards)

def calc_hand(hand):
    sorted_hand = sorted(hand)
    hand_value = 0
    for card in sorted_hand:
        if hand_value + card > 21 and card == 11:
            hand_value += 1
        else:
            hand_value += card
    return hand_value

def validate(prompt, valid_input):
    user_input = input(prompt).lower()
    while user_input not in valid_input:
        formatter(f"{user_input} is not a valid input. Please enter a valid input.", red)
        user_input = input(prompt).lower()
    return user_input


def hit_input():
    hit_input = input("Type 'y' to hit or 'n' to pass:").lower()
    return hit_input

def formatter(text, style):
    print(style + text + end_format)

def hand_result(hand_value):
    if hand_total > 21:
        formatter(f"Hand is at {str(hand_total)}", red)
        formatter("Bust!", red)
        print(big_line)
        # global player_lost
        # player_lost = True
        return False
    elif hand_total == 21:
        formatter(f"Hand is at {str(hand_total)}", cyan)
        formatter("Blackjack!", cyan)
        print(big_line)
        return False
    else:
        formatter(f"Hand is at {str(hand_total)}", green)
        return True

def determine_winner(user, opp):
    print(big_line)
    if user > 21:
        message = f"You busted. 😭 Dealer wins with {opp}!"
    elif opp > 21:
        message = f"Dealer busts! 😎 You win with {user}!"
    elif user == opp:
        message = f"PUSH! 🤔 It's a {user}-{opp} tie, guy."
    elif user > opp:
        message = f"You win! 😎 Your {user} beats {opp}"
    else:
        message = f"Dealer wins with {opp}! 😭"
    formatter(message, cyan)
    print(big_line)


print(big_line)
print( '\033[91m' + art.logo + '\033[0m')
print(big_line)
print("\n" )

play = validate(prompt="Do you want to play a game of Blackjack? Type 'y' or 'n':", valid_input=['y', 'n'])
if play == 'y':
    main = True
if play == 'n':
    formatter("Thanks for playing! Better luck next time!", cyan)
    main = False

while main:
    active_hand = True
    user_playing = True
    user_hand_viable = True

    dealer_playing = True

    opp_hand = []
    user_hand = []

    # Initial deal
    opp_hand.append(deal())
    opp_hand.append(deal())
    user_hand.append(deal())
    user_hand.append(deal())


    formatter(f"Dealer hand:[{opp_hand[0]}, ?]",yellow)
    print("\n")
    print(big_line)
    #### DEBUG
    # user_hand = [10,11]
    formatter(f"Your hand: {user_hand}",green)
    hand_total = calc_hand(user_hand)
    formatter(f"You have {str(hand_total)}", green)


    while user_playing:
        print(big_line)
        user_hits = validate(prompt="Type 'y' to hit or 'n' to stay:", valid_input=['y', 'n'])
        if user_hits == "y":
            user_hand.append(deal())
            formatter("You hit!", green)
            formatter(f"Your new hand: {user_hand}",green)
            hand_total = calc_hand(user_hand)
            user_playing = hand_result(hand_total)
        else:
            formatter(f"You stay at {hand_total}!", cyan)
            print(big_line)
            user_playing = False

    if calc_hand(user_hand) > 21:
        user_hand_viable = False

    formatter(f"Dealer flips {opp_hand[1]}",yellow)
    formatter(f"Dealer hand: {opp_hand}", yellow)
    hand_total = calc_hand(opp_hand)
    hand_result(hand_total)
    dealer_playing = user_hand_viable


    while dealer_playing:
        # if user_hand_viable == False:
        #      dealer_playing = False
        if calc_hand(opp_hand) < 17:
            opp_hand.append(deal())
            formatter("Dealer hits!", yellow)
            formatter(f"Dealer hand: {opp_hand}", yellow)
            hand_total = calc_hand(opp_hand)
            dealer_playing = hand_result(hand_total)
        else:
            hand_total = calc_hand(opp_hand)
            formatter(f"Dealer stays at {hand_total}!", yellow)
            # print(big_line)
            dealer_playing = False

    determine_winner(calc_hand(user_hand), calc_hand(opp_hand))
    play_again = validate(prompt="Do you want to play again? Type 'y' or 'n':", valid_input=['y', 'n'])
    if play_again == 'y':
        print("\n" * 30)
        print(big_line)
        print('\033[91m' + art.logo + '\033[0m')
        print(big_line)
        print("\n")
    else:
        print("Thanks for playing! Better luck next time!")
        main = False
