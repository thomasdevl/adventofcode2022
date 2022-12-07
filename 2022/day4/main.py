with open('test.txt') as f:
    lines = f.readlines()

#In how many assignment pairs does one range fully contain the other?

#Part 1
def part1():

    #Create a list of all the ranges
    ranges = []
    for line in lines:
        ranges.append(line.strip().split(','))

    #print(ranges)

    sum = 0

    for range in ranges:
        r1 = [ int(x) for x in range[0].split('-') ]
        r2 = [ int(x) for x in range[1].split('-') ]

        print(r1, r2)

        if (r1[0] <= r2[0] and r1[1] >= r2[1]):
            sum += 1
        elif (r2[0] <= r1[0] and r2[1] >= r1[1]):
            sum += 1
    
    print(sum)

#part1()

#Part 2
def part2():
    with open('input.txt', 'r') as file:
        print(len([
            line for line in file.read().split('\n')
            if any(
                x in list(range(int(line.split(',')[1].split('-')[0]), int(line.split('-')[-1]) + 1))
                for x in range(int(line.split('-')[0]), int(line.split(',')[0].split('-')[1]) + 1)
            )
        ]))

part2()
