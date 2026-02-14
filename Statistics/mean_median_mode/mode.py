import numpy

# Let consider all the emarks of students in the English test
#  out of 15

marksOfAllStudents = [2, 2, 2, 2, 5, 5, 6, 8, 11]

x = max(set(marksOfAllStudents), key=marksOfAllStudents.count)
print(x) 