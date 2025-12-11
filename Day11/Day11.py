def part1() -> int:
    result: int = 0
    connections: dict[str, list[str]] = {}
    with open("day11.txt", "r") as file:
        for line in file:
            server, links = line.strip().split(":")
            links_list = links.strip().split()
            connections[server] = links_list
        file.close()
    visited: dict[str, int] = {}
    result = DFS("you", connections, visited)
    return result


def DFS(server: str, connections: dict[str, list[str]], visited: dict[str, int]) -> int:
    if (server == "out"):
        return 1
    if (server in visited):
        return visited[server]
    result: int = 0
    for connection in connections[server]:
        result += DFS(connection, connections, visited)
    visited[server] = result
    return result


def part2() -> int:
    result: int = 0
    connections: dict[str, list[str]] = {}
    with open("day11.txt", "r") as file:
        for line in file:
            server, links = line.strip().split(":")
            links_list = links.strip().split()
            connections[server] = links_list
        file.close()
    visited: dict[tuple[str, int], int] = {}
    result = DFS_part2("svr", connections, visited, 0)
    return result


def DFS_part2(server: str, connections: dict[str, list[str]], visited: dict[tuple[str, int], int], seen: int) -> int:
    need_server: int = seen
    if (server == "out"):
        return 1 if seen == 3 else 0
    if (server == "fft"):
        need_server += 1
    elif (server == "dac"):
        need_server += 2
    if ((server, need_server) in visited):
        return visited[(server, need_server)]
    result: int = 0
    for connection in connections[server]:
        result += DFS_part2(connection, connections, visited, need_server)
    visited[(server, need_server)] = result
    return result


if __name__ == "__main__":
    print(part1())
    print(part2())