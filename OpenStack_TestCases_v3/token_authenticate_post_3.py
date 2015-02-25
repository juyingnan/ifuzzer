__author__ = 'bunny_gg'
import fuzzer
from utils import asserter

file_address='test.json'
http_address='http://openstackubuntu.chinacloudapp.cn:5000/v3/auth/tokens'
runner = fuzzer.fuzzer(http_address, 'POST', 1)
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
"domain": {
"name": "example.com"
},
"name": "Joe",
"password": "secretsecret"
}
}
}
}
}
'''
runner.body_fuzz_params["password"]=[1,32,True,True,True,True]
runner.body_fuzz_params["name"]=[1,32,True,True,True,True]
runner.run(asserter.assert_equal, 401, "/v3/auth/tokens ")

