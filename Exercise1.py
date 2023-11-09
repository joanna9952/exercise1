def print_labyrinth(lab):

    print("   0123456")

    for i, line in enumerate(lab):
        print(f"{i:2} {line}{i:2}")

    print("   0123456")


labyrinth = [
    "███████",
    "█     █",
    "█   ███",
    "█ ███ █",
    "█     █",
    "███████"
]

print_labyrinth(labyrinth)


def prompt_integer(message: str) -> int:

    while True:
        user_input = input(message)
        while user_input.isdigit():
            return int(user_input)
        print("Please enter a number")


def prompt_user_for_location(name: str) -> tuple[int, int]:

    row = prompt_integer(f"Row of {name}: ")
    column = prompt_integer(f"Column of {name}: ")
    return row, column


start_row, start_column = prompt_user_for_location("start")
print(f"Start location - ({start_row},{start_column})")


end_row, end_column = prompt_user_for_location("end")
print(f"End location - ({end_row},{end_column})")

from collections import deque


def bfs(lab, start, end):

    queue = deque([[start]])
    visited = set()

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:

        path = queue.popleft()
        last = path[-1]

        if last == end:
            return path

        if last not in visited:
            visited.add(last)

            for move in moves:
                row, col = last[0] + move[0], last[1] + move[1]
                next_location = (row, col)

                if 0 <= row < len(lab) and 0 <= col < len(lab[0]) and lab[row][col] != '█':
                    queue.append(path + [next_location])

    return []


def is_traversable(lab: list[str], location: tuple[int,int]) -> bool:
    row, col = location
    if 0 <= row < len(lab) and 0 <= col < len(lab[0]) and lab[row][col] == ' ':
        return True
    else:
        return False


path = bfs(labyrinth, (start_row, start_column), (end_row, end_column))


test_locations = path

for location in test_locations:
    result = is_traversable(labyrinth, location)
    print(f"Location {location}: Traversable - {result}")

print("Shortest path from start to end:", path)


def replace_at_index(s: str, r: str, idx: int) -> str:
    return s[:idx] + r + s[idx + len(r):]


def print_labyrinth(lab: list[str], path: list[tuple[int, int]]) -> None:

    print("   0123456")

    for row, line in enumerate(lab):
        if path:
            for element in path:
                if element[0] == row:
                    col = element[1]
                    line = replace_at_index(line, "X", col)
        print(f"{row:2} {line}{row:2}")

    print("   0123456")


print_labyrinth(labyrinth, path)