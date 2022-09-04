# Dynamic Programming

## Study links

- [Demystifying Dynamic Programming](https://medium.freecodecamp.org/demystifying-dynamic-programming-3efafb8d4296)
- [Dynamic Programming – 7 Steps to Solve any DP Interview Problem](https://dev.to/nikolaotasevic/dynamic-programming--7-steps-to-solve-any-dp-interview-problem-3870)

## Notes[​](#notes "Direct link to heading")

- Dynamic Programming (DP) is usually used to solve optimization problems. The only way to get better at DP is to practice. It takes some amount of practice to be able to recognize that a problem can be solved by DP.

- Sometimes you do not need to store the whole DP table in memory, the last two values or the last two rows of the matrix will suffice.

### Core step to play with during problem analysis

- Define the objective function, _**in words not equation**_
  - dp[i] is ...
- Identify base cases
  - dp[0] = ? or dp[n] = ? or dp[1] = ?
- Write down a recurrence relation (Transition function) for the optimized objective function
  - dp[n] = dp[whatever] +- dp[whatever]
- What's the order of execution?
  - bottom-up or top-down
- Where to look for the answer?

  - dp[0] or dp[-1] or ...

Example: **Climbing Stairs**, You are climbing a stair case. It takes n steps to reach to the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

- Define the objective function
  - dp[i] is the number of distinct ways to reach the i-th stair.
- Identify base cases
  - dp[0] = 1
  - dp[1] = 1
- Write down a recurrence relation for the optimized objective function
  - dp[n] = dp[n-1] + dp[n-2]
- What's the order of execution?
  - bottom-up
- Where to look for the answer?
  - dp[n]

```python
def climbCount(n: int) -> int:
    dp = [0] * (n+1)
    dp[0] = dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

```

## LC

- [0/1 Knapsack or Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
- [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
- [Coin Change](https://leetcode.com/problems/coin-change/)
- [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
- [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
- [Word Break Problem](https://leetcode.com/problems/word-break/)
- [Combination Sum](https://leetcode.com/problems/combination-sum-iv/)
- [House Robber](https://leetcode.com/problems/house-robber/) and [House Robber II](https://leetcode.com/problems/house-robber-ii/)
- [Decode Ways](https://leetcode.com/problems/decode-ways/)
- [Unique Paths](https://leetcode.com/problems/unique-paths/)
- [Jump Game](https://leetcode.com/problems/jump-game/)
