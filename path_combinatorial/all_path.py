__author__ = 'bunny_gg'
import cvs_reader

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

graph = {'A': ['B', 'C'],
        'B': ['C', 'D'],
        'C': ['D'],
        'D': ['C'],
        'E': ['F'],
        'F': ['C']}

# print find_all_paths(graph, 'A', 'D')

# r = cvs_reader.csv_to_node("sample.csv")
# g = cvs_reader.nodes_to_graph(r)
# print r
# print g
# print find_all_paths(g,"0","17")