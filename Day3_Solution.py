def parse_data(file):
    with open(file) as f:
        data = f.read().split()
        return data


def check_rows(line_above,index):
    symbol_check = False
    if index == 0:
        for i in range(index,index+2):
            if line_above[i].isdigit() == False and line_above[i] != '.': symbol_check = True
    elif index == len(line_above)-1:
        for i in range(index-1,index+1):
            if line_above[i].isdigit() == False and line_above[i] != '.': symbol_check = True
    else:
        for i in range(index-1,index+2):
            if line_above[i].isdigit() == False and line_above[i] != '.': symbol_check = True
    return(symbol_check)

def check_sides(line,index):
    symbol_check = False
    if index ==0:
        if line[index+1].isdigit() == False and line[index+1] != '.': symbol_check = True
    elif index == len(line)-1:
        if line[index-1].isdigit() == False and line[index-1] != '.': symbol_check = True
    else:
        if line[index-1].isdigit() == False and line[index-1] != '.': symbol_check = True
        if line[index+1].isdigit() == False and line[index+1] != '.': symbol_check = True
    return symbol_check

def solution_part_1(file):
    lines = parse_data(file)
    number='0'
    symbol_checker=[]
    part_sum=0
    
    for i,line in enumerate(lines):
        for idx,char in enumerate(line):
            if char.isdigit() == True:
                number+=char
                if i == 0:
                    symbol_checker+=[check_rows(lines[i+1],idx),check_sides(line,idx)]
                elif i == len(line)-1:
                    symbol_checker+=[check_rows(lines[i-1],idx),check_sides(line,idx)]
                else:
                    symbol_checker+=[check_rows(lines[i+1],idx),check_rows(lines[i-1],idx),check_sides(line,idx)]
            else:
            
                if True in symbol_checker:
                    part_sum+= int(number)
                number='0'
                symbol_checker=[]
                
        if True in symbol_checker:
            part_sum+= int(number)
        number='0'
        symbol_checker=[]
    
    return(part_sum)
            
def extract_num(line,idx):
    num=line[idx]
    i=idx
    while line[i-1].isdigit():
        num = line[i-1]+num
        i = i-1
    i=idx
    while line[i+1].isdigit():
        num = num + line[i+1]
        i = i+1
    return(num)


def check_rows_star(line_above,index):
    num_list = []
    duplicate_protect = False
    if index == 0:
        for i in range(index,index+2):
            if line_above[i].isdigit() == True and duplicate_protect == False:
                num_list.append(extract_num(line_above,i))
                duplicate_protect=True
            if line_above[i].isdigit() == False:
                duplicate_protect=False
    elif index == len(line_above)-1:
        for i in range(index-1,index+1):
            if line_above[i].isdigit() == True and duplicate_protect == False:
                num_list.append(extract_num(line_above,i))
                duplicate_protect=True
            if line_above[i].isdigit() == False:
                duplicate_protect=False
    else:
        for i in range(index-1,index+2):
            if line_above[i].isdigit() == True and duplicate_protect == False:
                num_list.append(extract_num(line_above,i))
                duplicate_protect=True
            if line_above[i].isdigit() == False:
                duplicate_protect=False
    return(num_list)

def check_sides_star(line,index):
    num_list = []
    if index ==0:
        if line[index+1].isdigit() == True: num_list.append(extract_num(line,index+1))
    elif index == len(line)-1:
        if line[index-1].isdigit() == True: num_list.append(extract_num(line,index-1))
    else:
        if line[index-1].isdigit() == True: num_list.append(extract_num(line,index-1))
        if line[index+1].isdigit() == True: num_list.append(extract_num(line,index+1))
    return num_list

def solution_part_2(file):
    lines = parse_data(file)
    gear_ratio=0
    for i, line in enumerate(lines):
        for idx,char in enumerate(line):
            num_list = []
            if char == '*':
                if i == 0:
                    num_list=+check_rows_star(lines[i+1],idx)+check_sides_star(line,idx)
                elif i == len(line)-1:
                    num_list+=check_rows_star(lines[i-1],idx)+check_sides(line,idx)
                else:
                    num_list+=check_rows_star(lines[i+1],idx)+check_rows_star(lines[i-1],idx)+check_sides_star(line,idx)
                if len(num_list) == 2:
                    gear_ratio+=int(num_list[0])*int(num_list[1])
    return(gear_ratio)

print(solution_part_1('Day3_input.txt'))
print(solution_part_2('Day3_input.txt'))
