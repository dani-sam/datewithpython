import heapq  # for priority queue


def dijkstra(graph, source):
    # Step 1: Initialize distance and previous
    distance = {vertex: float("inf") for vertex in graph}
    previous = {vertex: None for vertex in graph}
    distance[source] = 0

    # Step 2: Create priority queue
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, u = heapq.heappop(priority_queue)

        # Skip if this vertex is already processed with a smaller distance
        if current_distance > distance[u]:
            continue

        # Step 3: Check all neighbors
        for neighbor, weight in graph[u].items():
            alt = distance[u] + weight

            # If found a shorter path, update
            if alt < distance[neighbor]:
                distance[neighbor] = alt
                previous[neighbor] = u
                heapq.heappush(priority_queue, (alt, neighbor))

    return distance, previous


# --- Input Graph (Your Values) ---
graph = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "D": 3},
    "C": {"A": 2, "D": 1},
    "D": {"B": 3, "C": 1, "E": 5},
    "E": {"D": 5},
}

# --- Run Algorithm ---
source = "A"
distances, previous = dijkstra(graph, source)

# --- Output ---
print("Shortest Distances from Source", source)
for vertex in distances:
    print(f"{source} → {vertex} = {distances[vertex]}")

print("\nPrevious Vertices:")
for vertex in previous:
    print(f"{vertex} ← {previous[vertex]}")
