def depth_bounded_search(graph, node, goal, bound):
    if node == goal:
        return [node], True
    elif bound == 0:
        return [], False
    else:
        found = False
        for neighbor in graph[node]:
            path, found = depth_bounded_search(graph, neighbor, goal, bound - 1)
            if found:
                return [node] + path, True
        return [], False

def id_depth_search(graph, start_node, goal_node):
    bound = 0
    
    while True:
        path, found = depth_bounded_search(graph, start_node, goal_node, bound)
        
        if found:
            return path
        
        if not found and bound >= len(graph) - 1: # Assuming a connected graph as a worst case to stop increasing the bound.
            break
        
        bound += 1
    
    return []

# Example usage with a sample graph represented as an adjacency list.
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}

# Searching for a path from A to E.
path = id_depth_search(graph,'A','E')
print("Path:", " -> ".join(path) if path else "No Path Found")
