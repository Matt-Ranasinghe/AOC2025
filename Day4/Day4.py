from queue import Queue


def part1() -> int:
    result: int = 0
    grid: list[list[str]] = []
    with open("day4.txt", "r") as file:
        for line in file:
            grid.append([ch for ch in line.strip()])
        file.close()
    n, m = len(grid), len(grid[0])
    for i in range(0, n):
        for j in range(0, m):
            if (grid[i][j] == '@' and accessible(i, j, grid, n, m)):
                result += 1
    return result


def in_bounds(x: int, y: int, n: int, m: int) -> bool:
    return (x >= 0 and x < n and y >= 0 and y < m)


def accessible(x: int, y: int, grid: list[list[str]], n: int, m: int) -> bool:
    neighbours: int = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i == 0 and j == 0):
                continue
            if (in_bounds(x + i, y + j, n, m) and grid[x + i][y + j] == '@'):
                neighbours += 1
    return neighbours < 4


def part2() -> int:
    result: int = 0
    grid: list[list[str]] = []
    with open("day4.txt", "r") as file:
        for line in file:
            grid.append([ch for ch in line.strip()])
        file.close()
    n, m = len(grid), len(grid[0])
    for i in range(0, n):
        for j in range(0, m):
            if (grid[i][j] == '@'):
                result += BFS(i, j, grid, n, m)
    return result


def BFS(x: int, y: int, grid: list[list[str]], n: int, m: int) -> int:
    removed: int = 0
    queue: Queue[tuple[int, int]] = Queue()
    queue.put((x, y))
    seen: set[tuple[int, int]] = set()
    while (not (queue.empty())):
        coordinates: tuple[int, int] = queue.get()
        if (coordinates in seen):
            continue
        if (accessible(coordinates[0], coordinates[1], grid, n, m)):
            seen.add(coordinates)
            removed += 1
            neighbours: list[tuple[int, int]] = neighbour_finder(coordinates[0], coordinates[1], grid, n, m)
            for neighbour in neighbours:
                queue.put(neighbour)
            grid[coordinates[0]][coordinates[1]] = '.'
    return removed


def neighbour_finder(x: int, y: int, grid: list[list[str]], n: int, m: int) -> list[tuple[int, int]]:
    neighbours: list[tuple[int, int]] = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i == 0 and j == 0):
                continue
            if (in_bounds(x + i, y + j, n, m) and grid[x + i][y + j] == '@'):
                neighbours.append((x + i, y + j))
    return neighbours


if __name__ == "__main__":
    print(part1())
    print(part2())
