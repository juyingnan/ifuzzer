from unittest import TestCase
import parser
__author__ = 'bunny_gg'


class TestJson_to_string(TestCase):
    def test_json_to_string(self):
        input = '''
{
"auth": {
"identity": {
"methods": [
"password"
],
"password": {
"user": {
"id": "2a91bed69b3f43ea8e88be313d519421",
"password": "secrete"
}
}
}
}
}
'''
        json = parser.json_string_load(input)
        output = parser.json_to_string(json)
        print output