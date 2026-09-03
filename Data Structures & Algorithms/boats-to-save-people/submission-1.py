class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        p1,p2 = 0,len(people)-1
        people.sort()
        boat =0
        if len(people)==1:
            return 1

        while p1 <= p2:
            if people[p1] + people[p2] <= limit:
                p1+=1
                p2-=1
            else:
                p2-=1
            boat+=1

        return boat
                