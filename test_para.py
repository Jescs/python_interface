import is_leap_year
import pytest


class TestPara():
    def test_is_leap(self, is_leap_y):
        assert is_leap_year.is_leap_year(is_leap_y) == True

    def test_is_typeerror(self, is_type_error):
        with pytest.raises(TypeError):
            is_leap_year.is_leap_year(is_type_error)


if __name__ == "__main__":
    pytest.main()
