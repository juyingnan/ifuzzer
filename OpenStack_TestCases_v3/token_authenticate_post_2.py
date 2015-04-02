__author__ = 'bunny_gg'
import sys
sys.path.append("..")
import fuzzer
from utils import asserter

file_address = 'test.json'
http_address = 'http://openstackubuntu.chinacloudapp.cn:5000/v3/auth/tokens'
runner = fuzzer.fuzzer(http_address, 'POST', 5, file_address)
runner.headers["Content-Type"]="application/json"
runner.body_fuzz_params["password"]=[1,32,True,True,True,True]
runner.body_fuzz_params["id"]=[1,32,True,True,True,True]
runner.run(asserter.assert_equal, 401, "/v3/auth/tokens ")

