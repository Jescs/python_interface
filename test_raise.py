import sys
import pytest
import is_leap_year

sys.path.append(".")


class TestAssert:
    def test_exception_typeerror(self):
        with pytest.raises(ValueError):  # 预测输入某些特定数据，会抛出特定异常，若出现特定异常，则用例执行通过。
            is_leap_year.is_leap_year(0)

    def test_true(self):
        assert is_leap_year.is_leap_year(400) == True


if __name__ == "__main__":
    pytest.main()