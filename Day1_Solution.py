import string
import re


def parse_data(file):
    with open(file) as f:
        return f.read().split()


def solution_part_1(file):
    data = parse_data(file)
    lower_case=string.ascii_lowercase
    number_tracker =[]
    calibration_list=[]
    for line in data:
        for letter in line:
            if letter  not in lower_case:
                number_tracker.append(int(letter))
        calibration_list.append(str(number_tracker[0])+str(number_tracker[-1]))
        number_tracker=[]
    return sum(int(x) for x in calibration_list)


def solution_part_2(file):
    data = parse_data(file)
    
    number_dict={'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    keys='(?=('

    for key,value in number_dict.items():
        keys += key+'|'+value+'|' 
    keys = keys[:-1]+'))'

    calibration_list=[]

    for line in data:
        line = re.findall(keys,line)
        for i,num in enumerate(line):
            if len(num) !=1:
                line[i]=line[i].replace(num, number_dict[num])
        calibration_list.append(line[0]+line[-1])

    return sum(int(x) for x in calibration_list)

        
print(solution_part_1('Day1_input.txt'))
print(solution_part_2('Day1_input.txt'))
