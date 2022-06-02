import numpy as np
from cvxopt import matrix
from cvxopt.glpk import ilp

# For a given set of coins, find the minimum number of coins to sum up to the given amount

# Example:
# Coins = [1,2,5]
# sum = 11
# Result: 3

# Dynamic Programming approach

def dynamicProgramming(coins, amount):

    dp = [0 for i in range(amount+1)]
    for target in range(1,amount+1):
        for coin in coins:
            if(coin <= target):
                dp[target] = min(dp[target], dp[target-coin]+1)
                
    return dp[amount]

# As an integer programming problem, let [c[0], c[1] ...] be the number of coins of each denomination
# Optimization problem: minimize the sum of the total number of coins for the constraint:
# c[0]*coins[0] + c[1]*coins[1] + ... = amount
# c[0], c[1]... are integers
# GNU linear programming package is used

def integer_linear_problem(coins, amount):

    c = matrix(np.ones(len(coins)).astype(float))
    b = matrix(np.array([amount]).astype(float))
    A = matrix(np.array([coins]).astype(float))
    G = matrix(np.diag(-1 * np.ones(len(coins))).astype(float))
    h = matrix(np.zeros(len(coins)).astype(float))
    I = set(range(len(coins)))
    status,x = ilp(c=c,G=G,h=h,A=A,b=b,I=I)
    if(status == 'optimal'):
        return x;

if(__name__ == "__main__"):
    coins = [1,2,5]
    amount = 11
    print(dynamicProgramming(coins, amount))
    print(integer_linear_problem(coins, amount))


    