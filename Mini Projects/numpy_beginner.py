# Question1: With your high school reunion fast approaching, you decide to get in shape and lose some weight . You record your weight every day for five weeks starting on a Monday.

# Given these daily weights, build an array with your average weight per weekend1.

import numpy as np

dailywts = 185 - np.arange(5*7)/5

# Reshape the array to have 5 weeks and 7 days
weekly_wts = dailywts.reshape(5,7)

# Calculate the average weight for each weekend (Saturday and Sunday)
weekend_avg_wts = weekly_wts[:, 5:7].mean(axis=1)
print("Question 1:")
print(weekend_avg_wts, "\n")

# Question2: Make the following 4x7 array called nola that starts with 1 and steps by 2. However, note that the first element in each row is always 4 more than the last element in the previous row.
nola = np.arange(start=1, stop=65, step=2).reshape(4,8)[:, :-1]
print("Question 2:")
print(nola, "\n")

# Question3: After binge-watching the discovery channel, you ditch your job as a trial lawyer to become a gold miner  . You decide to prospect five locations underneath a 7x7 grid of land. How much gold do you uncover at each location?
np.random.seed(5555)
gold = np.random.randint(low=0, high=10, size=(7,7))

locs = np.array([
    [0,4],
    [2,2],
    [2,3],
    [5,1],
    [6,3]
])

found_gold = gold[locs[:,0], locs[:,1]]
print("Question 3:")
print(found_gold, "\n")

# Question4: Given a Numpy array, write a function to compute the sum of all its elements. You are given a 1-dimensional Numpy array.

def sum_array(arr):
    return np.sum(arr)

print("Question 4:")
arr = np.array([1, 2, 3, 4, 5])
print("Sum of array elements:", sum_array(arr), "\n")

# Question5: You are given an array arr[] of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). This array represents a permutation of the integers from 1 to n with one element missing. Your task is to identify and return the missing element.

def missing_number(self, arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    arr_sum = np.sum(arr)
    return total_sum - arr_sum

print("Question 5:")
arr = np.array([1, 2, 4, 5, 6])
print("Missing number:", missing_number(None, arr), "\n")

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix