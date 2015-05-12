__author__ = 'bunny_gg'
import itertools

critera = "U"

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

def rule_operation_combine(input):
    result = []
    if not input_check(input):
        return False
    for i in range(2, len(input)+1, 1):
        for combine in list(itertools.combinations(input,i)):
            if operation(combine[0], combine[1:])==critera:
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


class parameter:
    def __init__(self, name, interaction="P",):
        self.name = name
        self.interaction = interaction
    def __str__(self):
        return self.name

# p1 = parameter("P1","X")
# p2 = parameter("P2","E")
# p3 = parameter("P3","P")
# p4 = parameter("P4","P")
# p5 = parameter("P5","N")
# p6 = parameter("P6","U")
# p7 = parameter("P7","E")
# p8 = parameter("P8","P")
# ipt = [p1, p2, p3, p4, p5, p6, p7, p8]
# rst = rule_operation(ipt)
# for r in rst:
#     for t in r:
#         print t
#     print "-----"
