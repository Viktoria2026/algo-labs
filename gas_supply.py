def check_gas_supply(cities, storages, pipes):
    graph = {}
    for u, v in pipes:
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
        
    result = []

    for storage in storages:
        visited = set()
        stack = [storage] 
        visited.add(storage)
        
        while stack:
            current = stack.pop() 
            
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        unreachable_cities = []
        for city in cities:
            if city not in visited:
                unreachable_cities.append(city)

        if unreachable_cities:
            result.append([storage, unreachable_cities])
            
    return result