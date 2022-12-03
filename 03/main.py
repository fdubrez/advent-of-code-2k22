from functools import reduce
import string

priorities = {}
index = 0
for letter in string.ascii_lowercase:
    priorities[letter] = index+1
    index += 1
index= 26
for letter in string.ascii_uppercase:
    priorities[letter] = index + 1
    index += 1

def priority(line):
    half = len(line)//2
    compartment1 = line[:half]
    compartment2 = line[half:]
    intersect = [value for value in compartment1 if value in compartment2]
    return priorities[intersect[0]]

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def group_priority(chunk):
    intersect = [value for value in chunk[0] if value in chunk[1] and value in chunk[2]]
    #print(f"intersect: {intersect}")
    return priorities[intersect[0]]

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
    exo1 = reduce(lambda a,b: a+b, map(priority, lines))
    print(f"exo1: {exo1}")
    exo2 = reduce(lambda a,b: a+b, map(group_priority, chunks(lines, 3)))
    print(f"exo2: {exo2}")
