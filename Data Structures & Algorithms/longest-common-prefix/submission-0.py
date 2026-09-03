class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Compare each character of the first string
        for i in range(len(strs[0])):

            # Compare with every other string
            for j in range(1, len(strs)):

                # If index is out of range or characters don't match
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    print("yes")
                    return strs[0][:i]

        # Entire first string is the common prefix
        return strs[0]
