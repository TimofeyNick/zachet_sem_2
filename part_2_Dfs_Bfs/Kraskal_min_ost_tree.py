def kraskal(): # остовное дерево мин. суммарного веса
    N, M = map(int, input().split())
    edges = []
    for i in range(N):
        v1, v2, w = map(int, input().split())
        edges.append((w, v1, v2))
    edges.sort()

    colour = [x for x in range(N)]
    tree = []
    tree_weight = 0
    for w, v1, v2 in edges:
        if colour[v1] != colour[v2]:
            tree.append((v1, v2))
            tree_weight += w
            for j in range(N):
                if colour[j] == colour[v2] and v2 != j:
                    colour[j] = colour[v1]
            colour[v2] = colour[v1]
    print(tree)

kraskal()