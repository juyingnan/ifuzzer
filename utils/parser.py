__author__ = 'bunny_gg'
import json
import randomer


def fuzz_json_item(json_item, key, params):
    if isinstance(json_item, dict):
        for item in json_item:
            if isinstance(json_item[item], dict):
                fuzz_json_item(json_item[item], key, params)
            else:
                if item == key:
                    json_item[item]=randomer.random_string(params[0],params[1],params[2],params[3],params[4],params[5])
    else:
        print("Error: input is not json object.")


def shuffle_json_list(json_item, key):
    if isinstance(json_item, dict):
        for item in json_item:
            if item == key and isinstance(json_item[item], dict):
                None
            if isinstance(json_item[item], dict):
                shuffle_json_list(json_item[item], key)
    else:
        print("Error: input is not json object.")


def json_file_load(file_address):
    return json.load(file(file_address))


def json_string_load(json_string):
    return json.loads(json_string)


def json_to_string(json_object):
    return json.dumps(json_object)


def get_file_content(file_address):
    file_object=open(file_address, mode='r', buffering=-1)
    return file_object.read()


ff = get_file_content("test.json")
print ff

# json_object = json.load(file('test.json'))
# print json_object
# json_string = json.dumps(json_object)
# print json_string

# fuzz_json_item(json_object, "password",[8,20,True,True,True,True])
# print json_object
# fuzz_json_item(json_object, "id",[8,8,True,True,True,True])
# print json_object
# shuffle_json_list(json_object, "user")
# print json_object

# body_json_string='''
# {
# "auth": {
# "identity": {
# "methods": [
# "password"
# ],
# "password": {
# "user": {
# "id": "2a91bed69b3f43ea8e88be313d519421",
# "password": "secrete"
# }
# }
# }
# }
# }
# '''
# json_object = json_string_load(body_json_string)
# print json_object
# json_string = json_to_string(json_object)
# print json_string