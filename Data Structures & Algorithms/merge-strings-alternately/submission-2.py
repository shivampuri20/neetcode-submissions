class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge_list = []

        result = word1 if len(word1) > len(word2) else word2

        for i in range(len(result)):
            if i < len(word1):
                merge_list.append(word1[i])
            if i < len(word2):
                merge_list.append(word2[i])

        return (''.join(merge_list))
        