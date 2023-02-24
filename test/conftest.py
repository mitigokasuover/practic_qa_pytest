import pytest

@pytest.fixture()
def set_up():
    print("sing in system")
    yield
    print("exit system")

@pytest.fixture(scope="function")
def some():
    print("start")
    yield
    print("end procces")