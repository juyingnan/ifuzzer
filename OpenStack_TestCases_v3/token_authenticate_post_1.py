__author__ = 'bunny_gg'
import fuzzer
from utils import asserter

file_address='test.json'
http_address='http://openstackubuntu.chinacloudapp.cn:5000/v3/auth/tokens'
runner = fuzzer.fuzzer(http_address, 'POST', 1000)
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
"id": "2a91bed69b3f43ea8e88be313d519428",
"password": "secrete"
}
}
}
}
}
'''
#runner.body_fuzz_params["password"]=[1,32,True,True,True,True]
#runner.body_fuzz_params["id"]=[1,32,True,True,True,True]
runner.run(asserter.assert_equal, 201, "/v3/auth/tokens ")

