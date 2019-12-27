from selenium import webdriver
import time


def test_get_01(browser:webdriver.Firefox):
    browser.get("http://baidu.com")
    time.sleep(2)
    t = browser.title
    assert "百度" in t
