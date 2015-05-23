__author__ = 'bunny_gg'
import logging
import time

from utils import parser
from utils import networker
from utils import logger
from utils import randomer

class fuzzer:
    def __init__(self, http_address, method="GET", count=1000, template_file_address=""):
        self.template_file_address = template_file_address
        self.http_address = http_address
        self.original_http_address = http_address
        self.count = count
        self.current_count = 0
        self.method = method.upper()
        self.headers = {}
        self.body = {}
        self.body_json_string = ""
        self.headers_fuzz_params = {}
        self.body_fuzz_params = {}
        self.url_fuzz_params = {}
        self.headers_shuffle_params = False
        self.body_shuffle_params = []
        self.respond = {}
        self.random_file_params = [0,0]
        self.isRandomFile = False
        self.logging_setting()
        self.result_setting()


    def url_params_check(self):
        for item in self.url_fuzz_params:
            if not item in self.http_address:
                print "url_params_key error"
                return False
            if not isinstance(self.url_fuzz_params[item], list):
                print "url_params_format_value error"
                return False
            if not isinstance(self.url_fuzz_params[item][0], int):
                print "url_params_format_min error"
                return False
            if not isinstance(self.url_fuzz_params[item][1], int):
                print "url_params_format_max error"
                return False
            if not isinstance(self.url_fuzz_params[item][2], bool):
                print "url_params_format_upper error"
                return False
            if not isinstance(self.url_fuzz_params[item][3], bool):
                print "url_params_format_lower error"
                return False
            if not isinstance(self.url_fuzz_params[item][4], bool):
                print "url_params_format_digit error"
                return False
            if not isinstance(self.url_fuzz_params[item][5], bool):
                print "url_params_format_other error"
                return False
            if self.url_fuzz_params[item][0] > self.url_fuzz_params[item][1]:
                print "url_params_format min>max error"
                return False
        return True


    def headers_params_check(self):
        for item in self.headers_fuzz_params:
            if not self.headers.has_key(item):
                print "headers_params_key error"
                return False
            if not isinstance(self.headers_fuzz_params[item], list):
                print "headers_params_format_value error"
                return False
            if not isinstance(self.headers_fuzz_params[item][0], int):
                print "headers_params_format_min error"
                return False
            if not isinstance(self.headers_fuzz_params[item][1], int):
                print "headers_params_format_max error"
                return False
            if not isinstance(self.headers_fuzz_params[item][2], bool):
                print "headers_params_format_upper error"
                return False
            if not isinstance(self.headers_fuzz_params[item][3], bool):
                print "headers_params_format_lower error"
                return False
            if not isinstance(self.headers_fuzz_params[item][4], bool):
                print "headers_params_format_digit error"
                return False
            if not isinstance(self.headers_fuzz_params[item][5], bool):
                print "headers_params_format_other error"
                return False
            # if isinstance(item.value[6], int):
            # print "headers_params_format_posit error"
            #     return False
            if self.headers_fuzz_params[item][0] > self.headers_fuzz_params[item][1]:
                print "headers_params_format min>max error"
                return False
        return True

    def body_params_check(self):
        for item in self.body_fuzz_params:
            # if not self.body.has_key(item.key):
            #    print "body_params_key error"
            #    return False

            if not isinstance(self.body_fuzz_params[item], list):
                print "body_params_format_value error"
                return False
            if not isinstance(self.body_fuzz_params[item][0], int):
                print "body_params_format_min error"
                return False
            if not isinstance(self.body_fuzz_params[item][1], int):
                print "body_params_format_max error"
                return False
            if not isinstance(self.body_fuzz_params[item][2], bool):
                print "body_params_format_upper error"
                return False
            if not isinstance(self.body_fuzz_params[item][3], bool):
                print "body_params_format_lower error"
                return False
            if not isinstance(self.body_fuzz_params[item][4], bool):
                print "body_params_format_digit error"
                return False
            if not isinstance(self.body_fuzz_params[item][5], bool):
                print "body_params_format_other error"
                return False
            # if isinstance(item.value[6], int):
            #     print "body_params_format_posit error"
            #     return False
            if self.body_fuzz_params[item][0] > self.body_fuzz_params[item][1]:
                print "body_params_format min>max error"
                return False
        for item in self.body_shuffle_params:
            if not isinstance(self.body_shuffle_params[item], int):
                print "body_params_format_shuffle_posit error"
                return False
        return True

    def random_params_check(self):
        if self.isRandomFile:
            if self.random_file_params.__len__() < 2:
                print "random parameters less than 2"
                return False
            if not isinstance(self.random_file_params[0], int):
                print "random parameters lower limit wrong format"
                return False
            if not isinstance(self.random_file_params[1], int):
                print "random parameters upper limit wrong format"
                return False
            if self.random_file_params[1] < self.random_file_params[0]:
                print "random parameters upper limit < lower limit"
                return False
            return True
        return True

    def check(self):
        if self.count == 0:
            print "0 count error"
            return False
        if self.method != "GET" and self.method != "POST" and self.method != "DELETE" and self.method != "PUT" and self.method != "HEAD" and self.method != "DELETE":
            print "method error"
            return False
        if not self.url_params_check():
            return False
        if not self.headers_params_check():
            return False
        if not self.body_params_check():
            return False
        if not self.random_params_check():
            return False
        print "Checks OK"
        return True

    def logging_setting(self):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename="Log__" + time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime(time.time())) + ".log",
                            filemode='w')

    def result_setting(self):
        self.result = logger.file_write(
            "Result__" + time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime(time.time())) + ".log")

    def result_init(self):
        time_start = time.asctime(time.localtime(time.time()))
        self.result.write("TEST: %s;\n" % (self.http_address))
        self.result.write("HEAD: %s;\n" % (self.headers))
        self.result.write("BODY: %s;\n" % (self.body))
        self.result.write("START TIME: %s;\n" % (time_start))

    def result_finish(self, count_error, count_pass):
        time_end = time.asctime(time.localtime(time.time()))
        self.result.write("END TIME: %s;\n" % (time_end))
        # self.result.write("DURING: %s;\n" %(time_end - time_start))
        self.result.write("PASS: %d;\n" % (count_pass))
        self.result.write("ERROR: %d;\n" % (count_error))
        self.result.write("TOTAL: %d;\n" % (self.count))

    def http_request_fuzz(self):
        self.http_address = self.original_http_address
        for param in self.url_fuzz_params:
            self.http_address = parser.fuzz_url_item(self.http_address, param, self.url_fuzz_params[param])
        for param in self.headers_fuzz_params:
            parser.fuzz_json_item(self.headers, param, self.headers_fuzz_params[param])
        for param in self.body_fuzz_params:
            parser.fuzz_json_item(self.body, param, self.body_fuzz_params[param])

    def run(self, assertion, expected_result=400, message=""):
        if not self.check():
            return False
        else:
            if self.template_file_address == "":
                if self.body_json_string != "":
                    self.body = parser.json_string_load(self.body_json_string)
            else:
                self.body = parser.json_file_load(self.template_file_address)
            count_pass = 0
            count_error = 0
            self.result_init()
            for i in range(self.count):
                self.http_request_fuzz()
                self.body_json_string = parser.json_to_string(self.body)
                # print self.body_json_string
                logging.debug(self.http_address + " | " + self.headers.__str__() + " | " + self.body_json_string)
                self.respond = networker.send_request(self.http_address, self.method, self.headers, self.body_json_string)
                self.current_count += 1
                logging.info(self.current_count.__str__() + ":" + self.respond.__str__())
                if assertion(expected_result, self.respond["code"], message):
                    count_pass += 1
                else:
                    count_error += 1
                    logging.warning(
                        self.current_count.__str__() + ":" + self.http_address + " | " + self.headers.__str__() + "|" + self.body_json_string + "|" + self.respond.__str__())
                    self.result.write(
                        self.current_count.__str__() + ":" + self.http_address + " | " + self.headers.__str__() + "|" + self.body_json_string + "|" + self.respond.__str__() + "\n")
            self.result_finish(count_error, count_pass)

    def set_random_parameters(self, is_random, upper_limit, lower_limit):
        self.isRandomFile = is_random
        self.random_file_params[0] = lower_limit
        self.random_file_params[1] = upper_limit

    def get_random_file(self):
        if self.isRandomFile:
            randomer.generate_random_file(self.template_file_address, self.random_file_params[0], self.random_file_params[1])

    def run_file(self, assertion, expected_result=400, message=""):
        if not self.check():
            return False
        else:
            self.get_random_file()
            self.body = parser.get_file_content(self.template_file_address)
            count_pass = 0
            count_error = 0
            self.result_init()
            for i in range(self.count):
                self.http_request_fuzz()  # print self.headers
                # print self.body
                logging.debug(self.headers.__str__() + "|" + self.body.__str__())
                self.respond = networker.send_file_request(self.http_address, self.template_file_address, self.method, self.headers)
                self.current_count += 1
                logging.info(self.current_count.__str__() + ":" + self.respond.__str__())
                if assertion(expected_result, self.respond["code"], message):
                    count_pass += 1
                else:
                    count_error += 1
                    logging.warning(
                        self.current_count.__str__() + ":" + self.headers.__str__() + "|" + self.body_json_string + "|" + self.respond.__str__())
                    self.result.write(
                        self.current_count.__str__() + ":" + self.headers.__str__() + "|" + self.body_json_string + "|" + self.respond.__str__() + "\n")
            self.result_finish(count_error, count_pass)

    def get_token(self, user_id, password, http_address=""):
        if http_address == "":
            token_http_address = self.http_address.split(":")[0] + ":" +self.http_address.split(":")[1]
        else:
            token_http_address=http_address
        token_http_address += ":5000/v3/auth/tokens"
        token_method = "POST"
        token_headers = {}
        token_headers["Content-Type"]="application/json"
        token_body_json_string='''
        {
        "auth": {
        "identity": {
        "methods": [
        "password"
        ],
        "password": {
        "user": {
        "id": "%s",
        "password": "%s"
        }
        }
        }
        }
        }
        ''' % (user_id, password)
        token_respond = networker.send_request(token_http_address, token_method, token_headers, token_body_json_string)
        if token_respond["code"] == 201:
            return token_respond["headers"]["X-Subject-Token"]
        else:
            return ""
