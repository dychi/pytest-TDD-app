import pytest

@pytest.fixture()
def tasks_db():
    print("Start db connection.")
    yield
    print("Teardown db connection.")