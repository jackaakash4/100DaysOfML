#Coding challenge: z-scores for inference times
import numpy as np

times = np.array([
    102,
    98,
    105,
    101,
    100,
    97,
    99,
    350
])

"""
Task 1

Calculate:

Mean
Standard deviation
"""

print(f"Mean: {np.mean(times)} and standard deviation is {np.std(times)}")



"""

Compute the Z-score of each value.

Formula:

z = (x - mean) / std

Hint:

z_scores = (times - np.mean(times)) / np.std(times)

"""
zscore = (times - np.mean(times))/np.std(times)
print("Z-score : ", zscore)


"""
Task 3

Print all values where:

|z| > 2

or, for stricter detection:

|z| > 3

Question:

Is 350 ms a statistically unusual inference time?
Yes, 350ms is a statistically unusual inference time because the zscore of that value is above 2 which is consider unusual
"""

print("All values where |z| is greater then 3: ")
for i in zscore:
    if np.abs(i) > 2:
        print(i)
