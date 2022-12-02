
with open('input.txt') as f:
    lines = f.readlines()


def part1():

    score = 0

    letter_score = {"X":1, "Y":2, "Z":3}

    signs = {"A":"rock", 
            "B":"paper", 
            "C":"scissors", 
            "X":"rock", 
            "Y":"paper",
            "Z":"scissors"}

    for line in lines:
        line = line.strip().replace(" ", "")

        print(letter_score[line[1]])

        if signs[line[0]] == signs[line[1]]: #tie game
            score += 3 + letter_score[line[1]]

        elif (line[0] == "A" and line[1] == "Y" ) or (line[0] == "B" and line[1] == "Z") or (line[0] == "C" and line[1] == "X"): #All where player wins 
            score += 6 + letter_score[line[1]]

        elif (line[0] == "A" and line[1] == "Z" ) or (line[0] == "B" and line[1] == "X") or (line[0] == "C" and line[1] == "Y"): #All where player loses
            score += 0 + letter_score[line[1]]

    return score 
    
def part2():
    score = 0

    draw_score = {"A":1, "B":2, "C":3}
    losing_score = {"A":3, "B":1, "C":2}
    winning_score = {"A":2, "B":3, "C":1}

    signs = {"A":"rock", 
            "B":"paper", 
            "C":"scissors", 
            "X":"rock", 
            "Y":"paper",
            "Z":"scissors"}

    for line in lines:
        line = line.strip().replace(" ", "")

        if line[1] == "Y": #draw 
            score += 3 + draw_score[line[0]]
        
        elif line[1] == "X": #lose
            score += 0 + losing_score[line[0]]

        elif line[1] == "Z": #win
            score += 6 + winning_score[line[0]]
    
    return score 

print(part1())
print(part2())


