class Solution:
    def searchInsert(self, nums: List[int], k: int) -> int:

        l = 0
        r = len(nums) -1

        while l <=r:

            m = (l + r) //2
            if k == nums[m]:
                return m 
            if k > nums[m]:
                l = m +1
            else:
                r = m -1

        return l
        