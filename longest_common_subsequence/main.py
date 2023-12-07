class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1) + 1, len(text2) + 1

        dp = [[0] * cols for _ in range(rows)]

        for i in range(rows - 2, -1, -1):
            for j in range(cols - 2, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]
