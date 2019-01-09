# my code
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buyFlag = 0
        win = 0
        for i in range(len(prices)):
            if i == len(prices)-1:
                if not buyFlag:
                    break
                if buyFlag:
                    win = win + prices[i]
                    break
            # 第二天涨了
            if prices[i+1] > prices[i]:
                if not buyFlag:
                    win = win - prices[i]
                    buyFlag = 1
            # 第二天跌了
            else:
                if buyFlag:
                    win = win + prices[i]
                    buyFlag = 0
        return win
            

# others
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        win = 0
        for i in range(len(prices)-1):
			cha = prices[i+1] - prices[i]
            if cha > 0:
                win = win + cha
        return win                
