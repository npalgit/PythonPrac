__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/number-of-digit-one.py
# Time:  O(logn)
# Space: O(1)
#
# Given an integer n, count the total number of digit 1 appearing
# in all non-negative integers less than or equal to n.
#
# For example:
# Given n = 13,
# Return 6, because digit 1 occurred in the following numbers:
#  1, 10, 11, 12, 13.
#

class Solution:
    # @param {integer} n
    # @return {integer}
    def countDigitOne(self, n):
        k = 1
        cnt, multiplier, left_part = 0, 1, n

        while left_part > 0:
            # split number into: left_part, curr, right_part
            curr = left_part % 10
            right_part = n % multiplier

            # count of (c000 ~ oooc000) = (ooo + (k < curr)? 1 : 0) * 1000
            cnt += (left_part / 10 + ( k < curr)) * multiplier

            # if k == 0, oooc000 = (ooo - 1) * 1000
            if k == 0 and multiplier > 1:
                cnt -= multiplier

            # count of (oook000 ~ oookxxx): count += xxx + 1
            if curr == k:
                cnt += right_part + 1

            left_part /= 10
            multiplier *= 10

        return cnt


# java
js = '''
public class Solution {
    public int countDigitOne(int n) {
        long num = n;
        long base = 1;
        int result = 0;
        while (num >= base) {
            long left = num / base;
            long right = num % base;
            if (left % 10 > 1) {
                result += (left / 10 + 1) * base;
            } else if (left % 10 == 1) {
                result += left / 10 * base + right + 1;
            } else {
                result += left / 10 * base;
            }
            base *= 10;
        }
        return result;
    }
}


'''