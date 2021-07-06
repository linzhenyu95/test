#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# @Author   :Lins
# @Time     :2021/7/7 1:01
# @File     :demo.py
import pytest
import pytest
# 作用域：module是在是在模块之前执行，模块之后执行
@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    yield

    print("执行teardown!")
    print("最后关闭浏览器")

def test_search1(open):
    print("test_search1")
    raise NameError
    pass

def test_search2(open):
    print("test_search2")
    pass
if __name__== '__main__':
    pytest.main()