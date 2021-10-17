"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""
n = list(map(int, input().split(',')))
for i in n:
    if n.count(i) == 1:
        print(i)
