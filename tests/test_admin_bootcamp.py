import pytest
from admin_bootcamp import AdminBootcamp, Module

@pytest.fixture
def modules():
    return [
        Module("Module 1", "Learn sysadmin concepts", 30, "Assessment 1"),
        Module("Module 2", "Learn advanced sysadmin concepts", 60, "Assessment 2"),
        Module("Module 3", "Learn expert sysadmin concepts", 90, "Assessment 3"),
    ]

def test_get_current_module(modules):
    bootcamp = AdminBootcamp(modules)
    assert bootcamp.get_current_module().name == "Module 1"

def test_get_next_module(modules):
    bootcamp = AdminBootcamp(modules)
    assert bootcamp.get_next_module().name == "Module 2"

def test_pass_assessment(modules):
    bootcamp = AdminBootcamp(modules)
    bootcamp.pass_assessment()
    assert bootcamp.get_current_module().name == "Module 2"

def test_get_learning_path(modules):
    bootcamp = AdminBootcamp(modules)
    assert len(bootcamp.get_learning_path()) == 3

def test_get_next_module_last_module(modules):
    bootcamp = AdminBootcamp(modules)
    bootcamp.current_module_index = len(modules) - 1
    assert bootcamp.get_next_module() is None
