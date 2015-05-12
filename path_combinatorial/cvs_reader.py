__author__ = 'bunny_gg'

import csv
import node
import parameter

# seperator between parameters
spt_between_parameters = "/"
# seperator in parameter
spt_in_parameter = "!"

def csv_to_nodes(path, result=[]):
    reader = csv.DictReader(open(path))
    # for name, interaction, isStart, isEnd, comment, fromNodes, toNodes, headers, body in reader:
    for row in reader:
        n = node.node(name=row["name"],
                      interaction=row["interaction"],
                      isStart=row["isStart"] == str(True),
                      isEnd=row["isEnd"]== str(True),
                      comment=row["comment"],
                      toNodes=row["toNodes"],
                      fromNodes=row["fromNodes"],
                      headers=row["headers"],
                      body=row["body"])
        result.append(n)
    return result

def nodes_to_graph(nodes, graph={}):
    for node in nodes:
        toNodes_list = []
        for toNode in node.toNodes:
            for n in nodes:
                if toNode == n.name:
                    toNodes_list.append(n)
        graph[node] = toNodes_list
    return graph


# r = csv_to_node("sample.csv")
# g = nodes_to_graph(r)
# print r
# print g
