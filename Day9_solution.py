def parse_input(data):
    with open(data) as f:
        histories = [[int(y) for y in x.split()] for x in f.read().split('\n')]
        return histories


def extrapolate_backward(final_num_list):
    extrap=0

    final_num_list= final_num_list[::-1]
    for final_num in final_num_list:
        extrap = final_num-extrap
    return extrap

def check_zero(list):
    if len(set(list)) == 1:
        return True
    else:
        return False


def solution_part1(data):
    histories = parse_input(data)
    sum_extrap = 0
    
    for history in histories:
        final_num_list = [history[-1]]
        current_list = history

        while True:
            differences = []

            for i in range(len(current_list)-1):
                differences.append(current_list[i+1]-current_list[i])

            current_list=differences
            final_num_list.append(current_list[-1])

            if check_zero(current_list):
                break
        sum_extrap += sum(final_num_list)
       
    return sum_extrap


def solution_part2(data):          
    histories = parse_input(data)
    sum_extrap = 0
    
    for history in histories:
        final_num_list = [history[0]]
        current_list = history

        while True:
            differences = []

            for i in range(len(current_list)-1):
                differences.append(current_list[i+1]-current_list[i])

            current_list=differences
            final_num_list.append(current_list[0])

            if check_zero(current_list):
                break

        sum_extrap += extrapolate_backward(final_num_list)
       
    return sum_extrap

print(solution_part1('Day9_input.txt'))
print(solution_part2('Day9_input.txt'))
