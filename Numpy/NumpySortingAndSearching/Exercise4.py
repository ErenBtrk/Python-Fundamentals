'''
4. Write a NumPy program to sort the student id with increasing height
of the students from given students id and height. Print the integer
indices that describes the sort order by multiple columns and the sorted data

'''

import numpy as np
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40., 42., 45., 41., 38., 40., 42.0])
#Sort by studen_id then by student_height
indices = np.lexsort((student_id, student_height))
print("Sorted indices:")
print(indices)
print("Sorted data:")
for n in indices:
  print(student_id[n], student_height[n])