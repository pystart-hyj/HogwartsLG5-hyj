from time import sleep

import pytest


def test_run1():
    sleep(0.5)
    assert 1 == 2

def test_run2():
    sleep(0.5)
    assert 3 == 3

# 失败重跑5次,间隔1s
@pytest.mark.flaky(reruns=5,reruns_delay=1)
def test_run3():
    sleep(0.5)
    assert 5 == 6
