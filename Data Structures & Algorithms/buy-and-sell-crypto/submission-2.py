class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_amt = 0
        l = 0
        r = l

        while r < len(prices):
            diff = prices[r] - prices[l]
            print(prices[r], prices[l])

            if diff < 0:
                l = r
            else:
                max_amt = max(max_amt, diff)

            r += 1
        return max_amt

        