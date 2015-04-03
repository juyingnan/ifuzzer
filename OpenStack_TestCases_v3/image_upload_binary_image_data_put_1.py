__author__ = 'bunny_gg'
import sys
sys.path.append("..")
import fuzzer
from utils import asserter
from utils import randomer

file_address='../OpenStack_TestCases_v3/test.img'
randomer.generate_random_file(file_address, 0, 32)
# image_id = "e7db3b45-8db7-47ad-8109-3fb55c2c24f1"
# http_address='http://openstackubuntu.chinacloudapp.cn:9292/v2/images/%s/file' % image_id
http_address='http://openstackubuntu.chinacloudapp.cn:9292/v2/images/{id}/file'
runner = fuzzer.fuzzer(http_address, 'PUT', 1, file_address)
runner.url_fuzz_params["{id}"]=[1,32,True,True,True,True]
runner.url_fuzz_params["9292"]=[1,4,False,False,True,False]
runner.headers["X-Auth-Token"]="8c4d6c26887d4201b168ef12f0c18722"
runner.run_file(asserter.assert_equal, 401, "/v2/images/{image_id}/file ")

