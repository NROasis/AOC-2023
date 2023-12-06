import re


def parse_data(data):
    with open(data) as f:
        lines = f.read().split('\n\n')
        seeds=[int(x) for x in re.findall(r'\d+',lines[0])]
        maps_raw = [re.findall(r'\d+',x) for x in lines[1:]]
        maps_processed = []
        seed_pairs=[]
        for map in maps_raw:
            maps=[]
            for i in range(0,len(map)-2,3):
                maps.append([int(x) for x in map[i:i+3]])
            maps_processed.append(maps)

        for i in range(0,len(seeds)-1,2):
            seed_pairs.append([seeds[i],seeds[i+1]])
    
    return seeds,maps_processed,seed_pairs
    
def solution_part1(data):
    seeds,maps,seed_pairs = parse_data(data)
    current_number=0
    location_list = []
    for seed in seeds:
        current_number=seed
        for map in maps:
            for nums in map:
                if nums[1] <= current_number <= nums[1]+nums[2]-1:
                    current_number=(current_number-nums[1])+nums[0]
                    break
                    
        location_list.append(current_number)
    return(min(location_list))

def generate_small_value(seeds):
    seed_range=[]
    for i in range(0,len(seeds)-1,2):
        seed_range.append((seeds[i]+seeds[i+1]))
    
    for i in range(max(seed_range)):
        yield(i)
##Takes 30 minutes, but it works...so
def solution_part2(data):


    seeds,maps,seed_pairs = parse_data(data)
    lowest_number=generate_small_value(seeds)
    no_match=True

    while no_match:
        current_number=next(lowest_number)
        answer=current_number
        for map in maps[::-1]:
            for nums in map:
                if nums[1]<=current_number-nums[0]+nums[1]<=nums[1]+nums[2]-1:
                    current_number=current_number-nums[0]+nums[1]
                    break
        for pair in seed_pairs:
            if pair[0]<=current_number<=pair[0]+pair[1]:
                no_match = False
                break             
    return(answer)
    
    
print(solution_part1('Day5_input.txt'))    
print(solution_part2('Day5_input.txt'))
