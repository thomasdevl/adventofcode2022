with open('input.txt', 'r') as f:
    lines = f.read().split('\n')
    dirs, current = {}, []
    for l in lines:
        if l.startswith('$'):
            if 'cd' in l:
                _, _, dest = l.split()
                if dest == '/':    current = ['/']
                elif dest == '..': current.pop()
                else:              current.append(dest)
        elif l.startswith('dir'): continue
        else:
            for i in range(1, len(current) + 1):
                curr= tuple(current[:i])
                dirs.setdefault(curr, 0)
                dirs[curr] += int(l.split()[0])
        
    print(sum(v for v in dirs.values() if v < 100000))
    
    total_size, required = 70000000, 30000000
    free = total_size - dirs[('/',)]

    print(min(v for v in dirs.values() if free + v >= required))