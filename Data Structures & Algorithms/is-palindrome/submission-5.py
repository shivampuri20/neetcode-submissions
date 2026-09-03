import re
class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_list = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        l , r = 0 , len(s_list) -1

        while l<r:
            if s_list[l] != s_list[r]:
                return False
            l =l+1
            r= r-1

        return True
        