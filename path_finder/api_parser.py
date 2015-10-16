__author__ = 'bunny_gg'

import csv

import api



# separator between parameters
spt_between_parameters = "/"
# separator in parameter
spt_in_parameter = ":"


def csv_to_APIs(path, result=[]):
    reader = csv.DictReader(open(path))
    category_temp = ""
    # for Category, Name, Method, URI, Input, Response, Normal_response_code, Error_Response_code, and Description:
    for row in reader:
        if row["Category"] != "":
            category_temp = row["Category"]
        a = api.api(category=category_temp,
                    name=row["Name"],
                    method=row["Method"],
                    uri=row["URI"],
                    input=row["Input"],
                    response=row["Response"],
                    normal_response_code=row["Normal Response Code"],
                    error_response_code=row["Error Response Code"],
                    description=row["Description"])
        if a.name != "" and a.method != "" and a.uri != "":
            result.append(a)
    return result

# r = csv_to_APIs("sample.csv")
# for a in r:
#     print a
