class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for list1 , i in enumerate(matrix):
            for j in i:
                if j == target:
                    return True
        return False
        