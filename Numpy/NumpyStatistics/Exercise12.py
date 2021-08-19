'''
12. Write a Python NumPy program to compute the weighted average along
 the specified axis of a given flattened array.
From Wikipedia: The weighted arithmetic mean is similar to an ordinary
arithmetic mean (the most common type of average), except that instead
of each of the data points contributing equally to the final average,
some data points contribute more than others. The notion of weighted
mean plays a role in descriptive statistics and also occurs in a more
general form in several other areas of mathematics.

'''

import numpy as np

np_array = np.arange(9).reshape(3,3)
print(np_array)

r1 = np.average(np_array,axis=1, weights=[1./4,2./4,2./4])
print(r1)


'''
The weighted arithmetic mean is similar to an ordinary arithmetic mean (the most common type of average), except that instead of each of the data points contributing equally to the final average, some data points contribute more than others. The notion of weighted mean plays a role in descriptive statistics and also occurs in a more general form in several other areas of mathematics.

Basic example
Given two school classes, one with 20 students, and one with 30 students, the grades in each class on a test were:
Morning class = 62, 67, 71, 74, 76, 77, 78, 79, 79, 80, 80, 81, 81, 82, 83, 84, 86, 89, 93, 98
Afternoon class = 81, 82, 83, 84, 85, 86, 87, 87, 88, 88, 89, 89, 89, 90, 90, 90, 90, 91, 91, 91, 92, 92, 93, 93, 94, 95, 96, 97, 98, 99
The straight average for the morning class is 80 and the straight average of the afternoon class is 90. The straight average of 80 and 90 is 85, the mean of the two class means. However, this does not account for the difference in number of students in each class (20 versus 30); hence the value of 85 does not reflect the average student grade (independent of class). The average student grade can be obtained by averaging all the grades, without regard to classes (add all the grades up and divide by the total number of students):
x = 430050 = 86.
Or, this can be accomplished by weighting the class means by the number of students in each class (using a weighted mean of the class means):
x = (20 x 80)+(30 x 90)20 + 30 = 86.
Thus, the weighted mean makes it possible to find the average student grade in the case where only the class means and the number of students in each class are available.
'''


