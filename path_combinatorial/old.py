__author__ = 'bunny_gg'
import cvs_reader
import all_path
import node
import rule_combine
import rule_path

csv_file_name = "sample.csv"
criteria = "P"

def print_all_paths(paths, output_file_path):
    f = open(output_file_path, "w")
    for result in paths:
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
                        tmp = tmp + " + " + str(i)
                    parameter_list.append(tmp[3:])
                r.append(parameter_list)
        print >> f, r

def get_sub_paths_from_path(long_path):
    result = []
    for i in range(0, len(long_path)-1):
        result.append(long_path[i].find_path(long_path[i+1].name))
    return result

def find_test_paths(filename):
    nodes = cvs_reader.csv_to_nodes(filename)
    graph = cvs_reader.nodes_to_graph(nodes)
    # print graph
    paths = all_path.find_all_paths(graph, nodes[0], nodes[nodes.__len__()-1])
    # print paths

    # print all paths old
    print_all_paths(paths, "allpath_old.log")

    results = paths_filter(paths)

    print_result(results)


def print_result(results):
    # print result
    for result in results:
        r = []
        for n in result:
            if isinstance(n, node.node):
                r.append(n.name)
            if isinstance(n, dict):
                # r.append(n)
                parameter_list = []
                parameter_list.append(n.keys())
                for item in n.values()[0]:
                    tmp = ""
                    for i in item:
                        tmp = tmp + " + " + str(i)
                    parameter_list.append(tmp[3:])
                r.append(parameter_list)
        print r


def paths_filter(paths):
    results = []
    for path in paths:
        sub_paths = get_sub_paths_from_path(path)
        p = rule_path.rule_operation_path(sub_paths)
        if p:
            results.append(path)
    for result in results:
        sub_paths = get_sub_paths_from_path(result)
        sub_paths_in_criteria = [sub_path for sub_path in sub_paths if sub_path.interaction == criteria]
        nodes_in_criteria = [node for node in result if node.interaction == criteria]
        for sub_path in sub_paths_in_criteria:
            for n in nodes_in_criteria:
                if n.name == sub_path.from_node:
                    parameters = []
                    parameters.extend(n.headers)
                    parameters.extend(n.body)
                    parameter_combine = rule_combine.rule_operation_combine(parameters)
                    result.append({n.name: parameter_combine})
                    break
        # for n in result:
        #     if isinstance(n, node.node):
        #         if n.interaction == criteria:
        #             parameters = []
        #             parameters.extend(n.headers)
        #             parameters.extend(n.body)
        #             parameter_combine = rule_combine.rule_operation_combine(parameters)
        #             result.append({n.name: parameter_combine})
    return results


# find_test_paths(csv_file_name)




