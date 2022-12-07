with open('input.txt', 'r') as f:
    text = f.read()
    print([
        i+4 for i in range(len(text) - 4) if len(set(text[i : i + 4])) == 4
    ][0])


with open('input.txt', 'r') as f:
    text = f.read()
    print([i+14 for i in range(len(text) - 14) if len(set(text[i : i + 14])) == 14][0])


