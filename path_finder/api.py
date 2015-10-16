__author__ = 'bunny_gg'

import api_io

# separator between parameters
spt_between_parameters = "/"
# separator in parameter
spt_in_parameter = "\n"


class api:
    def __init__(self, category, name, method, uri, input, response, normal_response_code, error_response_code,
                 description, component=""):
        self.category = category
        self.name = name
        self.method = method
        self.uri = uri
        self.input = self.get_apiIO_list(input, spt_in_parameter)
        self.response = self.get_apiIO_list(response, spt_in_parameter)
        self.normal_response_code = self.get_string_list(normal_response_code, spt_between_parameters)
        self.error_response_code = self.get_string_list(error_response_code, spt_between_parameters)
        self.description = description
        self.component = component
        self.isCompleted = self.content_check()

    def get_string_list(self, input_string, separator):
        return str(input_string).split(separator)

    def get_apiIO_list(self, input_string, separator):
        strList = str(input_string).split(separator)
        result = []
        for string in strList:
            a = api_io.apiIO(string=string)
        result.append(a)
        return result

    def content_check(self):
        result = True
        if not isinstance(self.category, str):
            # self.category = ""
            result = False
        if not isinstance(self.method, str):
            # self.method = ""
            result = False
        if not isinstance(self.uri, str):
            # self.uri = ""
            result = False
        if not isinstance(self.input, list):
            # self.input = []
            result = False
        if not isinstance(self.response, list):
            # self.response = []
            result = False
        if not isinstance(self.normal_response_code, list):
            # self.normal_response_code = []
            result = False
        if not isinstance(self.error_response_code, list):
            # self.error_response_code = []
            result = False
        if not isinstance(self.description, str):
            # self.description = ""
            result = False
        if not isinstance(self.component, str):
            # self.component = ""
            result = False
        return result

    def __str__(self):
        string = self.name
        string += "; "
        string += self.category
        string += "; "
        string += self.uri
        string += "; "
        string += self.method
        string += "; "
        string += self.description
        string += "; "
        string += "["
        for item in self.input:
            string += item.__str__()
            string += "/"
        string += "]; "
        string += "["
        for item in self.response:
            string += item.__str__()
            string += "/"
        string += "]; "
        string += "["
        for item in self.normal_response_code:
            string += item
            string += "/"
        string += "]; "
        string += "["
        for item in self.error_response_code:
            string += item
            string += "/"
        string += "]; "
        string += self.component
        string += "; "
        string += str(self.isCompleted)
        string += "."
        return string

    def __eq__(self, other):
        if not isinstance(other, api):
            return False
        if other.name == self.name and other.category == self.category:
            return True
        else:
            return False
