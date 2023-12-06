import re
import numpy as np

def parse_data(data):
    with open(data) as f:
        lines =  f.read().strip().split('\n')
        races = [re.findall(r'\d+',line) for line in lines]
        single_race=[int(x) for x in [line[line.find(':')+1:].replace(' ','') for line in lines]]

        int_lines = [[int (x) for x in races] for races in races]
        compiled_races=[]
        for i in range(0,len(int_lines[0])):
            compiled_races.append([int_lines[0][i],int_lines[1][i]])
    return compiled_races,single_race

def solution_part1(data):
    compiled_races,single_race = parse_data(data)
    answer=[]
    for race in compiled_races:
        race_tracker=[]
        for i in range(race[0]+1):
            distance = (race[0]-i)*i
            if distance>race[1]:
                race_tracker.append(distance)
        answer.append(len(race_tracker))
    return(np.prod(answer))

def solution_part2(data):
    compiled_races,single_race = parse_data(data)
    race_tracker = []
    for i in range(single_race[0]+1):
        distance = (single_race[0]-i)*i
        if distance>single_race[1]:
            race_tracker.append(distance)
    return(len(race_tracker))

print(solution_part1('Day6\Day6_input.txt'))
print(solution_part2('Day6\Day6_input.txt'))
