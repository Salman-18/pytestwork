import pytest
from src.school import ClassRoom, Teacher, Student, ToManyStudents

# Fixture for creating a sample classroom with a teacher, students, and a course title.
@pytest.fixture


def sample_classroom():
    teacher = Teacher(name="Professor Dumbledore")
    students = [Student(name=f"Student {i+1}") for i in range(10)]
    course_title = "Defense Against the Dark Arts"
    return ClassRoom(teacher, students, course_title)


# Test adding students to a classroom
def test_add_students(sample_classroom):
    new_student = Student(name="Harry Potter")
    sample_classroom.add_students(new_student)
    assert len(sample_classroom.students) == 11
    assert new_student in sample_classroom.students


# Test adding too many students to a classroom
def test_add_too_many_students(sample_classroom):
    with pytest.raises(ToManyStudents):
        for i in range(5):
            student = Student(name=f"Extra Student {i+1}")
            sample_classroom.add_students(student)


# Test removing a student from a classroom
def test_remove_student(sample_classroom):
    student_to_remove = sample_classroom.students[0]
    sample_classroom.remove_student(name=student_to_remove.name)
    assert len(sample_classroom.students) == 9
    assert student_to_remove not in sample_classroom.students


# Test changing the teacher of a classroom
def test_change_teacher(sample_classroom):
    new_teacher = Teacher(name="Professor Snape")
    sample_classroom.change_teacher(new_teacher)
    assert sample_classroom.teacher == new_teacher
