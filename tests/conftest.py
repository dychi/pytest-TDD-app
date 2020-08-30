import pytest

@pytest.fixture(scope='session')
def tasks_db(tmpdir_factory):
    temp_dir = tmpdir_factory.mktemp('temp')
    print("Start db connection.", temp_dir)
    yield
    print("Teardown db connection.")