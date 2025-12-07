import re


def part1() -> int:
    result: int = 0
    file_contents: list[str] = []
    with open("day6.txt", "r") as file:
        for line in file:
            file_contents.append(line.strip("\n"))
        file.close()
    n: int = len(file_contents)
    numbers: list[list[int]] = []
    operations: list[str] = []
    for i in range(0, n - 1):
        numbers.append(list(map(int, re.split(r" +", file_contents[i]))))
    operations = re.split(r" +", file_contents[n - 1])
    m: int = len(numbers)
    o: int = len(numbers[0])
    for i in range(0, o):
        solution: int = 0
        for j in range(0, m):
            if (operations[i] == '+' or solution == 0):
                solution += numbers[j][i] 
            else:
                solution *= numbers[j][i]
        result += solution
    return result


def part2() -> int:
    result: int = 0
    file_contents: list[str] = []
    with open("day6.txt", "r") as file:
        for line in file:
            file_contents.append(line.replace("\n", ""))
        file.close()
    columns: list[list[str]] = column_collector(file_contents)
    operations: list[str] = re.split(r" +", file_contents[len(file_contents) - 1])
    for x, column in enumerate(columns):
        col_res: int = 0
        for row in column:
            number: int = 0
            for ch in row:
                if (ch != ' '):
                    number *= 10
                    number += int(ch)
            if (col_res == 0 or operations[x] == '+'):
                col_res += number
            else:
                col_res *= number
        result += col_res
    return result


def column_collector(file_contents: list[str]) -> list[list[str]]:
    result: list[list[str]] = []
    n, m = len(file_contents), len(file_contents[0])
    empty: bool = True
    column: list[str] = []
    for i in range(0, m):
        empty = True
        rotated_string: str = ""
        for j in range(0, n - 1):
            if (file_contents[j][i] != ' '):
                empty = False
            rotated_string = rotated_string + file_contents[j][i]
        if (not (empty)):
            column.append(rotated_string)
        else:
            result.append(column)
            column = []
    result.append(column)
    return result


if __name__ == "__main__":
    print(part1())
    print(part2())