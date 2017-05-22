def read_graph_as_list_no_orient(): # список смежности
    N, M = map(int, input().split())
    graph = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        #graph[b].append(a)
    #
    # for elem in graph:
    #     print(' '.join(map(str, elem)))
    # print()
    transp(N, M, graph)

def transp(N, M, graph):
    graph_1 = [[] for i in range(N)]
    i = 0
    for list_elem in graph:
        for j in list_elem:
            graph_1[j].append(i)
            i += 1

    # for elem in graph_1:
    #     print(' '.join(map(str, elem)))

read_graph_as_list_no_orient()