
with open('input1.txt') as f:
    lines = f.readlines()


# Part 1
max : int = 0
current : int = 0
for line in lines:
    line = line.strip()
    if line.isnumeric():
        current += int(line)
    if line == "":
        if current > max:
            max = current
        current = 0
    
#print(max)
## Answer : 69289

# Part 2
#find the top 3
max1 : int = 0
max2 : int = 0
max3 : int = 0
current = 0
for line in lines:
    line = line.strip()
    if line.isnumeric():
        current += int(line)
    if line == "":
        if current > max1:
            max3 = max2
            max2 = max1
            max1 = current
        elif current > max2:
            max3 = max2
            max2 = current
        elif current > max3:
            max3 = current
        current = 0
    
print(max3 + max2 + max1)

## Answer : 205615