class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for key in counter:
            if counter[key] == 1: return key