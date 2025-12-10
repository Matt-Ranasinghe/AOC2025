from queue import Queue


def part1() -> int:
    result: int = 0
    buttons: list[str] = []
    changes: list[list[list[int]]] = []
    file_input: list[list[str]] = []
    with open("day10.txt", "r") as file:
        for line in file:
            file_input.append(line.strip().replace("(", "").replace(")", "").split(" "))
        file.close()
    for file_line in file_input:
        buttons.append(file_line[0].replace("[", "").replace("]", ""))
        changes.append(get_changes(file_line))
    n: int = len(file_input)
    for i in range(0, n):
        result += shortest_path(buttons[i], changes[i])
    return result


def shortest_path(buttons: str, changes: list[list[int]]) -> int:
    # Should have done this with a bit mask, but oh well.
    seen: set[str] = set()
    queue: Queue[str] = Queue()
    empty: str = "".join(["." for _ in range(0, len(buttons))])
    queue.put(empty)
    seen.add(empty)
    new_queue: Queue[str] = Queue()
    count: int = 1
    while (not (queue.empty())):
        button_config: list[str] = list(queue.get().strip())
        for change in changes:
            copy: list[str] = button_config.copy()
            for num in change:
                if (copy[num] == '#'):
                    copy[num] = '.'
                else:
                    copy[num] = '#'
            copy_str: str = "".join(copy)
            if (copy_str == buttons):
                return count
            elif (not (copy_str in seen)):
                seen.add(copy_str)
                new_queue.put(copy_str)
        if (queue.empty()):
            queue = new_queue
            new_queue = Queue()
            count += 1
    return count


def get_changes(file_input: list[str]) -> list[list[int]]:
    result: list[list[int]] = []
    for i in range(1, len(file_input) - 1):
        switched_buttons: list[int] = list(map(int, file_input[i].split(",")))
        result.append(switched_buttons)
    return result


def part2() -> int:
    result: int = 0
    buttons: list[list[int]] = []
    changes: list[list[list[int]]] = []
    file_input: list[list[str]] = []
    with open("day10.txt", "r") as file:
        for line in file:
            file_input.append(line.strip().replace("(", "").replace(")", "").split(" "))
        file.close()
    for file_line in file_input:
        buttons.append(list(map(int, file_line[-1].replace("{", "").replace("}", "").split(","))))
        changes.append(get_changes(file_line))
    n: int = len(file_input)
    for i in range(0, n):
        result += shortest_path_power(buttons[i], changes[i])
    return result


def shortest_path_power(buttons: list[int], changes: list[list[int]]) -> int:
    seen: set = set()
    queue: Queue = Queue()
    empty: tuple = tuple([0 for _ in range(0, len(buttons))])
    queue.put(empty)
    seen.add(empty)
    new_queue: Queue = Queue()
    count = 1
    while (not (queue.empty())):
        state: tuple = queue.get()
        for change in changes:
            new_state: list[int] = list(state)
            for num in change:
                new_state[num] += 1
                if (new_state[num] > buttons[num]):
                    continue
            if (new_state == buttons):
                return count
            new_state_tup: tuple = tuple(new_state)
            if (not (new_state_tup in seen)):
                seen.add(new_state_tup)
                new_queue.put(new_state_tup)
        if (queue.empty()):
            queue = new_queue
            new_queue = Queue()
            count += 1
    return count


if __name__ == "__main__":
    print(part1())
    print(part2())