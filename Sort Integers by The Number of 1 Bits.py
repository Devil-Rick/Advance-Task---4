"""
Given an integer array arr. You have to sort the integers in the array in ascending order by the number of 1's in their binary representation and 
in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the sorted array.
"""
n = list(map(int, input().split(',')))
x = sorted(n, key=lambda x: bin(x).count('1'))
print(x)
