class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result =[]


        prefix = 1

        result = len(nums) * [prefix]
        for i in range(len(nums)):
            result[i] = prefix
            prefix = nums[i] * prefix

        suffix = 1

        for i in range(len(nums)-1 , -1 , -1):
            result[i] = result[i] * suffix 
            suffix = suffix * nums[i]

        return result


        