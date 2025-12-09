from operator import itemgetter
import operator


def part1() -> int:
    result: int = 0
    points: list[list[int]] = []
    with open("test.txt", "r") as file:
        for line in file:
            points.append(list(map(int, line.strip().split((",")))))
        file.close()
    n: int = len(points)
    for i in range(0, n):
        for j in range(i + 1, n):
            area: int = get_area(points, i, j)
            result = max(result, area)
    return result


def get_area(points: list[list[int]], i: int, j: int) -> int:
    width: int = max(points[i][0], points[j][0]) - min(points[i][0], points[j][0]) + 1
    height: int = max(points[i][1], points[j][1]) - min(points[i][1], points[j][1]) + 1
    return width * height


def part2() -> int:
    result: int = 0
    points: list[list[int]] = []
    with open("day9.txt", "r") as file:
        for line in file:
            points.append(list(map(int, line.strip().split((",")))))
        file.close()
    n: int = len(points)
    x_dim, y_dim = max(points, key=itemgetter(0))[0] + 1, max(points, key=itemgetter(1))[1] + 1
    cinema_grid: list[list[str]] = build_grid(points, x_dim, y_dim)
    for row in cinema_grid:
        print(row)
    for i in range(0, n):
        for j in range(i + 1, n):
            point1, point2 = points[i], points[j]
            if (cinema_grid[point1[0]][point2[1]] != '.' and cinema_grid[point2[0]][point1[1]] != '.'):
                area: int = get_area(points, i, j)
                result = max(result, area)
    return result


def build_grid(points: list[list[int]], x_dim: int, y_dim: int) -> list[list[str]]:
    matrix: list[list[str]] = [['.' for _ in range(0, y_dim)] for _ in range(0, x_dim)]
    for point in points:
        matrix[point[0]][point[1]] = '#'
    for i in range(0, x_dim):
        start: int = -1
        end: int = -1
        for j in range(0, y_dim):
            if (matrix[i][j] == '#'):
                if (start == -1):
                    start = j
                end = j
        if (start != end):
            for k in range(start + 1, end):
                matrix[i][k] = 'X'
    for j in range(0, y_dim):
        start: int = -1
        end: int = -1
        for i in range(0, x_dim):
            if (matrix[i][j] == '#'):
                if (start == -1):
                    start = i
                end = i
        if (start != end):
            for k in range(start + 1, end):
                matrix[k][j] = 'X'
    for i in range(0, x_dim):
        start: int = -1
        end: int = -1
        for j in range(0, y_dim):
            if (matrix[i][j] != '.'):
                if (start == -1):
                    start = j
                end = j
        if (start != end):
            for j in range(start, end):
                matrix[i][j] = 'X'
    return matrix


if __name__ == "__main__":
    print(part1())
    print(part2())