import pytest

is_leap = [4, 40, 400, 800, 1992, 2996]
is_not_leap = [1, 100, 500, 1000, 1999, 3000]
is_valueerror = [0, -4, -100, -1996, -2000]
is_typeerror = ['-4', '4', '100', 'ins', '**', '中文']


# params传入需要的list
@pytest.fixture(params=is_leap)
def is_leap_y(request):
    return request.param


# params: an optional list of parameters which will cause multiple
# invocations of the fixture function and all of the tests using it.
# The current parameter is available in ``request.param``.
# params 参数，当前参数在'request.param'中可用。
# def get_direct_param_fixture_func(request):
#     return request.param

@pytest.fixture(params=is_typeerror)
def is_type_error(request):
    return request.param
