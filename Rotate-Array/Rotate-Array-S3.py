def reverse(nums, i, j):
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    return


class Solution:
    # rotate (0, len(nums) - k - 1)
    # rotate (len(nums) - k, len(nums) - 1)
    # rotate the whole array
    # time O(n), space O(1)
    def rotate(nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        reverse(nums, 0, n - k - 1)
        reverse(nums, n - k, n - 1)
        reverse(nums, 0, n - 1)
        print(nums)
        return


if __name__ == "__main__":
    print(Solution.rotate([3, 9, -1, 100], 2))
