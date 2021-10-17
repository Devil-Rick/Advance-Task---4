"""
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
"""
n = list(map(int, input().split(',')))
x = []
for i in n:
    if n.count(i) == 1:
        x.append(i)
print(x)
