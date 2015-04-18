__author__ = 'bunny_gg'


def assert_equal(expected_result, actual_result, message=""):
    if expected_result == actual_result:
        return True
    else:
        print message + "| assert_equal failed."
        return False


def assert_not_equal(expected_result, actual_result, message=""):
    if expected_result != actual_result:
        return True
    else:
        print message + "| assert_not_equal failed."
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

def succeed():
    return True


def assert_range(expect_result_min, expect_result_max, actual_result, message="", min_equal=True, max_equal=True):
    if min_equal == True:
        if actual_result < expect_result_min:
            print message + "| assert_range failed."
            return False
    else:
        if actual_result <= expect_result_min:
            print message + "| assert_range failed."
            return False
    if max_equal == True:
        if actual_result > expect_result_max:
            print message + "| assert_range failed."
            return False
    else:
        if actual_result >= expect_result_max:
            print message + "| assert_range failed."
            return False
    return True


def assert_not_range(expect_result_min, expect_result_max, actual_result, message="", min_equal=True, max_equal=True):
    if min_equal == True:
        if actual_result < expect_result_min:
            return True
    else:
        if actual_result <= expect_result_min:
            return True
    if max_equal == True:
        if actual_result > expect_result_max:
            return True
    else:
        if actual_result >= expect_result_max:
            return True
    print False