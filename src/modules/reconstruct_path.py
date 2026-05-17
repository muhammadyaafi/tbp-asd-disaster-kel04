def reconstruct_path(parent, tujuan):

    path = []

    while tujuan:
        path.append(tujuan)
        tujuan = parent[tujuan]

    path.reverse()

    return path