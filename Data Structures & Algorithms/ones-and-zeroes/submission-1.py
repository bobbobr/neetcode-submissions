class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        dp = [[0] * (n+1) for i in range(m+1)]

        for s in strs:

            ones = s.count('1')
            zeros = s.count('0')

            for i in range(len(dp)-1, zeros-1, -1):
                for j in range(len(dp[0])-1, ones-1, -1):
                    dp[i][j] = max(
                        dp[i][j],
                        dp[i-zeros][j-ones] + 1
                    )
        return dp[-1][-1]

        