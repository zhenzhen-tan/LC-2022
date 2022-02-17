class Solution:
    # insert the last item in the list to the first position
    # delete the last item
    # repeat for k %= n times
    def rotate(nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        for _ in range(k):
            nums.insert(0, nums[-1])
            nums.pop()
        print(nums)


if __name__ == "__main__":
    print(Solution.rotate([3,9,-1,100],2))