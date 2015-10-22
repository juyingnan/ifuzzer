__author__ = 'bunny_gg'

import path_node
import api
import api_io
import api_parser
import random


def build_tree(csv_list, init_info_string_list, max_level, max_children, default_api=None, isRandom=False):
    # find all APIs
    api_list = []
    for csv_file in csv_list:
        api_list.extend(api_parser.csv_to_APIs(csv_file))

    # convert info string to api_io
    info_list = []
    for string in init_info_string_list:
        new_api_io = api_io.apiIO(string=string)
        info_list.append(new_api_io)

    # step 0, create a root node = Authenticate
    root = path_node.TreeNode(default_api, None, None, info_list)
    new_level_list = [root]
    level = 1

    # find all available paths
    while new_level_list.__len__() > 0 and level <= max_level:
        leaf_list = new_level_list
        new_level_list = []
        level += 1
        for node in leaf_list:
            for api in (api_list if isRandom == False else random.sample(api_list, len(api_list))):
                if len(node.child) < max_children:
                    # if api is not in upper node
                    isInUpperNode = is_api_in_upper_node(node, api)
                    # if info includes all api's input
                    isIncludeAllInput = is_include_all_input(node, api)
                    if isInUpperNode == False and isIncludeAllInput == True:
                        new_info = []
                        new_info.extend(node.info)
                        new_info.extend(api.response)
                        new_child = path_node.TreeNode(api, node, children=None, info=new_info, is_leaf=False,
                                                       level=level)
                        node.add_child(new_child)
                        new_level_list.append(new_child)
            if node.child.__len__() == 0:
                node.isLeaf = True
    # output
    return root


def is_api_in_upper_node(node, api):
    upperNode = node
    while upperNode is not None:
        if upperNode.api == api:
            return True
        upperNode = upperNode.parent
    return False


def is_include_all_input(node, api):
    includeCount = 0
    for input in api.non_optional_input:
        for info in node.info:
            if input == info:
                includeCount += 1
                break
    if includeCount == len(api.non_optional_input):
        return True
    return False


def get_all_paths(root, result=[], stack=[]):
    if root is None:
        return result
    stack.append(root)
    if len(root.child) == 0:
        # print stack
        print_tree_stack(stack)
        result.append(stack)
        stack.pop()
        return result
    for child in root.child:
        get_all_paths(child, result, stack)
    stack.pop()
    return result


def print_tree_stack(stack):
    string = ""
    separator = " -> "
    for node in stack:
        string += str(node) + separator
    print (string[:len(separator)*-1] if len(string) > len(separator) else string)

authenticate_api = api.api(category="Token", name="Authenticate", method="POST",
                               uri="/v3/auth/tokens", input="user_id\npassword", response="X-Auth-Token",
                               normal_response_code="201", error_response_code="400/401/403/405/413/503/404",
                               description="Authenticates and generates a token.", component="Keystone")
max_level = 6
max_child = 3
isRandom = True
tree = build_tree(["keystone.csv", "glance.csv", "nova.csv"],
                  ["tenant_id"],
                  max_level, max_child, authenticate_api,
                  isRandom)
result = get_all_paths(tree, [], [])
print result
