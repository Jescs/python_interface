import sys
import pytest
from day_01 import is_leap_year

sys.path.append(".")


class TestAssert:
    def test_exception_value(self):
        with pytest.raises(ValueError, match='公元元年是从公元一年开始的') as excinfo:  # 预测输入某些特定数据，会抛出特定异常，若出现特定异常，则用例执行通过。
            is_leap_year.is_leap_year(0)
        assert "从公元一年开始" in str(excinfo.value)
        assert excinfo.type == ValueError

    def test_true(self):
        assert is_leap_year.is_leap_year(400) == True

    @pytest.mark.xfail(raises=ValueError)
    def test_a(self):
        is_leap_year.is_leap_year(-100)


if __name__ == "__main__":
    pytest.main()