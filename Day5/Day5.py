

def part1() -> int:
    result: int = 0
    with open("day5.txt", "r") as file:
        file_contents = file.read()
    components: list[str] = file_contents.split("\n")
    dates, ranges = extract_dates(components)
    for date in dates:
        result += binary_search(date, ranges)
    return result


def binary_search(date: int, ranges: list[tuple[int, int]]) -> int:
    left, right = 0, len(ranges) - 1
    choice: int = -1
    while (left <= right):
        mid: int = left + (right - left) // 2
        if (ranges[mid][0] < date):
            left = mid + 1
            choice = mid
        elif (ranges[mid][0] > date):
            right = mid - 1
        else:
            return 1
    if (choice != -1):
        return 1 if ranges[choice][1] >= date else 0
    return 0


def extract_dates(components: list[str]) -> tuple[list[int], list[tuple[int, int]]]:
    date_ranges: list[tuple[int, int]] = []
    dates: list[int] = []
    for i in range(0, len(components)):
        if (components[i] == ""):
            dates = list(map(int, components[i + 1::]))
            break
        start, end = components[i].split('-')
        date_ranges.append((int(start), int(end)))
    return dates, optimise_ranges(date_ranges)


def optimise_ranges(date_ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    date_ranges.sort()
    simplified_ranges: list[tuple[int, int]] = []
    count: int = 0
    n: int = len(date_ranges)
    while (count < n):
        better_tuple: tuple[int, int] = (0, 0)
        start: int = date_ranges[count][0]
        end: int = date_ranges[count][1]
        temp: int = count + 1
        for j in range(count + 1, n):
            if (date_ranges[j][0] <= end):
                end = max(end, date_ranges[j][1])
            else:
                better_tuple = (start, end)
                break
            temp += 1
        if better_tuple == (0, 0):
            better_tuple = (start, end)
        count = temp
        simplified_ranges.append(better_tuple)
    return simplified_ranges


def part2() -> int:
    result: int = 0
    with open("day5.txt", "r") as file:
        file_contents = file.read()
    components: list[str] = file_contents.split("\n")
    _, ranges = extract_dates(components)
    for date_range in ranges:
        result += (date_range[1] - date_range[0] + 1)
    return result


if __name__ == "__main__":
    print(part1())
    print(part2())