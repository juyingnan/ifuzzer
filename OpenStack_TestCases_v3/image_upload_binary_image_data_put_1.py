__author__ = 'bunny_gg'
import sys
sys.path.append("..")
import fuzzer
from utils import asserter

file_address='../OpenStack_TestCases_v3/token_authenticate_post_1.py'
image_id = "e7db3b45-8db7-47ad-8109-3fb55c2c24f1"
http_address='http://openstackubuntu.chinacloudapp.cn:9292/v2/images/%s/file' % image_id
print http_address
runner = fuzzer.fuzzer(http_address, 'PUT', 1, file_address)
runner.headers["X-Auth-Token"]="8c4d6c26887d4201b168ef12f0c18722"
runner.run_file(asserter.assert_equal, 401, "/v2/images/{image_id}/file ")

