__author__ = 'bunny_gg'
import sys
sys.path.append("..")
import fuzzer
from utils import asserter
from utils import randomer

file_address='../keystone_v3_cases/test.img'
# randomer.generate_random_file(file_address, 0, 655360)
image_id = "e7db3b45-8db7-47ad-8109-3fb55c2c24f2"
http_address='http://openstack-ace.cloudapp.net:9292/v2/images/%s/file' % image_id
# http_address='http://openstack-ace.cloudapp.net:9292/v2/images/{id}/file'
runner = fuzzer.fuzzer(http_address, 'PUT', 1, file_address)
# runner.url_fuzz_params["{id}"]=[1,32,True,True,True,True]
# runner.url_fuzz_params["9292"]=[1,4,False,False,True,False]
# print runner.get_token("28fb0982afab42a19e44f6d0a124c73d","secrete")
runner.headers["X-Auth-Token"]=runner.get_token("28fb0982afab42a19e44f6d0a124c73d","secrete")
runner.set_random_parameters(is_random=True, upper_limit=6550, lower_limit=0)
runner.run_file(asserter.assert_equal, 204, "/v2/images/{image_id}/file ")

