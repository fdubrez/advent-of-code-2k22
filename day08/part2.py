from functools import reduce

def scenic_score(tree_coordinate, lines):
    value_at_coordinate = int(lines[tree_coordinate["y"]][tree_coordinate["x"]])
    # visible par le haut
    visible_top = 0
    for y in reversed(range(0, tree_coordinate["y"])):
        visible_top += 1
        if int(lines[y][tree_coordinate["x"]]) >= value_at_coordinate:
            break
    # visible par la droite
    visible_right = 0
    for x in range(tree_coordinate["x"]+1, len(lines[0])):
        visible_right += 1
        if int(lines[tree_coordinate["y"]][x]) >= value_at_coordinate:
            break
    # visible par le bas
    visible_bottom = 0
    for y in range(tree_coordinate["y"]+1, len(lines)):
        visible_bottom += 1
        if int(lines[y][tree_coordinate["x"]]) >= value_at_coordinate:
            break
    # visible par la gauche
    visible_left = 0
    for x in reversed(range(0, tree_coordinate["x"])):
        visible_left += 1
        if int(lines[tree_coordinate["y"]][x]) >= value_at_coordinate:
            break
    
   #print(f"{value_at_coordinate} is_visible_left: {is_visible_left} is_visible_top: {is_visible_top} is_visible_right: {is_visible_right} is_visible_bottom: {is_visible_bottom}")
    
    return visible_top * visible_left * visible_right * visible_bottom

def main(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
        visible_count_exterior = len(lines)*2 + (len(lines[0])-2)*2
        scenic_scores = []
        for y in range(1, len(lines)-1):
            for x in range(1, len(lines[y])-1):
                scenic_scores.append(scenic_score({"x": x, "y": y}, lines))
        
        print(f"scenic_scores: {sorted(scenic_scores).pop()}")

main("day08/input.txt")