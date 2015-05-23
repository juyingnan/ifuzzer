__author__ = 'bunny_gg'
import itertools

critera = "U"

def input_check(input):
    if not isinstance(input, list):
        print "input error, not list"
        return False
    if len(input)<1:
        print "input error, list length less than 1."
        return False
    for item in input:
        if item.interaction == None:
            print "input error, no interaction"
            return  False
    return True

def rule_operation_combine(input):
    result = []
    if not input_check(input):
        return False
    if len(input) == 1:
        result.append(input)
    else:
        for i in range(2, len(input)+1, 1):
            for combine in list(itertools.combinations(input,i)):
                if operation(combine[0], combine[1:])==critera:
                    for r in result[::-1]:
                        if len(combine) > len(r):
                            result.remove(r)
                    result.append(combine)
    return result


def operation(input1, input2):
        if len(input2)>1:
            return compare(input1.interaction, operation(input2[0], input2[1:]))
        if len(input2)==1:
            return compare(input1.interaction, input2[0].interaction)

def compare(input1, input2):
    # matrix 1
    # matrix1 = [
    #     ["E", "E", "E", "E", "E", "E"],
    #     ["E", "X", "E", "E", "E", "E"],
    #     ["E", "E", "F", "E", "F", "F"],
    #     ["E", "E", "E", "P", "P", "P"],
    #     ["E", "E", "F", "P", "N", "U"],
    #     ["E", "E", "F", "P", "U", "U"]
    # ]

    # matrix 2
    matrix2 = [
        ["E", "E", "E", "E", "E", "E"],
        ["E", "X", "X", "X", "X", "X"],
        ["E", "X", "F", "F", "F", "F"],
        ["E", "X", "F", "U", "N", "U"],
        ["E", "X", "F", "N", "N", "N"],
        ["E", "X", "F", "U", "N", "U"]
    ]
    ta_list = ["E", "X", "F", "P", "N", "U"]
    i1 = ta_list.index(input1)
    i2 = ta_list.index(input2)
    return matrix2[i1][i2]