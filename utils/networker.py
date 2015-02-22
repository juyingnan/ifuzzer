__author__ = 'bunny_gg'
from pywebfuzz import utils


def send_request(url, method='GET', headers={}, body={}):
    respond = utils.make_request(url, method="GET", headers=headers)
    respond_dict = {}
    respond_dict["headers"]=respond[0]
    respond_dict["content"]=respond[1]
    respond_dict["code"]=respond[2]
    respond_dict["time"]=respond[3]
    return respond_dict