import requests
import pytest


def test_one():
    r = requests.get('https://api.github.com/events')
    assert r.status_code == 200


def test_two():
    r = requests.get('https://api.github.com/events')
    assert r.encoding == 'utf', "断言失败编码错误,实际编码为:{}".format(r.encoding)


if __name__ == "__main__":
    pytest.main()
