import json
from dataclasses import dataclass
from typing import List

@dataclass
class Question:
    id: int
    text: str
    answers: List[str]

@dataclass
class Mentor:
    id: int
    name: str
    expertise: str

class AdminBootcamp:
    def __init__(self):
        self.questions = []
        self.mentors = []

    def add_question(self, question: Question):
        self.questions.append(question)

    def add_mentor(self, mentor: Mentor):
        self.mentors.append(mentor)

    def get_questions(self):
        return self.questions

    def get_mentors(self):
        return self.mentors

    def get_relevant_mentors(self, question: Question):
        relevant_mentors = []
        for mentor in self.mentors:
            if mentor.expertise in question.text:
                relevant_mentors.append(mentor)
        return relevant_mentors

    def get_relevant_questions(self, mentor: Mentor):
        relevant_questions = []
        for question in self.questions:
            if mentor.expertise in question.text:
                relevant_questions.append(question)
        return relevant_questions
