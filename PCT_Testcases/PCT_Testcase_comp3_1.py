__author__ = 'bunny_gg'
# This PCT test case is for connection between 3 components in OpenStack: Glance, Nova and Keystone.

import sys
sys.path.append("..")
import fuzzer
from utils import asserter

server_address = "http://openstack-ace.cloudapp.net"
count = 10000
if sys.argv.__len__() > 0:
    if isinstance(sys.argv[0], int):
        count = sys.argv[0]

# Step 0: Keystone generating token
# Step 1: Glance - Create Image
http_address_glance_create_image = server_address + ":9292/v2/images"
runner_1 = fuzzer.fuzzer(http_address_glance_create_image, 'POST', 1)
# Token
user_id = "28fb0982afab42a19e44f6d0a124c73d"
password = "secrete"
token = runner_1.get_token(user_id, password)
# Create Image
runner_1.headers["Content-Type"]= "application/json"
runner_1.headers["X-Auth-Token"]= token
runner_1.body_json_string='''
{
"name": "Ubuntu 12.10",
"container_format": "ami",
"disk_format": "ami",
"visibility": "public"
}
'''
#runner_1.body_fuzz_params["id"]=[32,32,False,False,True,False]
runner_1.body_fuzz_params["name"]=[1,128,True,True,True,False]

# Step 2: Glance - Upload binary image data
http_address_glance_upload_image = server_address + ":9292/v2/images/{image_id}/file"
# image_file_address = '../PCT_TestCases/test.img'
image_file_address = 'test.img'
runner_2 = fuzzer.fuzzer(http_address_glance_upload_image, "PUT", 1, image_file_address)
runner_2.headers["X-Auth-Token"]= token
runner_2.set_random_parameters(is_random=True, upper_limit=6550, lower_limit=0)

# Step 3: Nova - Get Image Detail
http_address_nove_get_image_detail = server_address + ":8774/v2.1/{tenant_id}/images/{image_id}"
tenant_id = "fca219c75755494380f9b12aa8f72b8d"
runner_3 = fuzzer.fuzzer(http_address_nove_get_image_detail, "GET", 1)
runner_3.headers["X-Auth-Token"]= token

# Step 4: Nova - Create Server
http_address_nova_create_server = server_address + ":8774/v2.1/{tenant_id}/servers"
runner_4 = fuzzer.fuzzer(http_address_nova_create_server, "POST", 1)
runner_4.headers["X-Auth-Token"]= token
runner_4.headers["Content-Type"]= "application/json"
body_string_create_server = '''
{
"server": {
"name": "server-test-1",
"imageRef": "{image_id}",
"flavorRef": "1",
"max_count": 1,
"min_count": 1
}
}
'''
runner_4.body_json_string=body_string_create_server
runner_4.body_fuzz_params["name"]=[1,128,True,True,True,False]

# Step 5: Nova - Delete Server
http_address_nova_delete_server = server_address + ":8774/v2.1/{tenant_id}/servers/{server_id}"
runner_5 = fuzzer.fuzzer(http_address_nova_delete_server, "DELETE", 1)
runner_5.headers["X-Auth-Token"]= token

# Step 6: Nova - Delete Image
http_address_nova_delete_image = server_address + ":8774/v2.1/{tenant_id}/images/{image_id}"
runner_6 = fuzzer.fuzzer(http_address_nova_delete_image, "DELETE", 1)
runner_6.headers["X-Auth-Token"]= token

# run fuzzers
for i in range(0, count, 1):
    try:
        # step 1:create image
        runner_1.run(asserter.assert_equal, 201, i.__str__() + ": Step 1: Create Image")
        if runner_1.respond != "Error" and runner_1.respond["code"] == 201:
            # step 2: upload binary image data
            image_location = runner_1.respond["headers"]["location"]
            image_id = image_location.split("/")[-1]
            runner_2.original_http_address = http_address_glance_upload_image.replace("{image_id}", image_id)
            runner_2.run_file(asserter.assert_equal, 204, i.__str__() + ": Step 2 Upload binary image data")
            # step 3
            runner_3.original_http_address = http_address_nove_get_image_detail.replace("{tenant_id}", tenant_id).replace("{image_id}", image_id)
            runner_3.run(asserter.assert_less_equal, 205, i.__str__() + ": Step 3: View Image Detail")
            # step 4
            runner_4.original_http_address = http_address_nova_create_server.replace("{tenant_id}", tenant_id)
            runner_4.body_json_string = body_string_create_server.replace("{image_id}", image_id)
            runner_4.run(asserter.assert_equal, 202, i.__str__() + ": Step 4: Create Server")
            if runner_4.respond != "Error" and runner_4.respond["code"] == 202:
                # step 5
                server_location = runner_4.respond["headers"]["location"]
                server_id = server_location.split("/")[-1]
                runner_5.original_http_address = http_address_nova_delete_server.replace("{tenant_id}", tenant_id).replace("{server_id}", server_id)
                runner_5.run(asserter.assert_equal, 204, i.__str__() + ": Step 5: Delete Server")
        else:
            print runner_1.respond
    finally:
        # step 6: delete image
        runner_6.original_http_address = http_address_nove_get_image_detail.replace("{tenant_id}", tenant_id).replace("{image_id}", image_id)
        runner_6.run(asserter.assert_equal, 204, i.__str__() + ": Step 6: Delete Image")




