__source__ = 'https://leetcode.com/problems/2-keys-keyboard/description/'
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 650. 2 Keys Keyboard
#
# Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:
#
# Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
# Paste: You can paste the characters which are copied last time.
# Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted.
# Output the minimum number of steps to get n 'A'.
#
# Example 1:
# Input: 3
# Output: 3
# Explanation:
# Intitally, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.
# Note:
# The n will be in the range [1, 1000].
# Companies
# Microsoft
# Related Topics
# Dynamic Programming
# Similar Questions
# 4 Keys Keyboard


import unittest
# 45 ms
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in xrange(2, n + 1):
            while n % i == 0:
                res += i
                n = n / i
        return res

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
To get the DP solution, analyse the pattern first by generating first few solutions
1: 1
2: 2
3: 3
4: 4
5: 5
6: 5
7: 7
8: 6
9: 6
10: 7
11: 11
12: 7
13: 13
14: 14
15: 8

Now, check the solution.
Eg: n=6
To get 6, we need to copy 3 'A's two time. (2)
To get 3 'A's, copy the 1 'A' three times. (3)
So the answer for 6 is 5

Now, take n=9.
We need the lowest number just before 9 such that (9% number =0). So the lowest number is 3.
So 9%3=0. We need to copy 3 'A's three times to get 9. (3)
For getting 3 'A's, we need to copy 1 'A' three times. (3)
So the answer is 6

Finally to analyse the below code, take n=81.
To get 81 we check
if (81 % 2 ==0) No
if (81 % 3 ==0) Yes
So we need to copy 81/3 = 27 'A's three times (3)
Now to get 27 'A's, we need to copy 27/3= 9 'A's three times (3)
To get 9 'A's, we need to copy 9/3=3 'A's three times (3)
And to get 3 'A's, we need to copy 3/3=1 'A's three times (3)
Final answer is 3+3+3+3 = 12

Last Example, n=18
18/2 = 9 Copy 9 'A's 2 times (2)
9/3=3 Copy 3 'A's 3 times (3)
3/3=1 Copy 1'A's 3 times (3)
Answer: 2+3+3= 8

#87.23% 9ms
public class Solution {
    public int minSteps(int n) {
        int res = 0;
        for (int i = 2; i <= n; i++) {
            while (n % i == 0) {
                res += i;
                n /= i;
            }
        }
        return res;
    }
}

'''