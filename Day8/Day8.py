def part1() -> int:
    result: int = 0
    nodes: list[list[int]] = []
    with open("day8.txt", "r") as file:
        for line in file:
            nodes.append(list(map(int, line.strip().split(','))))
        file.close()
    n: int = len(nodes)
    distances: list[tuple[int, int, int]] = []
    for i, (x0, y0, z0) in enumerate(nodes):
        for j in range(i+1, n):
            x1, y1, z1 = nodes[j]
            d2 = (x0 - x1)**2 + (y0 - y1)**2 + (z0 - z1)**2
            distances.append((d2, i, j))
    distances.sort(key=lambda x: x[0])
    neighbours = [i for i in range(0, n)]
    for i in range(0, 1000):
        union(distances[i][1], distances[i][2], neighbours)
    max_sizes = [0] * n
    for i in range(0, n):
        root = find(i, neighbours)
        max_sizes[root] += 1
    result = multiply(sorted(max_sizes, reverse=True)[:3])
    return result


def find(node: int, neighbours: list[int]) -> int:
    if neighbours[node] != node:
        neighbours[node] = find(neighbours[node], neighbours)
    return neighbours[node]


def union(i: int, j: int, neighbours: list[int]) -> None:
    i_parent: int = find(i, neighbours)
    j_parent: int = find(j, neighbours)
    neighbours[i_parent] = j_parent


def multiply(max_three: list[int]) -> int:
    result: int = 1
    for num in max_three:
        result *= num
    return result


def part2() -> int:
    nodes: list[list[int]] = []
    with open("day8.txt", "r") as file:
        for line in file:
            nodes.append(list(map(int, line.strip().split(','))))
        file.close()
    n: int = len(nodes)
    parents: list[int] = [i for i in range(0, n)]
    distances: list[tuple[int, int, int]] = []
    for i, (x0, y0, z0) in enumerate(nodes):
        for j in range(i+1, n):
            x1, y1, z1 = nodes[j]
            d2 = (x0 - x1)**2 + (y0 - y1)**2 + (z0 - z1)**2
            distances.append((d2, i, j))
    distances.sort(key=lambda x: x[0])
    count: int = 0
    while (n > 1):
        if (find(distances[count][1], parents) != find(distances[count][2], parents)):
            n -= 1
            union(distances[count][1], distances[count][2], parents)
            if (n == 1):
                return nodes[distances[count][1]][0] * nodes[distances[count][2]][0]
        count += 1
    return -1


if __name__ == '__main__':
    print(part1())
    print(part2())