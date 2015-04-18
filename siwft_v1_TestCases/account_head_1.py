__author__ = 'bunny_gg'
import sys
sys.path.append("..")
import fuzzer
from utils import asserter

# make sure http_address is correct
http_address='http://openstack-bit.cloudapp.net:8080/v1/AUTH_8fccf2cb64da46499a68c0cccc364ccc'
runner = fuzzer.fuzzer(http_address, 'HEAD', 500)

# token will be fuzzed, so X-Auth-Token can be any
runner.headers["X-Auth-Token"]="ba6bbdc90e14446fae8636daa00807cc"
runner.headers_fuzz_params["X-Auth-Token"]=[0,64,True,True,True,True]

runner.run(asserter.assert_equal, 401, "/v1/{account}")