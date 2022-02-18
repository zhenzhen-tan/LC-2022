class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2: return []
        nums1cnt = Counter(nums1)
        res = []
        for num in nums2:
            if num in nums1cnt and nums1cnt[num] > 0:
                res.append(num)
                nums1cnt[num] -= 1
        return res

#What if the given array is already sorted? How would you optimize your algorithm?
#用两个指针指向当前两个数组的遍历点, index1,index2.

#<1. 如果 nums1[index1]=nums2[index2]，将nums1[index1]加入结果，两个指针都+1，

#<2. 如果nums1[index1]>nums2[index2]，index2指针＋１

#<3.如果nums2[index1]<nums2[index2]，index1指针+1

#What if nums1's size is small compared to nums2's size? Which algorithm is better?

#What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
