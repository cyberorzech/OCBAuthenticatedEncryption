import pytest


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_three(self):
        with pytest.raises(RuntimeError) as excinfo:

            def f():
                f()

            f()
        assert "maximum recursion" in str(excinfo.value)
