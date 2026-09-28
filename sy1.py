def coin_change(coins,amount):
    dp=[amount+1]*(amount+1)

    dp[0]=0

    for i in range(1,amount+1):
        for coin in coins:
            if coin<=i:
                dp[i]=min(dp[i],dp[i-coin]+1)

    if dp[amount]==amount+1:
        return -1

    return dp[amount]

coins=[1,2,5]
amount=11

result=coin_change(coins,amount)

if result==-1:
    print("Amount cannot be formed with the given coins.")
else:
    print("Minimum no of coins :",result)