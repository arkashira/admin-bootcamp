import json
from dataclasses import dataclass
from typing import List

@dataclass
class Module:
    name: str
    learning_objective: str
    estimated_completion_time: int
    assessment: str

class AdminBootcamp:
    def __init__(self, modules: List[Module]):
        self.modules = modules
        self.current_module_index = 0

    def get_current_module(self):
        return self.modules[self.current_module_index]

    def get_next_module(self):
        if self.current_module_index < len(self.modules) - 1:
            return self.modules[self.current_module_index + 1]
        return None

    def pass_assessment(self):
        self.current_module_index += 1

    def get_learning_path(self):
        return self.modules
