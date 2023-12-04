def parse_data(file):
    with open(file) as f:
        lines = f.read().split('\n')
        games = [line[line.find(':')+2:] for line in lines]
        return games

def solution_1(file):
    block_count = {'red':12,'green':13,'blue':14}
    games=parse_data(file)
    id_count=0
    for i,game in enumerate(games):
        sequence=game.split(';')
        x=1
        for pulls in sequence:
            pull = pulls.strip().split(',')
            for blocks in pull:
                count,block=blocks.strip().split()
                if int(count)>block_count[block]:
                    x=0
        id_count+=(i+1)*x
        x=1
    return(id_count)
                
def solution_2(file):
    games=parse_data(file)
    id_count=0

    for game in games:
        blue_max, red_max, green_max=0,0,0
        sequence=game.split(';')
        for pulls in sequence:
            pull = pulls.strip().split(',')
            for blocks in pull:
                count,block=blocks.strip().split()
                count = int(count)
                if block=='blue' and count>blue_max: blue_max=count
                if block=='green' and count>green_max: green_max=count
                if block=='red' and count>red_max: red_max=count

        power=blue_max*red_max*green_max       
        id_count+=power
    return(id_count)

print(f"The soultion to part 1 is {solution_1('Day2_input.txt')}.")
print(f"The soultion to part 1 is {solution_2('Day2_input.txt')}.")
