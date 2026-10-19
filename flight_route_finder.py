
flights = {
    "Islamabad": [("Lahore", 40), ("Karachi", 90)],
    "Lahore": [("Karachi", 50), ("Peshawar", 30)],
    "Karachi": [("Quetta", 60)],
    "Peshawar": [("Quetta", 70)],
    "Quetta": []
}


def ucs_cheapest_route(graph, start, goal):
    queue = [(0, [start])]
    visited = []
    explored = []

    while queue:
        queue.sort(key=lambda item: item[0])
        cost, path = queue.pop(0)
        city = path[-1]

        if city in visited:
            continue

        visited.append(city)
        explored.append((path, cost))

        print("Explored path:", path, "| Cost:", cost)

        if city == goal:
            print("Total routes explored:", len(explored))
            return path, cost

        for next_city, price in graph.get(city, []):
            if next_city not in visited:
                new_path = path + [next_city]
                new_cost = cost + price
                queue.append((new_cost, new_path))

    print("Total routes explored:", len(explored))
    return None, None


route, total_cost = ucs_cheapest_route(
    flights, "Islamabad", "Quetta"
)

if route:
    print("Cheapest route:", route)
    print("Total ticket cost:", total_cost)
else:
    print("No route found.")
