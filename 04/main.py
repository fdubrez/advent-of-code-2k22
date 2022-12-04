def fully_contains(line):
    data = list(map(lambda x: list(map(lambda y: int(y), x.split("-"))), line.split(",")))
    return (data[0][0] >= data[1][0] and data[0][1] <= data[1][1]) or (data[1][0] >= data[0][0] and data[1][1] <= data[0][1])

def overlap(line):
    data = list(map(lambda x: list(map(lambda y: int(y), x.split("-"))), line.split(",")))
    range1 = range(data[0][0], data[0][1]+1)
    range2 = range(data[1][0], data[1][1]+1)
    intersect = [value for value in range1 if value in range2]
    return len(intersect) > 0

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
    exo1 = len(list(filter(lambda x : x, map(fully_contains, lines))))
    exo2 = len(list(filter(lambda x : x, map(overlap, lines))))
    print(f"exo1={exo1} exo2={exo2}")