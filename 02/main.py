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

# <opponent> <you>
rules = {
    "A X": 4, # 3 + 1
    "A Y": 8, # 6 + 2
    "A Z": 3, # 0 + 3
    "B X": 1, # 0 + 1
    "B Y": 5, # 3 + 2 
    "B Z": 9, # 6 + 3
    "C X": 7, # 6 + 1
    "C Y": 2, # 0 + 2
    "C Z": 6, # 3 + 3  
}

# <opponent> <goal>
rules2 = {
    #loose
    "A X": "A Z",
    "B X": "B X",
    "C X": "C Y",
    # draw
    "A Y": "A X",
    "B Y": "B Y",
    "C Y": "C Z",
    # win
    "A Z": "A Y",
    "B Z": "B Z",
    "C Z": "C X",
}

@timer
def run():
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]
        score = 0
        score2 = 0
        for line in lines:
            score += rules[line]
            score2 += rules[rules2[line]]

        print(f"exo1: {score} exo2: {score2}")

run()