import re
import math
import numpy as np

def parse_solution(data):
    with open(data) as f:
        lines = f.read().strip().split('\n\n')
        directions = lines[0]
        elements = [[re.findall(r'\w+',y) for y in x.split('\n')] for x in lines[1:]]
        return directions,elements[0]

def check_directions(i,directions):
    if i == len(directions):
        return 0
    else:
        return 1

def solution_part1(data):

    directions,elements = parse_solution(data)
    current_loc='AAA'
    direction_tracker = 0 
    element_tracker = 0
    steps = 0
    arrived = False


    while not arrived:
        direction_tracker *= check_directions(direction_tracker,directions)
        element_tracker *= check_directions(element_tracker,elements)
        if elements[element_tracker][0]==current_loc:
            if directions[direction_tracker]=='L':
                current_loc = elements[element_tracker][1]
                direction_tracker+=1
                steps +=1
            else:
                current_loc = elements[element_tracker][2]
                direction_tracker+=1
                steps +=1

        if current_loc == 'ZZZ':
            break
        element_tracker +=1

    return steps

def check_win(loc_list):
    loc_check=[]
    for x in loc_list:
        loc_check.append(x[1])
    if len(set(loc_check)) == 1 and loc_check[0]!=0:
        return True
    else:
        return False

def solution_part2(data):

    directions,elements = parse_solution(data)
    loc_list=[[x[0],0,0,0]for x in elements if x[0][2]=='A']

    for i in range(len(loc_list)):
            step = loc_list[i][1]
            arrived = False
            current_loc=loc_list[i][0]
            while not arrived:
                loc_list[i][2] *= check_directions(loc_list[i][2],directions)
                loc_list[i][3] *= check_directions(loc_list[i][3],elements)
                if elements[loc_list[i][3]][0]==current_loc:
                    if directions[loc_list[i][2]]=='L':
                        current_loc = elements[loc_list[i][3]][1]
                        loc_list[i][2]+=1
                        loc_list[i][1] +=1
                    else:
                        current_loc = elements[loc_list[i][3]][2]
                        loc_list[i][2]+=1
                        loc_list[i][1] +=1

                if current_loc[2] == 'Z' and loc_list[i][1] != step:
                    loc_list[i][0] = current_loc
                    break
                loc_list[i][3] +=1


    step_list = [np.int64(x[1]) for x in loc_list]

    return math.lcm(*step_list), np.lcm.reduce(step_list)

print(solution_part1('Day8_input.txt'))
print(solution_part2('Day8_input.txt'))
