def dijkstra_logistik(graph, depot): 
    """Shortest path dari depot. Big-O: O(V^2+E).""" 
    INF = float('inf') 
    dist = {v: INF for v in graph.adj} 
    parent = {v: None for v in graph.adj} 
    dist[depot] = 0 
    visited = set() 
    # TODO: implementasikan
    return dist, parent 