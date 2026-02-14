import numpy

# Let consider all the emarks of students in the English test
#  out of 100

marksOfAllStudents = [45, 92, 36, 49, 62, 46, 82, 72, 91, 66]
marksOfAllStudents.sort()
x = numpy.median(marksOfAllStudents)
print(x) // 64.0