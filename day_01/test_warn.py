import warnings
import pytest


def warn_message():
    warnings.warn("user", UserWarning)
    warnings.warn("runtime", RuntimeWarning)


def test_warn_match():
    with pytest.warns(UserWarning, match='.*u.*') as record:
        # . 匹配任意字符，除了换行符, ^ 匹配字符串的开头, *匹配前面的子表达式零次或多次。要匹配 * 字符，请使用 \*
        warn_message()
    assert len(record) == 2
    assert str(record[0].message) == "user"
    assert str(record[1].message) == "runtime"


if __name__ == "__main__":
    pytest.main()