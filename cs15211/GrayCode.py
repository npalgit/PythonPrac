__author__ = 'July'
# Time:  O(2^n)
# Space: O(1)
#
# The gray code is a binary numeral system where two successive values differ in only one bit.
#
# Given a non-negative integer n representing the total number of bits in the code,
# print the sequence of gray code. A gray code sequence must begin with 0.
#
# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
#
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# Note:
# For a given n, a gray code sequence is not uniquely defined.
#
# For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.
#
# For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
# Amazon
#
class Solution:
    # @return a list of integers
    def grayCode(self, n):
        result = [0]
        for i in xrange(n):
            for j in reversed(result):
                result.append( 1 << i | j)
        return result

# proof of closed form formula could be found here:
# http://math.stackexchange.com/questions/425894/proof-of-closed-form-formula-to-convert-a-binary-number-to-its-gray-code
class Solution2:
    # @return a list of integers
    def grayCode(self, n):
        return [i >> 1 ^ i for i in xrange(1 << n)]


if __name__ == "__main__":
    print Solution().grayCode(0)
    print Solution().grayCode(2)

class SolutionOther:
    # @return a list of integers
    def grayCode(self, n):
        self.res = [0]
        for i in [2**x for x in range(0,n)]:
            print self.res, i
            self.res.append(self.res[-1] +i)
            #print "temp", self.res[-3:-1],self.res[-3:None:-1]
            self.res.extend([i+v for v in self.res[-3:None:-1]])
        return self.res

#test
#test=SolutionOther()
#print test.grayCode(3)
#test = [0,1,2,3,4,5,6]
#print test[-3:-1], test[-3:None:-1]
#java
js = '''
public class Solution {
    public List<Integer> grayCode(int n) {
        List<Integer> result = new ArrayList<>();
        if (n < 0) {
            return result;
        }
        result.add(0);
        for (int i = 0; i < n; i++) {
            int highBit = 1 << i;
            for (int j = result.size() - 1; j >= 0; j--) {
                result.add(result.get(j) + highBit);
            }
        }
        return result;
    }
}
'''