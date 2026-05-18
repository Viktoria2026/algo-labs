def solve_max_flow(filename):
    graph = {}
    original_capacities = {} 
    def add_edge(u, v, cap):
        if u not in graph: graph[u] = {}
        if v not in graph: graph[v] = {}
        graph[u][v] = graph[u].get(v, 0) + cap
        if u not in graph[v]: graph[v][u] = 0

        if cap != float('inf'):
            original_capacities[(u, v)] = original_capacities.get((u, v), 0) + cap
            
        if u not in graph[v]: graph[v][u] = 0

    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    if not lines: return 0
    
    farms = [name.strip() for name in lines[0].split(',')]
    shops = [name.strip() for name in lines[1].split(',')]
    source = "SuperSource"
    sink = "SuperSink"

    for farm in farms:
        add_edge(source, farm, float('inf'))

    for shop in shops:
        add_edge(shop, sink, float('inf'))

    for i in range(2, len(lines)):
        parts = lines[i].split(',')
        if len(parts) >= 3:
            u, v, cap = parts[0].strip(), parts[1].strip(), int(parts[2].strip())
            add_edge(u, v, cap)

    max_flow = 0 

    while True:
        parent = {node: None for node in graph}
        queue = [source]
        path_found = False
        
        while queue:
            u = queue.pop(0)
            if u == sink:
                path_found = True
                break
            for v, cap in graph.get(u, {}).items():
                if parent.get(v) is None and cap > 0:
                    parent[v] = u
                    queue.append(v)
        
        if not path_found:
            break
            
        path_flow = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = u

        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u
            
    return max_flow, graph, original_capacities