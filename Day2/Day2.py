from turtle import st


def part1() -> int:
    result: int = 0
    with open("day2.txt", "r") as file:
        contents: str = file.read()
        components: list[str] = contents.strip().replace("\n", "").split(',')
        for component in components:
            start, end = map(int, component.split('-'))
            result += duplicated_half_numbers_in_range(start, end)
        file.close()
    return result

def duplicated_half_numbers_in_range(start: int, end: int) -> int:
    result: int = 0
    start_str, end_str = str(start), str(end)
    for L in range(len(start_str), len(end_str) + 1):
        if L % 2 == 1:
            continue
        H = L // 2
        start_num = max(start, 10**(L-1))
        end_num   = min(end, 10**L - 1)
        min_half = 10**(H-1)
        max_half = 10**H - 1
        for h in range(min_half, max_half + 1):
            sym = int(str(h) + str(h))
            if sym < start_num:
                continue
            if sym > end_num:
                break
            result += sym
    return result


def part2() -> int:
    result: int = 0
    with open("test.txt", "r") as file:
        contents: str = file.read()
        components: list[str] = contents.strip().replace("\n", "").split(',')
        for component in components:
            start_str, end_str = component.split('-')
            start_int, end_int = int(start_str), int(end_str)
            seen: set[int] = set()
            for L in range(len(start_str), len(end_str) + 1):
                s_L = max(start_int, 10 ** (L - 1))
                e_L = min(end_int, 10 ** L - 1)
                if s_L > e_L:
                    continue
                factors: set[int] = factor_finder(L)
                for factor in factors:
                    output: tuple[int, set[int]] = find_numerical_repetition(s_L, e_L, factor, L, seen)
                    result += output[0]
                    seen = output[1]
        file.close()
    return result

def factor_finder(length: int) -> set[int]:
    if length <= 1:
        return set()
    divisors: set[int] = set()
    for f in range(1, length):
        if length % f == 0:
            divisors.add(f)
    return divisors

def find_numerical_repetition(start: int, end: int, factor: int, length: int, seen: set[int]) -> tuple[int, set[int]]:
    result = 0
    if factor <= 0 or length % factor != 0 or factor >= length:
        return (0, seen)

    repeats = length // factor
    min_block = 10 ** (factor - 1)
    max_block = 10 ** factor - 1
    for b in range(min_block, max_block + 1):
        candidate = int(str(b) * repeats)
        if candidate < start:
            continue
        if candidate > end:
            break
        if candidate not in seen:
            seen.add(candidate)
            result += candidate
    return (result, seen)


if __name__ == "__main__":
    print(part1())
    print(part2())