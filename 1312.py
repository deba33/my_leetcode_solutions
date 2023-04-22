# Minimum Insertion Steps to Make a String Palindrome
class Solution:
    def minInsertions(self, s: str) -> int:
        '''
        This code implements a dynamic programming solution to find the minimum number of insertions required to make a given string s a palindrome. The function takes a string s as input and returns an integer representing the minimum number of insertions required.

        The approach used here is to build a 2D table (dp) where dp[i][j] represents the minimum number of insertions required to make the substring s[i:j+1] a palindrome. The base case is when i=j, in which case dp[i][j]=0. The solution to the problem is then given by dp[0][n-1], where n is the length of the string.

        The code iterates over the table in a bottom-up manner, starting from the bottom-right corner and moving towards the top-left corner. At each iteration, it computes dp[i][j] based on the values of dp[i+1][j], dp[i][j-1], and dp[i+1][j-1]. If s[i] and s[j] are equal, then dp[i][j] is simply equal to dp[i+1][j-1]. Otherwise, we need to insert either s[i] or s[j] to make the substring s[i:j+1] a palindrome. We take the minimum of dp[i+1][j] and dp[i][j-1], which represent the minimum number of insertions required to make the substrings s[i+1:j+1] and s[i:j], respectively, and add 1 to it to account for the insertion of either s[i] or s[j].

        The code uses a 1D array dp instead of a 2D array to store the values of dp[i][j]. This is possible because we only need the values of dp[i+1][j-1], dp[i+1][j], and dp[i][j-1] at each iteration, which can be stored in variables prev, dp[j], and temp, respectively.

        Time complexity: O(n^2)
        Space complexity: O(n)

        :param s: The string to be checked
        :type s: str
        :return: The minimum number of insertions required to make the string s a palindrome
        :rtype: int

        >>> Solution().minInsertions("zzazz")
        0
        >>> Solution().minInsertions("mbadm")
        2
        >>> Solution().minInsertions("leetcode")
        5
        >>> Solution().minInsertions("g")
        0
        >>> Solution().minInsertions("no")
        1
        >>> Solution().minInsertions("mm")
        0
        >>> Solution().minInsertions("aabb")
        1
        >>> Solution().minInsertions("abc")
        2
        >>> Solution().minInsertions("abcde")
        5
        >>> Solution().minInsertions("aab")
        1
        >>> Solution().minInsertions("a")
        0
        >>> Solution().minInsertions("aa")
        0
        >>> Solution().minInsertions("ab")
        1
        '''
        n = len(s)
        dp = [0]*(n)
        for i in range(n-2, -1, -1):
            prev = 0
            for j in range(i+1, n):
                temp = dp[j]
                if s[i] == s[j]:
                    dp[j] = prev
                else:
                    dp[j] = min(dp[j], dp[j-1])+1
                prev = temp
        return dp[n-1]
