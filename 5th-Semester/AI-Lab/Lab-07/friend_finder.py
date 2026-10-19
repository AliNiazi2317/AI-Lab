
network = {
    "Ali": ["Bilal", "Sara"],
    "Bilal": ["Ali", "Zara"],
    "Sara": ["Ali", "Omar"],
    "Zara": ["Bilal", "Hira"],
    "Omar": ["Sara", "Hira"],
    "Hira": ["Zara"]
}


def bfs_shortest_path(graph, start, goal):
    visited = [start]
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        person = path[-1]

        if person == goal:
            return path

        for neighbour in graph[person]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(path + [neighbour])

    return None


path = bfs_shortest_path(network, "Ali", "Hira")

if path:
    print("Shortest chain from Ali to Hira:", path)
    print("Number of introductions needed:", len(path) - 1)
else:
    print("No connection found.")
