__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/single-number.py
# Time:  O(n)
# Space: O(1)
# Bit Manipulation
# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#

import operator

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        return reduce(operator.xor, A)

if __name__ == '__main__':
    print Solution().singleNumber([1, 1, 2, 2, 3])

class SolutionOther:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        # self XOR self == 0, 0 XOR self == self
        answer = 0
        for num in A:
            answer ^= num
        return answer

    def singleNumber2(self, A):
        # self XOR self == 0, 0 XOR self == self
        answer = 0
        sum = 0
        for num in A:
            answer ^= num
            sum += num
        return (3*answer - sum )/2

    def genericSingleNumber(self, A, reptime):
        res = 0
        count = 0
        negative = 0

        for i in range(32):
            count = 0
            for j in range(len(A)):
                if A[j] < 0 :
                    temp = ~A[j] + 1
                    negative += 1
                else:
                    temp = A[j]
                count += (temp >> i) & 1

            res = res | ((count % reptime) << i)
            #print res , count

        if ((negative /32) % reptime ) * -1  != 0 :
            res *= -1
        return res




# test case
my_test = SolutionOther()
#print my_test.singleNumber([2,2,4,5,4])
#print my_test.singleNumber([-2,-2,4,5,4])

#print my_test.singleNumber2([2,2,2,4,4,5,4])
#print my_test.singleNumber2([-2,-2,-2,4,5,4, 4])

print my_test.genericSingleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2],3)
#print my_test.genericSingleNumber([2,2,2,4,4,5,4], 3)
#print my_test.genericSingleNumber([-1,-5,-5], 2)
#print my_test.genericSingleNumber([-5,-5, -5, 1], 3)
#print my_test.genericSingleNumber([1,5,5], 2)
#print my_test.genericSingleNumber([1], 2)

#java
js = '''
public class Solution {
    public int singleNumber(int[] nums) {
        int cur = 0;
        for (int num : nums) {
            cur ^= num;
        }
        return cur;
    }
}
'''