def count_power_groups(stations, lines):
    """
    Count how many connected groups of power stations exist.

    stations: list of station name strings.
    lines: list of (a, b) pairs, meaning there is an undirected line between a and b.

    Return: integer number of connected components (groups) in the network.
    """

    # Step 1: Build graph (adjacency list)
    graph = {s: [] for s in stations}

    for a, b in lines:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    groups = 0

    # Step 2: DFS/BFS to explore each component
    for station in stations:
        if station not in visited:
            groups += 1
            stack = [station]   # you can also use queue

            while stack:
                curr = stack.pop()
                if curr in visited:
                    continue
                visited.add(curr)

                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        stack.append(neighbor)

    return groups
