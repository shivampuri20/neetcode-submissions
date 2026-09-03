class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        temp_nums = nums
        concat_nums = []
        concat_nums = temp_nums + nums
        return concat_nums