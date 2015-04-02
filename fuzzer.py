__author__ = 'bunny_gg'
import logging
import time

from utils import parser
from utils import networker
from utils import logger


class fuzzer:
    def __init__(self, http_address, method="GET", count=1000, template_file_address=""):
        self.template_file_address = template_file_address
        self.http_address = http_address
        self.count = count
        self.method = method.upper()
        self.headers = {}
        self.body = {}
        self.body_json_string = ""
        self.headers_fuzz_params = {}
        self.body_fuzz_params = {}
        self.headers_shuffle_params = False
        self.body_shuffle_params = []
        self.respond = {}
        self.logging_setting()
        self.result_setting()

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

    def check(self):
        if self.count == 0:
            print "0 count error"
            return False
        if self.method != "GET" and self.method != "POST" and self.method != "DELETE" and self.method != "PUT" and self.method != "HEAD" and self.method != "DELETE":
            print "method error"
            return False
        if not self.headers_params_check():
            return False
        if not self.body_params_check():
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
        for param in self.headers_fuzz_params:
            parser.fuzz_json_item(self.headers, param, self.headers_fuzz_params[param])
        for param in self.body_fuzz_params:
            parser.fuzz_json_item(self.body, param, self.body_fuzz_params[param])

    def run(self, assertion, expected_result=400, message=""):
        if not self.check():
            return False
        else:
            if self.template_file_address == "":
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
                logging.debug(self.headers.__str__() + " | " + self.body_json_string)
                self.respond = networker.send_request(self.http_address, self.method, self.headers, self.body_json_string)
                logging.info(i.__str__() + ":" + self.respond.__str__())
                if assertion(expected_result, self.respond["code"], message):
                    count_pass += 1
                else:
                    count_error += 1
                    logging.warning(
                        i.__str__() + ":" + self.headers.__str__() + "|" + self.body_json_string + "|" + self.respond.__str__())
                    self.result.write(
                        i.__str__() + ":" + self.headers.__str__() + "|" + self.body_json_string + "|" + self.respond.__str__() + "\n")
            self.result_finish(count_error, count_pass)

    def run_file(self, assertion, expected_result=400, message=""):
        if not self.check():
            return False
        else:
            self.body = parser.get_file_content(self.template_file_address)
            count_pass = 0
            count_error = 0
            self.result_init()
            for i in range(self.count):
                self.http_request_fuzz()  # print self.headers
                # print self.body
                logging.debug(self.headers.__str__() + "|" + self.body.__str__())
                self.respond = networker.send_file_request(self.http_address, self.template_file_address, self.method, self.headers)
                logging.info(i.__str__() + ":" + self.respond.__str__())
                if assertion(expected_result, self.respond["code"], message):
                    count_pass += 1
                else:
                    count_error += 1
                    logging.warning(
                        i.__str__() + ":" + self.headers.__str__() + "|" + self.body_json_string + "|" + self.respond.__str__())
                    self.result.write(
                        i.__str__() + ":" + self.headers.__str__() + "|" + self.body_json_string + "|" + self.respond.__str__() + "\n")
            self.result_finish(count_error, count_pass)