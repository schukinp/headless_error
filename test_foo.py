import pytest


@pytest.mark.usefixtures('setup')
class TestFoo:
    def test_one(self):
        pass

    def test_two(self):
        pass
