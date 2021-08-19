'''
3. Write a NumPy program to create a structured array from given student name, height,
class and their data types. Now sort by class, then height if class are equal.

'''

import numpy as np

data_type = [("name","S5"),("class",int),("height",float )]
np_array =[('James', 5, 48.5), ('Nail', 6, 52.5),('Paul', 5, 42.10), ('Pit', 5, 40.11)]
# create a structured array
students = np.array(np_array, dtype=data_type)   
print("Original array:")
print(students)
print("Sort by class, then height if class are equal:")
print(np.sort(students, order=['class', 'height']))