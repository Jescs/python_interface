import is_leap_year
import pytest


class TestPara():
    is_leap = [4, 40, 400, 800, 1992, 2996]
    is_typeerror = ['-4', '4', '100', 'ins', '**', '中文']

    @pytest.mark.parametrize('year', is_leap)
    def test_is_leap(self, year):
        assert is_leap_year.is_leap_year(year) == True

    @pytest.mark.parametrize('year', is_typeerror)
    def test_is_typeerror(self, year):
        with pytest.raises(TypeError):
            is_leap_year.is_leap_year(year)

    value = [(4, True), (40, True), (400, True), (800, True), (1992, True), (2996, True)]

    @pytest.mark.parametrize('year, assert_value', value)
    def test_is_leap(self, year, assert_value):
        assert is_leap_year.is_leap_year(year) == assert_value

    value_error = [(0, ValueError), ('-4', TypeError), (-4, ValueError), ('ss', TypeError), ('中文', TypeError), ('**', TypeError)]

    @pytest.mark.parametrize('year,assert_value',value_error)
    def test_is_typeerror(self,year, assert_value):
        if assert_value == ValueError:
            with pytest.raises(ValueError) as excinfo:
                is_leap_year.is_leap_year(year)
            assert excinfo.type == assert_value
        else:
            with pytest.raises(TypeError) as excinfo:
                is_leap_year.is_leap_year(year)
            assert excinfo.type == assert_value


if __name__ == "__main__":
    pytest.main()
