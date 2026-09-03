import re
class Solution:
    def isPalindrome(self, s: str) -> bool:

        s= re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()

        s_list = list(s)
        print(s_list)

        l , r = 0 , len(s_list) -1

        while l<r:
            if s_list[l] != s_list[r]:
                return False
            l =l+1
            r= r-1

        return True
        