import pytest
from pytest_tdd_app import Task, add

def test_add_raises():
    """add() should raise an execption with wrong type param."""
    with pytest.raises(TypeError):
        add(task='not a Task object')