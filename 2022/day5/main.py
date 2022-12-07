



# [T]     [D]         [L]            
# [R]     [S] [G]     [P]         [H]
# [G]     [H] [W]     [R] [L]     [P]
# [W]     [G] [F] [H] [S] [M]     [L]
# [Q]     [V] [B] [J] [H] [N] [R] [N]
# [M] [R] [R] [P] [M] [T] [H] [Q] [C]
# [F] [F] [Z] [H] [S] [Z] [T] [D] [S]
# [P] [H] [P] [Q] [P] [M] [P] [F] [D]
#  1   2   3   4   5   6   7   8   9 





def part1():
    stacks = [["P","F","M","Q","W","G","R","T"],
            ["H","F","R"],
            ["P","Z","R","V","G","H","S","D"],
            ["Q","H","P","B","F","W","G"],
            ["P","S","M","J","H"],
            ["M","Z","T","H","S","R","P","L"],
            ["P","T","H","N","M","L"],
            ["F","D","Q","R"],
            ["D","S","C","N","L","P","H"]]

    with open('input.txt') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip().split()
        # print(line)

        number_of_times = int(line[1]) #number of times to move
        fromo = int(line[3]) #from
        to = int(line[-1]) #to 


        for _ in range(number_of_times):
            stacks[to-1].append(stacks[fromo-1].pop())
        #     stacks[int(line[-1])-1].append(stacks[int(line[3])-1])
        #     stacks[int(line[3])-1].pop()

    for stack in stacks:
        print(stack[-1])

def part2():
    stacks = [["P","F","M","Q","W","G","R","T"],
            ["H","F","R"],
            ["P","Z","R","V","G","H","S","D"],
            ["Q","H","P","B","F","W","G"],
            ["P","S","M","J","H"],
            ["M","Z","T","H","S","R","P","L"],
            ["P","T","H","N","M","L"],
            ["F","D","Q","R"],
            ["D","S","C","N","L","P","H"]]

    with open('input.txt') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip().split()
        print(line)

        number_of_times = int(line[1]) #number of crates to move
        fromo = int(line[3]) #from
        to = int(line[-1]) #to 

        
        crates_to_move = stacks[fromo-1][-number_of_times:]

        for crate in crates_to_move:
            stacks[to-1].append(crate)
            stacks[fromo-1].pop()

    for stack in stacks:
        print(stack[-1])


part2()