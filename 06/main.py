
def main(filename, count):
    with open(filename) as file:
        lines = [line for line in file]
        line = lines[0]
        chars = []
        processed = 0
        for char in line:
            processed += 1
            chars.append(char)
            last_four = chars[-1*count:]
            if len(last_four) == count and len(set(last_four)) == count:
                break
        print(f"processed: {processed}")

main("06/input.txt", 4)
main("06/input.txt", 14)