import pytest
import is_leap_year
is_leap = [4, 40, 400, 800, 1992, 2996]
is_not_leap = [1, 100, 500, 1000, 1999, 3000]
is_valueerror = [0, -4, -100, -1996, -2000]
is_typeerror = ['-4', '4', '100', 'ins', '**', '中文']


class TestFix():
    @pytest.fixture(params=is_leap)
    def is_leap(self, request):
        return request.param

    def test_is_leap(self, is_leap):
        assert is_leap_year.is_leap_year(is_leap) == True


if __name__ == "__main__":
    pytest.main()