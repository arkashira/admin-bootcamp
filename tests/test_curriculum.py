import pytest
from curriculum import CurriculumDesignEngine, Module, Curriculum

def test_create_curriculum():
    engine = CurriculumDesignEngine()
    engine.create_curriculum("Test Curriculum", "This is a test curriculum")
    assert "Test Curriculum" in engine.curricula

def test_add_module():
    engine = CurriculumDesignEngine()
    engine.create_curriculum("Test Curriculum", "This is a test curriculum")
    engine.add_module("Test Curriculum", "Test Module", "This is a test module")
    assert len(engine.curricula["Test Curriculum"].modules) == 1

def test_edit_module():
    engine = CurriculumDesignEngine()
    engine.create_curriculum("Test Curriculum", "This is a test curriculum")
    engine.add_module("Test Curriculum", "Test Module", "This is a test module")
    engine.edit_module("Test Curriculum", "Test Module", "New Test Module", "This is a new test module")
    assert engine.curricula["Test Curriculum"].modules[0].title == "New Test Module"

def test_delete_module():
    engine = CurriculumDesignEngine()
    engine.create_curriculum("Test Curriculum", "This is a test curriculum")
    engine.add_module("Test Curriculum", "Test Module", "This is a test module")
    engine.delete_module("Test Curriculum", "Test Module")
    assert len(engine.curricula["Test Curriculum"].modules) == 0

def test_reorder_modules():
    engine = CurriculumDesignEngine()
    engine.create_curriculum("Test Curriculum", "This is a test curriculum")
    engine.add_module("Test Curriculum", "Test Module 1", "This is a test module 1")
    engine.add_module("Test Curriculum", "Test Module 2", "This is a test module 2")
    engine.reorder_modules("Test Curriculum", ["Test Module 2", "Test Module 1"])
    assert engine.curricula["Test Curriculum"].modules[0].title == "Test Module 2"

def test_define_prerequisites():
    engine = CurriculumDesignEngine()
    engine.create_curriculum("Test Curriculum", "This is a test curriculum")
    engine.add_module("Test Curriculum", "Test Module", "This is a test module")
    engine.define_prerequisites("Test Curriculum", "Test Module", ["Prerequisite 1", "Prerequisite 2"])
    assert engine.curricula["Test Curriculum"].modules[0].prerequisites == ["Prerequisite 1", "Prerequisite 2"]

def test_publish_curriculum():
    engine = CurriculumDesignEngine()
    engine.create_curriculum("Test Curriculum", "This is a test curriculum")
    engine.publish_curriculum("Test Curriculum")
    assert engine.curricula["Test Curriculum"].published

def test_unpublish_curriculum():
    engine = CurriculumDesignEngine()
    engine.create_curriculum("Test Curriculum", "This is a test curriculum")
    engine.publish_curriculum("Test Curriculum")
    engine.unpublish_curriculum("Test Curriculum")
    assert not engine.curricula["Test Curriculum"].published
