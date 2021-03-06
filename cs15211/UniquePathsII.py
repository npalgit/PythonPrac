__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/unique-paths-ii.py
# Time:  O(m * n)
# Space: O(m + n)
# DP
#
# Follow up for "Unique Paths":
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
#
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.
#
# Note: m and n will be at most 100.
#
# Bloomberg


class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m ,n = len(obstacleGrid), len(obstacleGrid[0])
        ways = [0] * n

        if obstacleGrid[0][0] == 0:
            ways[0] = 1

        for j in xrange(1, n):
            if obstacleGrid[0][j] == 1:
                ways[j] = 0
            else:
                ways[j] = ways[j - 1]

        for i in xrange(1, m):
            if obstacleGrid[i][0] == 1:
                ways[0] = 0
            for j in xrange(1, n):
                if obstacleGrid[i][j] == 1:
                    ways[j] = 0
                else:
                    ways[j] += ways[j - 1]
        return ways[n - 1]

class SolutionLeetcode:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m ,n = len(obstacleGrid), len(obstacleGrid[0])
        if m == 0:
            return 0
        dp = [[ 0 for i in xrange(n+1)] for j in xrange(m+1)]
        dp[m-1][n] = 1

        for i in reversed(xrange(m)):
            for j in reversed(xrange(n)):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j+1] + dp[i+1][j]
        return dp[0][0]

if __name__ == "__main__":
    obstacleGrid = [
                      [0,0,0],
                      [0,1,0],
                      [0,0,0]
                   ]
    print Solution().uniquePathsWithObstacles(obstacleGrid)
    print SolutionLeetcode().uniquePathsWithObstacles(obstacleGrid)

#java
js = '''
public class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        if (m == 0) {
            return 0;
        }
        int n = obstacleGrid[0].length;
        int[] dp = new int[n];
        for (int i = 0; i < n; i++) {
            if (obstacleGrid[0][i] == 1) {
                break;
            }
            dp[i] = 1;
        }
        for (int i = 1; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (j == 0) {
                    if (obstacleGrid[i][j] == 1) {
                        dp[j] = 0;
                    }
                } else {
                    dp[j] = obstacleGrid[i][j] == 1 ? 0 : dp[j - 1] + dp[j];
                }
            }
        }
        return dp[n - 1];
    }
}
'''