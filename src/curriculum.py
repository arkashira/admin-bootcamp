import json
from dataclasses import dataclass, field
from typing import List

@dataclass
class Module:
    title: str
    description: str
    prerequisites: List[str] = field(default_factory=list)

@dataclass
class Curriculum:
    title: str
    description: str
    modules: List[Module] = field(default_factory=list)
    published: bool = False

class CurriculumDesignEngine:
    def __init__(self):
        self.curricula = {}

    def create_curriculum(self, title: str, description: str):
        if title in self.curricula:
            raise ValueError("Curriculum with this title already exists")
        self.curricula[title] = Curriculum(title, description)

    def add_module(self, curriculum_title: str, module_title: str, module_description: str):
        if curriculum_title not in self.curricula:
            raise ValueError("Curriculum not found")
        self.curricula[curriculum_title].modules.append(Module(module_title, module_description))

    def edit_module(self, curriculum_title: str, module_title: str, new_title: str, new_description: str):
        if curriculum_title not in self.curricula:
            raise ValueError("Curriculum not found")
        for module in self.curricula[curriculum_title].modules:
            if module.title == module_title:
                module.title = new_title
                module.description = new_description
                return
        raise ValueError("Module not found")

    def delete_module(self, curriculum_title: str, module_title: str):
        if curriculum_title not in self.curricula:
            raise ValueError("Curriculum not found")
        self.curricula[curriculum_title].modules = [module for module in self.curricula[curriculum_title].modules if module.title != module_title]

    def reorder_modules(self, curriculum_title: str, new_order: List[str]):
        if curriculum_title not in self.curricula:
            raise ValueError("Curriculum not found")
        self.curricula[curriculum_title].modules = sorted(self.curricula[curriculum_title].modules, key=lambda module: new_order.index(module.title) if module.title in new_order else float('inf'))

    def define_prerequisites(self, curriculum_title: str, module_title: str, prerequisites: List[str]):
        if curriculum_title not in self.curricula:
            raise ValueError("Curriculum not found")
        for module in self.curricula[curriculum_title].modules:
            if module.title == module_title:
                module.prerequisites = prerequisites
                return
        raise ValueError("Module not found")

    def publish_curriculum(self, curriculum_title: str):
        if curriculum_title not in self.curricula:
            raise ValueError("Curriculum not found")
        self.curricula[curriculum_title].published = True

    def unpublish_curriculum(self, curriculum_title: str):
        if curriculum_title not in self.curricula:
            raise ValueError("Curriculum not found")
        self.curricula[curriculum_title].published = False

    def to_json(self):
        return json.dumps({title: {
            "title": curriculum.title,
            "description": curriculum.description,
            "modules": [{"title": module.title, "description": module.description, "prerequisites": module.prerequisites} for module in curriculum.modules],
            "published": curriculum.published
        } for title, curriculum in self.curricula.items()})
