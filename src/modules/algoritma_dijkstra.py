def dijkstra_logistik(graph, depot): 
    """Shortest path dari depot. Big-O: O(V^2+E).""" 
    INF = float('inf') 
    dist = {v: INF for v in graph._adj} # Jarak awal semua node = tak hingga
    parent = {v: None for v in graph._adj} # Parent untuk rekonstruksi jalur
    dist[depot] = 0 # Jarak depot ke dirinya sendiri = 0
    visited = set() # Menyimpan node yang sudah diproses
    # TODO: implementasikan

    while len(visited) < len(graph._adj):

        # Cari node belum dikunjungi
        # dengan jarak minimum
        current = None
        current_dist = INF

        for node in graph._adj:

            if node not in visited and dist[node] < current_dist:
                current = node
                current_dist = dist[node]

        # Jika tidak ada node terjangkau lagi
        if current is None:
            break

        # Tandai sudah dikunjungi
        visited.add(current)

        # Traversal tetangga current
        edge = graph._adj[current]

        while edge:

            neighbor = edge.dest
            weight = edge.jarak

            # Relaxation
            new_dist = dist[current] + weight

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = current

            edge = edge.next

    return dist, parent