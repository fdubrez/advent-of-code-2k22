from functools import wraps, reduce
import time

def timer(func):
    @wraps(func)
    def wrapper(*args):
        start_time = time.time();
        retval = func(*args)
        print("the function ends in ", time.time()-start_time, "secs")
        return retval
    return wrapper


def in_right_order(left, right) -> bool:
    """Returns True if in the right order
    
    >>> in_right_order([1,1,3,1,1], [1,1,5,1,1])
    True
    >>> in_right_order([[1],[2,3,4]], [[1],4])
    True
    >>> in_right_order([9],[[8,7,6]])
    False
    >>> in_right_order([[4,4],4,4],[[4,4],4,4,4])
    True
    >>> in_right_order([7,7,7,7], [7,7,7])
    False
    >>> in_right_order([], [3])
    True
    >>> in_right_order([[[]]], [[]])
    False
    >>> in_right_order([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9])
    False
    """
    for idx, value in enumerate(left):
        left_type = type(value)
        try:
            right_type = type(right[idx])
        except:
            # Right side ran out of items, so inputs are not in the right order
            return False
        right_value = right[idx]
        # both values are integers
        if left_type is int and right_type is int:
            if value <= right_value:
                continue
            else:
                return False
        # both values are lists
        if left_type is list and right_type is list:
            if in_right_order(value, right_value):
                continue
            else:
                return False
        # exactly one value is an integer
        if left_type is int and right_type is list:
            if in_right_order([value], right_value[:1]):
                continue
            else:
                return False
        # exactly one value is an integer #2
        if left_type is list and right_type is int:
            if in_right_order(value[:1], [right_value]):
                continue
            else:
                return False
    
    return True

@timer
def main(filename):
    with open(filename) as file:
        data = list(map(lambda lines: list(map(lambda line: eval(line), lines.split("\n"))), file.read().split("\n\n")))
        
        indexes_in_right_order = []
        for idx, d in enumerate(data):
            # index starts at 1
            index = idx + 1

            if in_right_order(left=d[0], right=d[1]):
                indexes_in_right_order.append(index)
        
        print(indexes_in_right_order)
        print(reduce(lambda a,b: a+b, indexes_in_right_order, 0))


main("day13/input.txt")