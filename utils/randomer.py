__author__ = 'bunny_gg'
import random
import string


def random_string(min_length=0, max_length=32, have_upper=True, have_lower=True, have_digit=True, have_other=True):
    length = random.randint(min_length, max_length)
    string_pool = ''
    if have_upper:
        string_pool += string.ascii_uppercase
    if have_lower:
        string_pool += string.ascii_lowercase
    if have_digit:
        string_pool += string.digits
    if have_other:
        string_pool += string.printable + string.punctuation
    return ''.join(random.SystemRandom().choice(string_pool) for _ in range(length))


def random_shuffle(shuffle_list):
    random.shuffle(shuffle_list)

