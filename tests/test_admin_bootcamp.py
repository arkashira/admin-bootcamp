from admin_bootcamp import AdminBootcamp, Question, Mentor

def test_add_question():
    bootcamp = AdminBootcamp()
    question = Question(1, "What is Python?", ["Python is a programming language"])
    bootcamp.add_question(question)
    assert len(bootcamp.get_questions()) == 1

def test_add_mentor():
    bootcamp = AdminBootcamp()
    mentor = Mentor(1, "John Doe", "Python")
    bootcamp.add_mentor(mentor)
    assert len(bootcamp.get_mentors()) == 1

def test_get_relevant_mentors():
    bootcamp = AdminBootcamp()
    question = Question(1, "What is Python?", ["Python is a programming language"])
    mentor = Mentor(1, "John Doe", "Python")
    bootcamp.add_question(question)
    bootcamp.add_mentor(mentor)
    relevant_mentors = bootcamp.get_relevant_mentors(question)
    assert len(relevant_mentors) == 1

def test_get_relevant_questions():
    bootcamp = AdminBootcamp()
    question = Question(1, "What is Python?", ["Python is a programming language"])
    mentor = Mentor(1, "John Doe", "Python")
    bootcamp.add_question(question)
    bootcamp.add_mentor(mentor)
    relevant_questions = bootcamp.get_relevant_questions(mentor)
    assert len(relevant_questions) == 1

def test_edge_case_empty_questions():
    bootcamp = AdminBootcamp()
    assert len(bootcamp.get_questions()) == 0

def test_edge_case_empty_mentors():
    bootcamp = AdminBootcamp()
    assert len(bootcamp.get_mentors()) == 0
