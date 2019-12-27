import pytest
import sys


@pytest.mark.xfail(raises=AssertionError)
def test_01():
    assert 1 == 2


@pytest.mark.me
def test_02():
    if isinstance('1234', int) is not True:
        raise TypeError("传入参数非整数")


if __name__ == '__main__':
    pytest
