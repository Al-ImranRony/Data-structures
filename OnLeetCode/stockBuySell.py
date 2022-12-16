'''
Tech Interview Prep Group task - Session 4.
Stock Buy and Sell, in Python
Time complexity: O()
'''


def maxProfit(prices: list) -> int:
    buy, maxProfit = float('inf'), 0
    for price in prices:
        buy = min(buy, price)

        if (price-buy > maxProfit):
            maxProfit =  price-buy
        
    return maxProfit

print(maxProfit([7,1,5,3,6,4]))