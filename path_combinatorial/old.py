__author__ = 'bunny_gg'
import cvs_reader
import all_path
import node
import rule_combine
import rule_path

csv_file_name = "sample.csv"

nodes = cvs_reader.csv_to_nodes(csv_file_name)
graph = cvs_reader.nodes_to_graph(nodes)
print graph
paths = all_path.find_all_paths(graph,nodes[0],nodes[nodes.__len__()-1])
print paths
results = []
for path in paths:
    p = rule_path.rule_operation_path(path)
    if p:
        results.append(p)

for result in results:
    for n in result:
        if isinstance(n, node.node):
            if n.interaction == "P":
                parameters = []
                parameters.extend(n.headers)
                parameters.extend(n.body)
                parameter_combine = rule_combine.rule_operation_combine(parameters)
                result.append(parameter_combine)

for result in results:
    r = []
    for n in result:
        if isinstance(n, node.node):
            r.append(n.name)
        if isinstance(n, list):
            # r.append(n)
            parameter_list = []
            for item in n:
                tmp = ""
                for i in item:
                    tmp = tmp + "+" + str(i)
                parameter_list.append(tmp)
            r.append(parameter_list)
    print r