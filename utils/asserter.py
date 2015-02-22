__author__ = 'bunny_gg'


def assert_equal(expected_result, actual_result, message=""):
    if expected_result == actual_result:
        return True
    else:
        print message + "| assert_equal failed."
        return False


def assert_less(expected_result, actual_result, message=""):
    if actual_result < expected_result:
        return True
    else:
        print message + "| assert_less failed."
        return False


def assert_less_equal(expected_result, actual_result, message=""):
    if actual_result <= expected_result:
        return True
    else:
        print message + "| assert_less_equal failed."
        return False


def assert_great(expected_result, actual_result, message=""):
    if actual_result > expected_result:
        return True
    else:
        print message + "| assert_great failed."
        return False


def assert_great_equal(expected_result, actual_result, message=""):
    if actual_result >= expected_result:
        return True
    else:
        print message + "| assert_great_equal failed."
        return False


def assert_true(actual_result, message=""):
    if actual_result == True:
        return True
    else:
        print message + "| assert_true failed."
        return False


def assert_false(actual_result, message=""):
    if actual_result == False:
        return True
    else:
        print message + "| assert_false failed."
        return False


def fail():
    return False