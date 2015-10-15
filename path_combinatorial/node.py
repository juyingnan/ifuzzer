__author__ = 'bunny_gg'

# separator between parameters
spt_between_parameters = "/"
# separator in parameter
spt_in_parameter = ":"

class node:
    def __init__(self, name, interaction, isStart=False, isEnd=False, comment="", toNodes="", headers="", body=""):
        self.name = name
        self.interaction = interaction
        self.isStart = isStart
        self.isEnd = isEnd
        self.comment = comment
        self.toNodes_str = toNodes
        self.headers_str = headers
        self.body_str = body
        self.toNodes = []
        self.headers = []
        self.body = []
        self.sub_paths = []
        self.get_Nodes()
        self.get_headers()
        self.get_body()
        self.get_sub_paths()

    def get_Nodes(self):
        for string in self.toNodes_str.split(spt_between_parameters):
            self.toNodes.append(string.split(spt_in_parameter)[0])

    def get_headers(self):
        if self.headers_str != None and len(self.headers_str)>2:
            header_strings = self.headers_str.split(spt_between_parameters)
            for header_string in header_strings:
                parameter_tmp = header_string.split(spt_in_parameter)
                self.headers.append(parameter(name=parameter_tmp[0], interaction=parameter_tmp[1]))

    def get_body(self):
        if self.body_str != None and len(self.body_str)>2:
            body_strings = self.body_str.split(spt_between_parameters)
            for body_string in body_strings:
                parameter_tmp = body_string.split(spt_in_parameter)
                self.body.append(parameter(name=parameter_tmp[0], interaction=parameter_tmp[1]))

    def get_sub_paths(self):
        if self.toNodes_str is not None and len(self.toNodes_str)>2:
            Node_Strings = self.toNodes_str.split(spt_between_parameters)
            for node_and_interaction in Node_Strings:
                node_tmp = node_and_interaction.split(spt_in_parameter)
                self.sub_paths.append(path(from_node=self.name, to_node=node_tmp[0], interaction=node_tmp[1]))

    def find_path(self, to_node_name):
        for sub_path in self.sub_paths:
            if sub_path.to_node == to_node_name:
                return sub_path
        return path(from_node=self.name, to_node=self.name, interaction="E", comment="self generated")

    def __str__(self):
        return str(self.name)


class parameter:
    def __init__(self, name="A", interaction="P", comment=""):
        self.name = name
        self.interaction = interaction
        self.comment = comment

    def __str__(self):
        return str(self.name)

class path:
    def __init__(self, from_node, to_node, interaction, comment=""):
        self.from_node = from_node
        self.to_node = to_node
        self.interaction = interaction
        self.comment = comment

    def __str__(self):
        # return str("->" + self.to_node.__str__())
        return str(self.from_node.__str__() + "->" + self.to_node.__str__())