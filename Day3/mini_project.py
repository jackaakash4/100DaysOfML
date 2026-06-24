#challenge
import numpy as np

students = np.array([
    [85,90,88],
    [70,65,72],
    [95,92,98],
    [60,75,70]
])

#Tasks:

"""Calculate mean score per subject.
Calculate highest score per subject.
Normalize the dataset.
Find students with average score > 85. """

mean_score = students.mean(axis = 0)
print("Mean score in each subjects: ", mean_score)

#standard deviation
std = students.std(axis = 0)
print("Standard deviation in each subjects: ", std)

#normalizing the dataset
normalize = students - mean_score / std

print("Normalized data: ", normalize)

highest_score = students.max(axis = 0)
print("Highest score: ", highest_score)
