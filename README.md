# ifuzzer

## Introduction
ifuzzer is a fuzz-testing framework for REST APIs. It aims to simplify test case and process of fuzz-testing of REST APIs, like REST APIs in OpenStack. 

## Features
* Send REST request
* Assertion: expected result & actual result
* Different HTTP methods
* Fuzz Testing count
```
...
http_address='http://openstackubuntu.chinacloudapp.cn:5000/v3/auth/tokens'
runner = fuzzer.fuzzer(http_address, 'POST', 5)
...
runner.run(asserter.assert_equal, 401, "/v3/auth/tokens ")
```
* All data fuzz generation (randomly)
* http url fuzzing
```
...
http_address='http://openstackubuntu.chinacloudapp.cn:9292/v2/images/{id}/file'
runner.url_fuzz_params["{id}"]=[1,32,True,True,True,True]
runner.url_fuzz_params["9292"]=[1,4,False,False,True,False]
...
```
* http request header and body fuzzing
```
...
runner.header_fuzz_params["Content-Type"]=[1,32,True,True,True,True]
runner.body_fuzz_params["password"]=[1,32,True,True,True,True]
runner.body_fuzz_params["id"]=[1,32,True,True,True,True]
...
```
* Logging
* File generation, like image file
```
...
file_address='../OpenStack_TestCases_v3/test.img'
randomer.generate_random_file(file_address, 0, 65536)
...
```

## Test Case
* OPTIONAL: import sys for other path quote
```
import sys
sys.path.append("..")
...
```
* MUST: import fuzzer, asserter
* OPTIONAL: randomer
```
import fuzzer
from utils import asserter
from utils import randomer
...
```
* MUST: http_address (tested API)
* MUST: runner defination
  * parameter 1: http_address
  * parameter 2: http method
  * parameter 3: fuzzing count
```
...
http_address='http://openstackubuntu.chinacloudapp.cn:5000/v3/auth/tokens'
runner = fuzzer.fuzzer(http_address, 'POST', 5)
...
```
* MUST: template file address or body_json_string defination
```
...
file_address='test.json'
...
```
or
```
...
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
...
```
* OPTIONAL: fuzzing url
* OPTIONAL: fuzzing header
* OPTIONAL: fuzzing body
```
...
runner.url_fuzz_params["{id}"]=[1,32,True,True,True,True]
runner.header_fuzz_params["Content-Type"]=[1,32,True,True,True,True]
runner.body_fuzz_params["password"]=[1,32,True,True,True,True]
...
```
* MUST: runner.run (including asserter defination, expected result and OPTIONAL message)
```
...
runner.run(asserter.assert_equal, 401, "/v3/auth/tokens ")
...
```
* OPTIONAL: File transfer
  * OPTIONAL: file generation
  ```
  ...
  file_address='../OpenStack_TestCases_v3/test.img'
  randomer.generate_random_file(file_address, 0, 65536)
  ...
  ```
  * MUST: runner.run_file (including asserter defination, expected result and OPTIONAL message)
  * MUST: runner defination needs contain file_address
  ```
  ...
  runner = fuzzer.fuzzer(http_address, 'PUT', 1, file_address)
  ...
  runner.run_file(asserter.assert_equal, 401, "/v2/images/{image_id}/file ")
  ...
  ```
# TODO
* test case parameter (for temp test)
* bug fixes
