__author__ = 'bunny_gg'
import sys
sys.path.append("..")
import fuzzer
from utils import asserter

# make sure http_address is correct
http_address='http://openstack-bit.cloudapp.net:8080/v1/AUTH_8fccf2cb64da46499a68c0cccc364ccc'
runner = fuzzer.fuzzer(http_address, 'POST', 9)

# make sure token is correct
runner.headers["X-Auth-Token"]="ba6bbdc90e14446fae8636daa00807cc"
# "X-Account-Meta-Book" & "X-Account-Meta-Subject" will be fuzzed, can be any
runner.headers["X-Account-Meta-Book"]="test"
runner.headers["X-Account-Meta-Subject"]="test"

runner.headers_fuzz_params["X-Account-Meta-Book"]=[0,64,True,True,True,False]
runner.headers_fuzz_params["X-Account-Meta-Subject"]=[0,64,True,True,True,False]

runner.run(asserter.assert_equal, 204, "/v1/{account}")