import pytest
from actions_poetry_cache import add_one


def test_actions():
    a = 1
    b = add_one(a)
    assert a == 1
    assert b == 2
