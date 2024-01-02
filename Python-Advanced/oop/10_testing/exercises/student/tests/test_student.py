from unittest import TestCase, main
from project.student import Student


class StudentTests(TestCase):
    def setUp(self) -> None:
        courses = {'Course 1': [1, 2, 3], 'Course 2': [4, 5]}
        self.student = Student('Name', courses)

    def test_student_initialization_without_courses(self):
        student = Student('Name', None)
        self.assertEqual('Name', student.name)
        self.assertEqual({}, student.courses)

    def test_student_initialization_with_courses(self):
        courses = {'Course 1': [1, 2, 3], 'Course 2': [2, 3]}
        student = Student("Name", courses)
        self.assertEqual('Name', student.name)
        self.assertEqual({'Course 1': [1, 2, 3], 'Course 2': [2, 3]}, student.courses)

    def test_enroll_an_already_enrolled_course_with_adding_notes(self):
        course = 'Course 1'
        notes = [6, 7]
        expected_result = "Course already added. Notes have been updated."
        actual_result = str(self.student.enroll('Course 1', notes))
        self.assertEqual(expected_result, actual_result)
        self.assertEqual([1, 2, 3, 6, 7], self.student.courses[course])

    def test_enroll_an_already_enrolled_course_without_adding_notes(self):
        course = 'Course 1'
        notes = []
        expected_result = "Course already added. Notes have been updated."
        actual_result = str(self.student.enroll(course, notes))
        self.assertEqual(expected_result, actual_result)
        self.assertEqual([1, 2, 3], self.student.courses[course])

    def test_enroll_a_course_with_adding_notes_by_default(self):
        course = 'Course 3'
        notes = [6, 7]
        expected_result = "Course and course notes have been added."
        actual_result = str(self.student.enroll(course, notes))
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(notes, self.student.courses[course])

    def test_enroll_a_course_with_adding_blank_notes_by_default(self):
        course = 'Course 3'
        notes = []
        expected_result = "Course and course notes have been added."
        actual_result = str(self.student.enroll(course, notes))
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(notes, self.student.courses[course])

    def test_enroll_a_course_with_adding_notes_by_command_y(self):
        course = 'Course 3'
        notes = [6, 7]
        add_course_notes = 'Y'
        expected_result = "Course and course notes have been added."
        actual_result = str(self.student.enroll(course, notes, add_course_notes))
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(notes, self.student.courses[course])

    def test_enroll_a_course_with_adding_blank_notes_by_command_y(self):
        course = 'Course 3'
        notes = []
        add_course_notes = 'Y'
        expected_result = "Course and course notes have been added."
        actual_result = str(self.student.enroll(course, notes, add_course_notes))
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(notes, self.student.courses[course])

    def test_enroll_a_course_with_adding_blank_notes_by_command_n(self):
        course = 'Course 3'
        notes = []
        add_course_notes = 'N'
        expected_result = "Course has been added."
        actual_result = str(self.student.enroll(course, notes, add_course_notes))
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(notes, self.student.courses[course])

    def test_enroll_a_course_with_adding_notes_by_command_n(self):
        course = 'Course 3'
        notes = [1, 2]
        add_course_notes = 'N'
        expected_result = "Course has been added."
        actual_result = str(self.student.enroll(course, notes, add_course_notes))
        self.assertEqual(expected_result, actual_result)
        self.assertEqual([], self.student.courses[course])

    def test_add_notes_to_a_non_existing_course(self):
        course = 'Course 3'
        notes = [1, 2]
        with self.assertRaises(Exception) as ex:
            self.student.add_notes(course, notes)
        expected_result = "Cannot add notes. Course not found."
        actual_result = str(ex.exception)
        self.assertEqual(expected_result, actual_result)

    def test_add_blank_notes_to_a_non_existing_course(self):
        course = 'Course 3'
        notes = []
        with self.assertRaises(Exception) as ex:
            self.student.add_notes(course, notes)
        expected_result = "Cannot add notes. Course not found."
        actual_result = str(ex.exception)
        self.assertEqual(expected_result, actual_result)

    def test_add_notes_to_an_existing_course(self):
        course = 'Course 1'
        notes = 6
        expected_result = "Notes have been updated"
        actual_result = self.student.add_notes(course, notes)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual([1, 2, 3, 6], self.student.courses[course])

    def test_leave_non_existing_course(self):
        course = 'Course 3'
        with self.assertRaises(Exception) as ex:
            self.student.leave_course(course)
        expected_result = "Cannot remove course. Course not found."
        actual_result = str(ex.exception)
        self.assertEqual(expected_result, actual_result)

    def test_leave_an_existing_course(self):
        course = 'Course 1'
        expected_result = "Course has been removed"
        actual_result = self.student.leave_course(course)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual({'Course 2': [4, 5]}, self.student.courses)


if __name__ == '__main__':
    main()
