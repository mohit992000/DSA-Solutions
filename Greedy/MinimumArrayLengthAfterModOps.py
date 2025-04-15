from math import gcd
from functools import reduce

class Solution:
    def minimumArrayLength(self, nums):
        overall_gcd = reduce(gcd, nums)
        return 1 if overall_gcd == 1 else 2
