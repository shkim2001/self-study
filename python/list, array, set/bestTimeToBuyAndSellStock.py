class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        
        left, right = 0, 1
        maxPrice = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                maxPrice = max(maxPrice, prices[right] - prices[left])
            else:
                left = right
            
            right += 1
        
        return maxPrice
        # buy = prices[0]
        # mx_profit = 0

        # for i in range(1,len(prices)):
        #     profit = prices[i]-buy

        #     if profit>mx_profit:
        #         mx_profit = profit

        #     if buy>prices[i]:
        #         buy = prices[i]

        # return mx_profit