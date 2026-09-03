class Solution:
    def isValid(self, s: str) -> bool:
        list1 = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for i in s:
            if i in closeToOpen:
                if list1 and list1[-1] == closeToOpen[i]:
                    list1.pop()
                else:
                    return False
            else:
                list1.append(i)

        if len(list1) == 0:
            return True
        else:
            return False
        