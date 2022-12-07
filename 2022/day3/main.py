with open('input.txt') as f:
    lines = f.readlines()

small_letters = 'abcdefghijklmnopqrstuvwxyz'
big_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


sum = 0

for line in lines:
    line = line.strip()
   
   #divide line in two euqal parts
    line1 = line[:int(len(line)/2)]
    line2 = line[int(len(line)/2):]

    # print(line1)
    # print(line2)

    a=list(set(line1)&set(line2))

    for i in a:
        if (i.islower()):
            sum += small_letters.index(i) + 1
        else:
            sum += big_letters.index(i) + 27

 
# print(sum)


#part 2

with open('input.txt') as f:
    lines = f.readlines()

small_letters = 'abcdefghijklmnopqrstuvwxyz'
big_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

sum = 0


for line in range(0,len(lines),3):
    line1 = lines[line].strip()
    line2 = lines[line+1].strip()
    line3 = lines[line+2].strip()

    print(line1)
    print(line2)
    print(line3)
    print(" ")

    a=list(set(line1)&set(line2)&set(line3))

    for i in a:
        if (i.islower()):
            sum += small_letters.index(i) + 1
        else:
            sum += big_letters.index(i) + 27

print(sum)


    
