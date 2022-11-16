def is_visible(tree_coordinate, lines):
    value_at_coordinate = int(lines[tree_coordinate["y"]][tree_coordinate["x"]])
    # visible par le haut
    is_visible_top = True
    for y in range(0, tree_coordinate["y"]):
        if int(lines[y][tree_coordinate["x"]]) >= value_at_coordinate:
            is_visible_top = False
    # visible par la droite
    is_visible_right = True
    for x in range(tree_coordinate["x"]+1, len(lines[0])):
        if int(lines[tree_coordinate["y"]][x]) >= value_at_coordinate:
            is_visible_right = False
    # visible par le bas
    is_visible_bottom = True
    for y in range(tree_coordinate["y"]+1, len(lines)):
        if int(lines[y][tree_coordinate["x"]]) >= value_at_coordinate:
            is_visible_bottom = False
    # visible par la gauche
    is_visible_left = True
    for x in range(0, tree_coordinate["x"]):
        if int(lines[tree_coordinate["y"]][x]) >= value_at_coordinate:
            is_visible_left = False
    
   #print(f"{value_at_coordinate} is_visible_left: {is_visible_left} is_visible_top: {is_visible_top} is_visible_right: {is_visible_right} is_visible_bottom: {is_visible_bottom}")
    
    return is_visible_top or is_visible_left or is_visible_right or is_visible_bottom

def main(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
        visible_count_exterior = len(lines)*2 + (len(lines[0])-2)*2
        visible_count_interior = 0
        for y in range(1, len(lines)-1):
            for x in range(1, len(lines[y])-1):
                visible = is_visible({"x": x, "y": y}, lines)
                if visible:
                    visible_count_interior += 1
    
    print(f"visible_count_exterior: {visible_count_exterior}")
    print(f"visible_count_interior: {visible_count_interior}")
    print(f"total: {visible_count_exterior + visible_count_interior}")

main("day08/input.txt")