def part1() -> int:
    result: int = 0
    max_seen: int = 0
    with open("day3.txt", "r") as file:
        for line in file:
            max_seen = 0
            local_max: int = 0 
            for c in line.strip():
                num: int = int(c)
                if (local_max + num > max_seen):
                    max_seen = local_max + num
                if (num * 10 > local_max):
                    local_max = int(c) * 10
            result += max_seen
    return result


def part2() -> int:
    result: int = 0
    with open("day3.txt", "r") as file:
        for line in file:
            num_stack: list[int] = []
            s = line.strip()
            for i, ch in enumerate(s):
                num = int(ch)
                remaining = len(s) - i - 1
                while num_stack and num_stack[-1] < num and (len(num_stack) - 1 + remaining + 1) >= 12:
                    num_stack.pop()
                if len(num_stack) < 12:
                    num_stack.append(num)
            max_val = 0
            for d in num_stack:
                max_val = max_val * 10 + d

            result += max_val

    return result


if __name__ == "__main__":
    print(part1())
    print(part2())