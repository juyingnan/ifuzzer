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
# json_object = json.load(file('test.json'))
# print json_object
# fuzz_json_item(json_object, "password",[8,20,True,True,True,True])
# print json_object
# fuzz_json_item(json_object, "id",[8,8,True,True,True,True])
# print json_object
# shuffle_json_list(json_object, "user")
# print json_object