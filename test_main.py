import pytest
from main import Student


# Create student for test
@pytest.fixture
def student():
    return Student("John Billder ", "subject.csv")

# Then a test to verify that the student's creation is correct.
def test_student_creatin(student):
    assert student.name == "John Billder ", "False"
    assert student.subject == {'Математика': {'grade': [], 'test_score': []}, 
                            'Физика': {'grade': [], 'test_score': []}, 
                            'История': {'grade': [], 'test_score': []}, 
                            'Литература': {'grade': [], 'test_score': []}}


# Test that func(student_grade)
def test_student_grade(student):
    student.add_grade("Физика", 5)
    assert student.subject["Физика"]["grade"][0] == 5, "False"

# Test that func(add_test_score)
def test_add_test_score(student):
    student.add_test_score("Математика", 87)
    assert student.subject["Математика"]["test_score"][0] == 87, "False"
    