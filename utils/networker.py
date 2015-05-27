__author__ = 'bunny_gg'
import sys
sys.path.append("..")
from pywebfuzz import utils


def send_request(url, method='GET', headers={}, body="", timeout=60):
    respond = utils.make_request(url, method=method, headers=headers, postdata=body, timeout=timeout)
    respond_dict = {}
    respond_dict["headers"]=respond[0]
    respond_dict["content"]=respond[1]
    respond_dict["code"]=respond[2]
    respond_dict["time"]=respond[3]
    return respond_dict


def send_file_request(url, file_address, method='PUT', headers={}, timeout=60):
    respond = utils.make_file_request(url, method=method, post_file_address=file_address, headers=headers, timeout=timeout)
    respond_dict = {}
    respond_dict["headers"]=respond[0]
    respond_dict["content"]=respond[1]
    respond_dict["code"]=respond[2]
    respond_dict["time"]=respond[3]
    return respond_dict