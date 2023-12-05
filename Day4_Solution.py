def parse_input(data):
    with open(data) as f:
        lines = f.read().split('\n')
        winning_numbers = [num.replace('  ',' ').split(' ') for num in [x[x.find('|')+1:].strip() for x in lines]]
        cards = [num.replace('  ',' ').split(' ') for num in [x[x.find(': ')+1:x.find('|')].strip() for x in lines]]
        return cards,winning_numbers

def solution_part1(data):
    total_worth = 0

    cards,winning_numbers = parse_input(data)

    for i,card in enumerate(cards):
        count = 0
        for num in card:
            if num in winning_numbers[i]:
                if count == 0: count = 1
                else: count*=2
        total_worth+=count
    return(total_worth)


def solution_part2(data):

    cards,winning_numbers = parse_input(data)
    board_list = [x for x in range(len(cards))]
    game_dict={}
    for i in range(len(cards)):
        game_dict[i]=[cards[i],winning_numbers[i]]
    
    for i in board_list:
        count =0
        for num in game_dict[i][0]:
            if num in game_dict[i][1]:
                count+=1
                board_list.append(i+count)

    return len(board_list)

print(solution_part1('Day4_input.txt'))        
print(solution_part2('Day4_input.txt'))
