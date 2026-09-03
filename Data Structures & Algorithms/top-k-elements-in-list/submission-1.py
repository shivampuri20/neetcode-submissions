class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map ={}
        for i in range(len(nums)):
            hash_map[nums[i]] = hash_map.get(nums[i], 0) +1
        
        fq_no = sorted(hash_map.items(), key =lambda x: x[1], reverse =True)[:k]
        output = [num[0] for num in fq_no]
        return output
        