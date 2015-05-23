__author__ = 'bunny_gg'
import sys
sys.path.append("..")
import fuzzer
from utils import asserter

file_address='test.json'
http_address='http://openstack-ace.cloudapp.net:5000/v3/auth/tokens'
runner = fuzzer.fuzzer(http_address, 'POST', 5)
runner.headers["Content-Type"]="application/json"
runner.body_json_string='''
{
"auth": {
"identity": {
"methods": [
"password"
],
"password": {
"user": {
"id": "28fb0982afab42a19e44f6d0a124c73d",
"password": "secrete"
}
}
}
}
}
'''
runner.body_fuzz_params["password"]=[1,32,True,True,True,True]
runner.body_fuzz_params["id"]=[1,32,True,True,True,True]
for i in range(3):
    runner.run(asserter.assert_equal, 401, "/v3/auth/tokens ")

