class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))

        count =0
        count1 = 0 

        if len(nums) ==0:
            return 0

        tem_ele = nums[0]
        for i in range(len(nums)):
            if tem_ele +1  == nums[i]:
                count +=1
                tem_ele = nums[i]
            elif nums[i] - tem_ele >1:
                tem_ele =nums[i]
                count1 = max(count , count1)
                count =0
        count1 = max(count , count1)

        return count1+1
        