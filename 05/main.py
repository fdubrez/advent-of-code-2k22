import re
from copy import deepcopy

# regex = r"(?P<stack1>\[\w\]?|\s{3}) (?P<stack2>\[\w\]?|\s{3}) (?P<stack3>\[\w\]?|\s{3}) (?P<stack4>\[\w\]?|\s{3}) (?P<stack5>\[\w\]?|\s{3}) (?P<stack6>\[\w\]?|\s{3}) (?P<stack7>\[\w\]?|\s{3}) (?P<stack8>\[\w\]?|\s{3}) (?P<stack9>\[\w\]?|\s{3})"
# re.match("(?P<stack1>\[\w\]?|\s{3}) (?P<stack2>\[\w\]?|\s{3}) (?P<stack3>\[\w\]?|\s{3}) (?P<stack4>\[\w\]?|\s{3}) (?P<stack5>\[\w\]?|\s{3}) (?P<stack6>\[\w\]?|\s{3})", line).groupdict()
# {'stack1': '   ', 'stack2': '   ', 'stack3': '[H]', 'stack4': '   ', 'stack5': '[W]', 'stack6': '[B]'}

indexes = {
    "stack1": 1,
    "stack2": 5,
    "stack3": 9,
    "stack4": 13,
    "stack5": 17,
    "stack6": 21,
    "stack7": 25,
    "stack8": 29,
    "stack9": 33,
}

def parse_start_line(line, stacks):
    for i in range(1, 10):
        char = line[indexes[f"stack{i}"]]
        if char != " ":
            stacks[i-1].append(char)

def main(filename):
    with open(filename) as file:
        lines = [line for line in file]
        # init stacks
        stacks = list(map(lambda x: [], range(1, 10)))
        moves = []
        for line in lines:
            if line.startswith(" 1"):
                continue
            if line.startswith(" ") or line.startswith("["):
                parse_start_line(line=line, stacks=stacks)
            if line.startswith("move"):
                moves.append(line)

        for i in range(0, 9):
            stacks[i] = list(reversed(stacks[i]))

        # copy stacks for exo2
        stacks2 = deepcopy(stacks)
        
        for move in moves:
            groups = re.match("move (?P<count>\d+) from (?P<from>\d+) to (?P<to>\d+)", move).groupdict()    
            count = int(groups["count"])
            from_ = int(groups["from"]) -1
            to = int(groups["to"]) -1
            
            for _ in range(0, count):
                stacks[to].append(stacks[from_].pop())
            
            if count > 1:
                stacks2[to].extend(stacks2[from_][-1*count:])
                for _ in range(0, count):
                    stacks2[from_].pop()
            else:
                stacks2[to].append(stacks2[from_].pop())
        exo1 = ""
        exo2 = ""
        for i in range(0,9):
            exo1 = exo1 + stacks[i][-1:][0]
            exo2 = exo2 + stacks2[i][-1:][0]
        print(f"exo1={exo1} exo2={exo2}")

main("05/input.txt")