__author__ = 'bunny_gg'
import fuzzer
from utils import asserter

file_address='test.json'
http_address='http://openstackubuntu.chinacloudapp.cn:5000/v3/services'
runner = fuzzer.fuzzer(file_address, http_address, 'GET', 3)
runner.headers["X-Auth-Token"]=""
runner.headers_fuzz_params["X-Auth-Token"]=[32,32,True,True,True,True]
runner.body_fuzz_params["password"]=[1,32,True,True,True,True]
runner.body_fuzz_params["id"]=[1,32,True,True,True,True]
runner.run(asserter.assert_great_equal)

