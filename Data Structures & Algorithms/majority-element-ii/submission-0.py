class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        hash_map = {}
        sets = set()


        for i in range(len(nums)):
            hash_map[nums[i]] = hash_map.get(nums[i], 0) +1

            if nums_len  // 3 < hash_map[nums[i]]:
                sets.add(nums[i])

        return list(sets)
        