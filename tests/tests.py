import pytest

from src.associated_data_hash import *


class TestClass:
    def test_hash_associated_data(self):
        print(type(hash(1, 4)))
        assert 1 == 1

    # def test_one(self):
    #     x = "this"
    #     assert "h" in x

    # def test_three(self):
    #     with pytest.raises(RuntimeError) as excinfo:

    #         def f():
    #             f()

    #         f()
    #     assert "maximum recursion" in str(excinfo.value)
