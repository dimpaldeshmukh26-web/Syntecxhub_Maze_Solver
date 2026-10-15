import heapq

maze = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(maze, start, goal):
    rows = len(maze)
    cols = len(maze[0])

    open_list = [(0, start)]
    came_from = {}
    g_score = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        r, c = current

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < rows and 0 <= nc < cols):
                continue

            if maze[nr][nc] == 1:
                continue

            tentative_g = g_score[current] + 1

            if tentative_g < g_score.get((nr, nc), float("inf")):
                neighbor = (nr, nc)
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g

                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor))

    return None


path = astar(maze, start, goal)

if path:
    print("Maze solved!")
    print("Shortest path:", path)
    print("Path length:", len(path) - 1)

    print("\nMaze visualization:")
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if (r, c) == start:
                print("S", end=" ")
            elif (r, c) == goal:
                print("G", end=" ")
            elif (r, c) in path:
                print("*", end=" ")
            elif maze[r][c] == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No path found!")