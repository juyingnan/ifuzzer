__author__ = 'bunny_gg'
import itertools

critera = "P"


def input_check(input):
    if not isinstance(input, list):
        print "input error, not list"
        return False
    if len(input)<2:
        print "input error, list length less than 2."
        return False
    for item in input:
        if item.interaction == None:
            print "input error, no interaction"
            return  False
    return True


def rule_operation_path(input):
    result = []
    if not input_check(input):
        return False
    for item in input:
        if operation(input[0], input[1:])==critera:
            return input
        else:
            return None


def operation(input1, input2):
        if len(input2)>1:
            return compare(input1.interaction, operation(input2[0], input2[1:]))
        if len(input2)==1:
            return compare(input1.interaction, input2[0].interaction)

def compare(input1, input2):

    matrix1 = [
        ["E", "E", "E", "E", "E", "E"],
        ["E", "X", "E", "E", "E", "E"],
        ["E", "E", "F", "E", "F", "F"],
        ["E", "E", "E", "P", "P", "P"],
        ["E", "E", "F", "P", "N", "U"],
        ["E", "E", "F", "P", "U", "U"]
    ]
    ta_list = ["E", "X", "F", "P", "N", "U"]
    i1 = ta_list.index(input1)
    i2 = ta_list.index(input2)
    return matrix1[i1][i2]