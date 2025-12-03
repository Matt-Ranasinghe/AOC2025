import os

def part1() -> str:
    with open("test.txt", "r") as file:
        contents: str = file.read()
        components: list[str] = contents.strip().split(',')
        return components[0]

if __name__ == "__main__":
    print(os.getcwd())
    print(part1())
