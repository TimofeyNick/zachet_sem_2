def read_graph_as_list_orient(): # словарь словарей
    N, M = map(int, input().split())
    G = {}
    for i in range(M):
        a, b, weight = input().split()
        weight = float(weight)
        if a not in G:
            G[a] = {b:weight}
        else:
            G[a][b] = weight
        # if b not in G: # если неориентированный
        #     G[b] = {a: weight}
        # else:
        #     G[b][a] = weight
    return G

def deikstra(G, start):
    d = {v: float('+inf') for v in G}
    d[start] = 0
    used = set()
    used.add(start)
    paths = {v: [] for v in G}
    paths[start].append(start)
    while len(used) != len(d):
        min_d = float('+inf')
        for v in d: # поиск вершины с минимальной длинной от начальной
            if d[v] < min_d:
                current = v
                min_d = d[v]
        for neig in G[current]: # релаксация расстояний от текущей вершины и последующее добавление её в used
            l = d[current] + G[current][neig]
            if l < d[neig]:
                paths[neig] = paths[current] + [neig]
                d[neig] = l
        used.add(current)
    return d

G = read_graph_as_list_orient()
print(deikstra(G, '0'))

# def deikstra(G, start): предыдущий год, косячная?? реализация Хирьянова
#     sh_path = {vertex:float('+inf') for vertex in G}
#     paths={v:[] for v in G}
#     paths[start].append(start)
#     sh_path[start]=0
#     Queue=[start]
#     while Queue:
#         current = Queue.pop(0) # Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
#         for neig in G[current]:
#             offer = sh_path[current]+G[current][neig]
#             if offer < sh_path[neig]:
#                 paths[neig] = paths[current] + [neig]
#                 sh_path[neig] = offer
#                 Queue.append(neig)
#     return paths

# 4 4
# 0 1 3
# 1 2 4
# 1 3 10
# 2 3 46