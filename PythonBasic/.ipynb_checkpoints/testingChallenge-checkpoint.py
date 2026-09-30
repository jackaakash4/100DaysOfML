"""
Write pytest-style tests for your Student class:

1. test_average_calculates_correctly() — create a Student with known grades, 
   assert average() returns the expected value
2. test_highest_returns_max_grade() — same idea, for highest()
3. test_student_with_single_grade() — an EDGE CASE: what happens with only 
   one grade in the list? Does average() still work correctly?

Then, a genuinely harder one:
4. test_student_with_empty_grades() — what SHOULD happen if grades = []? 
   Right now, would your Student class crash (like the traceback above), 
   or handle it gracefully? You don't need to fix the class yet — just 
   write a test that reveals what actually happens, and tell me: does it 
   pass or fail against your current code?

"""
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def highest(self):
        return max(self.grades)

    def summary(self):
        return f"{self.name} ({self.age}): avg {self.average():.2f}, highest {self.highest()}"


jack = Student("Jack", 19, [40, 40, 40])

def test_average_calculates_correctly():
    assert jack.average() == 40.00

def test_highest_returns_max_grade():
    assert jack.highest() == 40

def test_student_with_empty_grades():
    assert Student("Jack", 19, []).average()

