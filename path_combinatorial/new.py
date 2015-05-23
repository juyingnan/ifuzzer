__author__ = 'bunny_gg'
import cvs_reader
import all_path
import node
import rule_combine
import rule_path

csv_file_name = "long.csv"
criteria = "P"

def cut_nodes(nodes):
    no_criteria = ["E", "F", "X"]
    for n in nodes:
        if n.interaction in no_criteria:
            for x in nodes:
                if n.name in x.toNodes:
                    x.toNodes.remove(n.name)
            nodes.remove(n)
        cut_parameters(n.headers)
        cut_parameters(n.body)

def cut_sub_paths(nodes):
    no_criteria = ["E", "F", "X"]
    for n in nodes[::-1]:
        to_remove_nodes=[]
        to_remove_sub_paths=[]
        for sub_path in n.sub_paths[::-1]:
            if sub_path.interaction in no_criteria:
                n.toNodes.remove(sub_path.to_node)
                n.sub_paths.remove(sub_path)
        cut_parameters(n.headers)
        cut_parameters(n.body)

def cut_parameters(parameters):
    no_criteria = ["E", "F", "X", "N"]
    for p in parameters[::-1]:
        if p.interaction in no_criteria:
            parameters.remove(p)


def find_test_paths(filename):
    nodes = cvs_reader.csv_to_nodes(csv_file_name)
    cut_sub_paths(nodes)
    graph = cvs_reader.nodes_to_graph(nodes)
    # print graph
    paths = all_path.find_all_paths(graph, nodes[0], nodes[nodes.__len__()-1])
    # print paths

    # print all paths new
    old.print_all_paths(paths, "allpath_new.log")

    results = old.paths_filter(paths)

    old.print_result(results)

#find_test_paths(csv_file_name)

import time
import old
start = time.time()
#old.find_test_paths(csv_file_name)
end = time.time()
print "old: ", end-start
start = time.time()
find_test_paths(csv_file_name)
end = time.time()
print "new: ", end-start