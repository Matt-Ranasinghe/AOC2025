def part1() -> int:
    position: int = 50
    result: int = 0
    with open("day1.txt", "r") as file:
        for line in file:
            goRight: bool = (line[0] == 'R')
            movement: int = int(line[1::].strip())
            if (goRight):
                position += movement
                if (position > 99):
                    position %= 100
            else:
                position -= movement
                if (position < 0):
                    position %= 100
            if (position == 0):
                result += 1
    return result


def part2() -> int:
    position: int = 50
    result: int = 0
    with open("day1.txt", "r") as file:
        for line in file:
            goRight: bool = (line[0] == 'R')
            movement: int = int(line[1::].strip())
            if (goRight):
                position += movement
                result += position // 100
                position %= 100
            else:
                position -= movement
                if (position + movement == 0):
                    result -= 1
                result += (-position // 100) + 1
                position %= 100
    return result


if __name__ == "__main__":
    print(part1())
    print(part2())
