

def part1() -> int:
    result: int = 0
    input: list[list[str]] = []
    with open("day7.txt", "r") as file:
        for line in file:
            input.append(list(line.strip()))
        file.close()
    n, m = len(input), len(input[0])
    for j in range(0, m):
        if (input[0][j] == 'S'):
            input[1][j] = '|'
            break
    for i in range(2, n, 2):
        for j in range(0, m):
            if (input[i - 1][j] == '|'):
                if (input[i][j] == '^'):
                    result += 1
                    input[i + 1][j - 1] = '|'
                    input[i + 1][j + 1] = '|'
                else:
                    input[i + 1][j] = '|'
    return result


def part2() -> int:
    result: int = 0
    input: list[list[str]] = []
    with open("day7.txt", "r") as file:
        for line in file:
            input.append(list(line.strip()))
        file.close()
    n, m = len(input), len(input[0])
    for j in range(0, m):
        if (input[0][j] == 'S'):
            input[1][j] = '1'
            break
    for i in range(2, n, 2):
        for j in range(0, m):
            if (input[i - 1][j] != '.'):
                if (input[i][j] == '^'):
                    if (input[i + 1][j - 1] == '.'):
                        input[i + 1][j - 1] = input[i - 1][j]
                    else:
                        input[i + 1][j - 1] = str(int(input[i - 1][j]) + int(input[i + 1][j - 1]))
                    if (input[i + 1][j + 1] == '.'):
                        input[i + 1][j + 1] = input[i - 1][j]
                    else:
                        input[i + 1][j + 1] = str(int(input[i - 1][j]) + int(input[i + 1][j + 1]))
                else:
                    if (input[i + 1][j] == '.'):
                        input[i + 1][j] = input[i - 1][j]
                    else:
                        input[i + 1][j] = str(int(input[i - 1][j]) + int(input[i + 1][j]))
    for point in input[n - 1]:
        if (point != '.'):
            result += int(point)
    return result


if __name__ == "__main__":
    print(part1())
    print(part2())