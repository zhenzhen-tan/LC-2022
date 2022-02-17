class Solution
    def containsDuplicate(self, nums):
        if not nums: return False
        cnt = set()
        for i in nums:
            if i in cnt: return True
            else:
                cnt.add(i)
        return False

    # if not nums: return False
    # return len(nums) != len(set(nums))