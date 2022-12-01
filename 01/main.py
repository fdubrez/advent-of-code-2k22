import functools

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
    print(lines)
    elves = []
    current_elf = []
    for line in lines:
        if '' == line:
            elves.append(current_elf)
            current_elf = []
        else:
            current_elf.append(int(line))
    
    print(elves)
    reduced = list(map(lambda elf: functools.reduce(lambda a, b : a + b, elf), elves))
    reduced.sort()
    print(reduced)
    print(reduced.pop())