__author__ = 'bunny_gg'
import sys
sys.path.append("..")
import fuzzer
from utils import asserter

# {account} in uri will be fuzzed, so {account} can be any
http_address='http://openstack-bit.cloudapp.net:8080/v1/{account}'
runner = fuzzer.fuzzer(http_address, 'GET', 5)
runner.url_fuzz_params["{account}"]=[1,64,True,True,True,False]
# make sure token is correct
runner.headers["X-Auth-Token"]="3a917a00c425494981f7059fe9ab9989"

runner.run(asserter.assert_equal, 403, "/v1/{account}")