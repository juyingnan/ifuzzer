__author__ = 'bunny_gg'
import fuzzer
from utils import asserter
import sys
sys.path.append("..")

file_address='OpenStack_TestCases_v3/token_authenticate_post_1.py'
image_id = ""
http_address='http://openstackubuntu.chinacloudapp.cn:9292/v2/images/%s}/file' % image_id
runner = fuzzer.fuzzer(file_address, http_address, 'PUT', 1)
runner.headers["X-Auth-Token"]=""
runner.run(asserter.assert_equal, 401, "/v2/images/{image_id}/file ")

