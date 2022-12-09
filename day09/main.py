from functools import wraps
import time

def timer(func):
    @wraps(func)
    def wrapper(*args):
        start_time = time.time();
        retval = func(*args)
        print("the function ends in ", time.time()-start_time, "secs")
        return retval
    return wrapper

@timer
def main(filename):
    with open(filename) as file:
        moves = [line.rstrip() for line in file]
        coordinates = {
            "head": {
                "x": 0,
                "y": 0
            },
            "tail": {
                "x": 0,
                "y": 0
            }
        }
        tail_positions = set()

        # add starting tail position
        tail_positions.add(f"{coordinates['tail']['x']},{coordinates['tail']['y']}")

        for move in moves:
            direction, steps = move[:1], int(move[2:])
            # move right
            if direction == "R":
                coordinates["head"]["x"] += steps
                if coordinates["head"]["y"] != coordinates["tail"]["y"]:
                    if steps > 1:
                        coordinates["tail"]["y"] = coordinates["head"]["y"]
                        coordinates["tail"]["x"] += 1
                        tail_positions.add(f"{coordinates['tail']['x']},{coordinates['tail']['y']}")
                for step in range(coordinates["tail"]["x"], coordinates["head"]["x"]-1):
                    coordinates["tail"]["x"] += 1
                    tail_positions.add(f"{coordinates['tail']['x']},{coordinates['tail']['y']}")
            # move up
            elif direction == "U":
                coordinates["head"]["y"] -= steps
                if coordinates["head"]["x"] != coordinates["tail"]["x"]:
                    if steps > 1:
                        coordinates["tail"]["x"] = coordinates["head"]["x"]
                        coordinates["tail"]["y"] -= 1
                        tail_positions.add(f"{coordinates['tail']['x']},{coordinates['tail']['y']}")
                for step in range(coordinates["head"]["y"], coordinates["tail"]["y"]-1):
                    coordinates["tail"]["y"] -= 1
                    tail_positions.add(f"{coordinates['tail']['x']},{coordinates['tail']['y']}")
            # move left
            elif direction == "L":
                coordinates["head"]["x"] -= steps
                if coordinates["head"]["y"] != coordinates["tail"]["y"]:
                    if steps > 1:
                        coordinates["tail"]["y"] = coordinates["head"]["y"]
                        coordinates["tail"]["x"] -= 1
                        tail_positions.add(f"{coordinates['tail']['x']},{coordinates['tail']['y']}")
                for step in range(coordinates["head"]["x"], coordinates["tail"]["x"]-1):
                    coordinates["tail"]["x"] -= 1
                    tail_positions.add(f"{coordinates['tail']['x']},{coordinates['tail']['y']}")
            # move down
            elif direction == "D":
                coordinates["head"]["y"] += steps
                if coordinates["head"]["x"] != coordinates["tail"]["x"]:
                    if steps > 1:
                        coordinates["tail"]["x"] = coordinates["head"]["x"]
                        coordinates["tail"]["y"] += 1
                        tail_positions.add(f"{coordinates['tail']['x']},{coordinates['tail']['y']}")
                for step in range(coordinates["tail"]["y"], coordinates["head"]["y"]-1):
                    coordinates["tail"]["y"] += 1
                    tail_positions.add(f"{coordinates['tail']['x']},{coordinates['tail']['y']}")
                
        print(coordinates)
        #print(tail_positions)
        print(len(tail_positions))

                    


main("day09/example.txt")
#main("day09/input.txt")