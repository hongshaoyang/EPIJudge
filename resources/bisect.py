import bisect
from collections import namedtuple

# Given an array of students, sorted by descending GPA, with ties broken on name.
# use `bisect` to perform fast searches

Student = namedtuple('Student', ('name', 'gpa'))

def comp_gpa(student: Student):
    return (-student.gpa, student.name)

def search_student(students, target, comp_gpa):
    # custom comparator
    i = bisect.bisect_left([comp_gpa(s) for s in students], comp_gpa(target))
    return 0 <= i < len(students) and students[i] == target

bisect.bisect_left(a, x) # find 1st ele not less than target
bisect.bisect_right(a, x) # find 1st ele greater than target