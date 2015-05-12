__author__ = 'bunny_gg'
import parameter

# seperator between parameters
spt_between_parameters = "/"
# seperator in parameter
spt_in_parameter = "!"

class node:
    def __init__(self, name="A", interaction="P", isStart=False, isEnd=False, comment="", toNodes="", fromNodes="", headers="", body=""):
        self.name = name
        self.interaction = interaction
        self.isStart = isStart
        self.isEnd = isEnd
        self.comment = comment
        self.fromNodes_str = fromNodes
        self.toNodes_str = toNodes
        self.headers_str = headers
        self.body_str = body
        self.fromNodes = []
        self.toNodes = []
        self.headers = []
        self.body = []
        self.get_Nodes()
        self.get_headers()
        self.get_body()

    def get_Nodes(self):
        self.toNodes.extend(self.toNodes_str.split(spt_between_parameters))
        self.fromNodes.extend(self.fromNodes_str.split(spt_between_parameters))

    def get_headers(self):
        if self.headers_str != None and len(self.headers_str)>3:
            header_strings = self.headers_str.split(spt_between_parameters)
            for header_string in header_strings:
                parameter_tmp = header_string.split(spt_in_parameter)
                self.headers.append(parameter.parameter(name=parameter_tmp[0], interaction=parameter_tmp[1]))

    def get_body(self):
        if self.body_str != None and len(self.body_str)>3:
            body_strings = self.body_str.split(spt_between_parameters)
            for body_string in body_strings:
                parameter_tmp = body_string.split(spt_in_parameter)
                self.body.append(parameter.parameter(name=parameter_tmp[0], interaction=parameter_tmp[1]))

    def __str__(self):
        return str(self.name)