class Solution:
    # 利用Python的数组slice的操作和赋值，实际上相当于创建了两个新的数组，
    # 分别保存原数组的前后部分，再依次将元素赋值给原数组。
    # 时间复杂度O(n)，空间复杂度O(n)
    # a[start:stop]  # items start through stop-1
    # a[start:]  # items start through the rest of the array
    # a[:stop]  # items from the beginning through stop-1
    # a[:]  # a copy of the whole array
    def rotate(nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums[:k], nums[k:] = nums[n - k:], nums[:n - k]
        print(nums)
        return


if __name__ == "__main__":
    print(Solution.rotate([3, 9, -1, 100], 2))
