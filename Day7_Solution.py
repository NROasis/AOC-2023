from operator import *

def parse_data(data):
    with open(data) as f:
        lines = f.read().split('\n')
        hands = [[*x[0]]+[x[1]] for x in [line.split()for line in lines]]

        return hands
    

def find_win(hand):
    count={}
    for card in hand[:-1]:
        count[card]=hand.count(card)
 
    if max(count.values()) == 1:
        
        return 0
    if max(count.values()) == 2:
        if countOf(count.values(),2) == 2:
            return 2
        else:
            return 1
    if max(count.values()) == 3:
        if countOf(count.values(),2) == 1:
            return 4
        else:
            return 3 
    if max(count.values()) == 4:
        return 5
    if max(count.values()) == 5:
        return 6
    


def solution_part1(data):
    card_dict = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    hands = parse_data(data)
    new_hands = []
    answer = 0
    for hand in hands:
        new_cards=[]
        new_cards.append(find_win(hand))
        for card in hand:
            if card.isdigit():
                new_cards.append(int(card))
            else:
                new_cards.append(card_dict[card])
        new_hands.append(new_cards)
    for i, hand in enumerate(sorted(new_hands)):
        answer += (i+1)*hand[-1]
    return(answer) 


def find_win_joker(hand):
    count={}
    for card in hand[:-1]:
        # if card.isdigit() is False and card != 'J':
            # hand = list(map(lambda x: x.replace(card, card_dict[card]), hand))
        if card == 'J':
            count[0]='J'
        else:
            count[hand.count(card)]=card
    hand = list(map(lambda x: x.replace('J', count[max(count.keys())]), hand))
    count={}
    for card in hand[:-1]:

        count[card]=hand.count(card)

    if max(count.values()) == 1:
        
        return 0
    if max(count.values()) == 2:
        if countOf(count.values(),2) == 2:
            return 2
        else:
            return 1
    if max(count.values()) == 3:
        if countOf(count.values(),2) == 1:
            return 4
        else:
            return 3 
    if max(count.values()) == 4:
        return 5
    if max(count.values()) == 5:
        return 6
 

def solution_part2(data):
    card_dict = {'T':10, 'J':0, 'Q':12, 'K':13, 'A':14}
    hands = parse_data(data)
    new_hands = []
    answer = 0
    for hand in hands:
        new_cards=[]
        new_cards.append(find_win_joker(hand))
        for card in hand:
            if card.isdigit():
                new_cards.append(int(card))
            else:
                new_cards.append(card_dict[card])
        new_hands.append(new_cards)
    for i, hand in enumerate(sorted(new_hands)):
        answer += (i+1)*hand[-1]

    return(answer) 

print(solution_part1('Day7_input.txt'))
print(solution_part2('Day7_input.txt'))
