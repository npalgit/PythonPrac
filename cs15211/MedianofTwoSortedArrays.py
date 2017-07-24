__source__ = 'https://leetcode.com/problems/median-of-two-sorted-arrays/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/median-of-two-sorted-arrays.py
# Time:  O(log(m + n))
# Space: O(1)
# Binary Search
#
# Description: Leetcode # 4. Median of Two Sorted Arrays
# There are two sorted arrays A and B of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# Companies
# Google Zenefits Microsoft Apple Yahoo Dropbox Adobe
# Related Topics
# Binary Search Array Divide and Conquer
#
# using list slicing (O(k)) may be slower than solution1
import unittest
#95ms
class Solution4:
    # @return a float
    def median(A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0

# Time:  O(log(m + n))
# Space: O(log(m + n))
class Solution3:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        lenA, lenB = len(A), len(B)
        if (lenA + lenB) % 2 == 1:
            return self.getKth(A, 0, B, 0, (lenA + lenB)/ 2 + 1)
        else:
            return (self.getKth(A, 0, B, 0, (lenA + lenB) / 2) + self.getKth(A, 0, B, 0, (lenA + lenB) / 2 + 1)) * 0.5

    def getKth(self, A, i, B, j, k):
        lenA, lenB = len(A) - i, len(B) - j
        if lenA > lenB:
            return self.getKth(B, j, A, i, k)

        if lenA == 0:
            return B[j + k - 1]

        if k == 1:
            return min(A[i], B[j])
        pa = min(k/2, lenA)
        pb = k - pa

        if A[ i + pa - 1] < B[j + pb - 1]:
            return self.getKth(A, i + pa, B, j , k - pa)
        elif A[i + pa - 1] > B[j + pb - 1]:
            return self.getKth(A, i , B, j + pb, k - pb)
        else:
            return A[ i + pa - 1]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution3().findMedianSortedArrays([1, 3, 5, 7], [2, 4, 6])
        print Solution4().findMedianSortedArrays([1, 3, 5], [2, 4, 6])
        #test
        test = Solution4()
        #A = [1,1,1]
        #B = [0,0,0]
        A = [1,3,5,7]
        B = [2,4,6,8,9,10]
        #print test.findMedianSortedArrays(A, B)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/contains-duplicate/solution/
#Thought:
# https://discuss.leetcode.com/topic/4996/share-my-o-log-min-m-n-solution-with-explanation
# To solve this problem, we need to understand "What is the use of median".
# In statistics, the median is used for dividing a set into two equal length subsets,
# that one subset is always greater than the other. If we understand the use of median
# for dividing, we are very close to the answer.
#
# First let's cut A into two parts at a random position i:
#
#       left_A             |        right_A
# A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
# Since A has m elements, so there are m+1 kinds of cutting( i = 0 ~ m ).
# And we know: len(left_A) = i, len(right_A) = m - i . Note: when i = 0 ,
#  left_A is empty, and when i = m , right_A is empty.
#
# With the same way, cut B into two parts at a random position j:
#
#       left_B             |        right_B
# B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]
# Put left_A and left_B into one set, and put right_A and right_B into another set.
# Let's name them left_part and right_part :
#
#       left_part          |        right_part
# A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
# B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]
# If we can ensure:
#
# 1) len(left_part) == len(right_part)
# 2) max(left_part) <= min(right_part)
# then we divide all elements in {A, B} into two parts with equal length,
# and one part is always greater than the other. Then median = (max(left_part) + min(right_part))/2.
#
# To ensure these two conditions, we just need to ensure:
#
# (1) i + j == m - i + n - j (or: m - i + n - j + 1)
#     if n >= m, we just need to set: i = 0 ~ m, j = (m + n + 1)/2 - i
# (2) B[j-1] <= A[i] and A[i-1] <= B[j]
# ps.1 For simplicity, I presume A[i-1],B[j-1],A[i],B[j] are always valid even if i=0/i=m/j=0/j=n .
# I will talk about how to deal with these edge values at last.
#
# ps.2 Why n >= m? Because I have to make sure j is non-nagative since 0 <= i <= m and j = (m + n + 1)/2 - i.
# If n < m , then j may be nagative, that will lead to wrong result.
#
# So, all we need to do is:
#
# Searching i in [0, m], to find an object `i` that:
#     B[j-1] <= A[i] and A[i-1] <= B[j], ( where j = (m + n + 1)/2 - i )
# And we can do a binary search following steps described below:
#
# <1> Set imin = 0, imax = m, then start searching in [imin, imax]
#
# <2> Set i = (imin + imax)/2, j = (m + n + 1)/2 - i
#
# <3> Now we have len(left_part)==len(right_part). And there are only 3 situations
#      that we may encounter:
#     <a> B[j-1] <= A[i] and A[i-1] <= B[j]
#         Means we have found the object `i`, so stop searching.
#     <b> B[j-1] > A[i]
#         Means A[i] is too small. We must `ajust` i to get `B[j-1] <= A[i]`.
#         Can we `increase` i?
#             Yes. Because when i is increased, j will be decreased.
#             So B[j-1] is decreased and A[i] is increased, and `B[j-1] <= A[i]` may
#             be satisfied.
#         Can we `decrease` i?
#             `No!` Because when i is decreased, j will be increased.
#             So B[j-1] is increased and A[i] is decreased, and B[j-1] <= A[i] will
#             be never satisfied.
#         So we must `increase` i. That is, we must ajust the searching range to
#         [i+1, imax]. So, set imin = i+1, and goto <2>.
#     <c> A[i-1] > B[j]
#         Means A[i-1] is too big. And we must `decrease` i to get `A[i-1]<=B[j]`.
#         That is, we must ajust the searching range to [imin, i-1].
#         So, set imax = i-1, and goto <2>.
# When the object i is found, the median is:
#
# max(A[i-1], B[j-1]) (when m + n is odd)
# or (max(A[i-1], B[j-1]) + min(A[i], B[j]))/2 (when m + n is even)
# Now let's consider the edges values i=0,i=m,j=0,j=n where A[i-1],B[j-1],A[i],B[j] may not exist.
#  Actually this situation is easier than you think.
#
# What we need to do is ensuring that max(left_part) <= min(right_part). So, if i and j are not edges
# values(means A[i-1],B[j-1],A[i],B[j] all exist), then we must check both B[j-1] <= A[i] and A[i-1] <= B[j].
# But if some of A[i-1],B[j-1],A[i],B[j] don't exist, then we don't need to check one(or both) of these two conditions.
#  For example, if i=0, then A[i-1] doesn't exist, then we don't need to check A[i-1] <= B[j]. So, what we need to do is:
#
# Searching i in [0, m], to find an object `i` that:
#     (j == 0 or i == m or B[j-1] <= A[i]) and
#     (i == 0 or j == n or A[i-1] <= B[j])
#     where j = (m + n + 1)/2 - i
# And in a searching loop, we will encounter only three situations:
#
# <a> (j == 0 or i == m or B[j-1] <= A[i]) and
#     (i == 0 or j = n or A[i-1] <= B[j])
#     Means i is perfect, we can stop searching.
#
# <b> j > 0 and i < m and B[j - 1] > A[i]
#     Means i is too small, we must increase it.
#
# <c> i > 0 and j < n and A[i - 1] > B[j]
#     Means i is too big, we must decrease it.
# Thank @Quentin.chen , him pointed out that: i < m ==> j > 0 and i > 0 ==> j < n . Because:
#
# m <= n, i < m ==> j = (m+n+1)/2 - i > (m+n+1)/2 - m >= (2*m+1)/2 - m >= 0
# m <= n, i > 0 ==> j = (m+n+1)/2 - i < (m+n+1)/2 <= (2*n+1)/2 <= n
# So in situation <b> and <c>, we don't need to check whether j > 0 and whether j < n.


# BFS
# 75.36% 66ms
public class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int len = nums1.length + nums2.length;
        if ((len & 1) == 0) { // (1 & 1 == 1)
            return ((double) findKthNumber(nums1, nums2, (len >> 1)) + findKthNumber(nums1, nums2, (len >> 1) + 1)) / 2;
        } else {
            return findKthNumber(nums1, nums2, (len >> 1) + 1);
        }
    }

    private int findKthNumber(int[] nums1, int[] nums2, int k) {
        int left1 = 0;
        int right1 = nums1.length;
        int left2 = 0;
        int right2 = nums2.length;
        while (k > 0) {
            if (right1 - left1 > right2 - left2) {
                int[] arr = nums1;
                nums1 = nums2;
                nums2 = arr;
                int tmp = left1;
                left1 = left2;
                left2 = tmp;
                tmp = right1;
                right1 = right2;
                right2 = tmp;
                continue;
            } else if (left1 == right1) {
                return nums2[left2 + k - 1];
            } else if (k == 1) {
                return Math.min(nums1[left1], nums2[left2]);
            }
            int mid1 = Math.min(k >> 1, right1 - left1);
            int mid2 = k - mid1;
            if (nums1[left1 + mid1 - 1] < nums2[left2 + mid2 - 1]) {
                left1 += mid1;
                k -= mid1;
            } else if (nums1[left1 + mid1 - 1] > nums2[left2 + mid2 - 1]) {
                left2 += mid2;
                k -= mid2;
            } else {
                return nums1[left1 + mid1 - 1];
            }
        }
        return 0;
    }
}

# DFS
# 75.36% 66ms

public class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int len1 = nums1.length;
        int len2 = nums2.length;
        if (((len1 + len2) & 1) == 0) {
            return ((double) findKthNumber(nums1, nums2, (len1 + len2) >>> 1
                + findKthNumber(nums1, nums2, ((len1 + len2) >>> 1) + 1)) / 2;
        } else {
            return findKthNumber(nums1, nums2, ((len1 + len2) >>> 1) + 1);
        }
    }

    private int findKthNumber(int[] nums1, int[] nums2, int k) {
        return findKthNumber(nums1, nums2, 0, nums1.length, 0, nums2.length, k);
    }

    private int findKthNumber(int[] nums1, int[] nums2, int start1, int end1, int start2, int end2, int k) {
        if (end1 - start1 > end2 - start2) {
            return findKthNumber(nums2, nums1, start2, end2, start1, end1, k);
        }
        if (start1 == end1) {
            return nums2[start2 + k - 1];
        }
        if (k == 1) {
            return Math.min(nums1[start1], nums2[start2]);
        }
        int mid1 = Math.min(k / 2, end1 - start1);
        int mid2 = k - mid1;
        if (nums1[start1 + mid1 - 1] < nums2[start2 + mid2 - 1]) {
            return findKthNumber(nums1, nums2, start1 + mid1, end1, start2, end2, k - mid1);
        } else if (nums1[start1 + mid1 - 1] > nums2[start2 + mid2 - 1]) {
            return findKthNumber(nums1, nums2, start1, end1, start2 + mid2, end2, k - mid2);
        } else {
            return nums1[start1 + mid1 - 1];
        }
    }
}

#99.70% 57ms
public class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int m = nums2.length;
        if (n > m)
            return findMedianSortedArrays(nums2, nums1);
        int k = (n + m - 1) / 2;
        int l = 0, r = Math.min(k, n);
        while (l < r)
        {
            int mid1 = (l + r) / 2;
            int mid2 = k - mid1;
            if (nums1[mid1] < nums2[mid2])
                l = mid1 + 1;
            else
                r = mid1;
        }
        int a = Math.max(l > 0 ? nums1[l - 1] : Integer.MIN_VALUE, k - l >= 0 ? nums2[k - l] : Integer.MIN_VALUE);
        if (((n + m) & 1) == 1)
        return (double) a;
        int b = Math.min(l < n ? nums1[l] : Integer.MAX_VALUE, k - l + 1 < m ? nums2[k - l + 1] : Integer.MAX_VALUE);
        return (a + b) / 2.0;
    }
}


# 75.36% 66ms
public class Solution {
    public int data[];
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        data = new int[nums1.length+nums2.length];
        // merge sort
        int i=0,j=0;
        while(i<nums1.length || j<nums2.length){
            if(i>=nums1.length){
                data[i+j] = nums2[j];
                j++;
                continue;
            }else if(j>=nums2.length){
                data[i+j] = nums1[i];
                i++;
                continue;
            }
            if(nums1[i]>=nums2[j]){
                data[i+j] = nums2[j];
                j++;
            }else{
                data[i+j] = nums1[i];
                i++;
            }
        }
        if(data.length%2==1) return data[data.length/2];
        else{
          return (data[data.length/2]+data[data.length/2-1])/2.0;
        }
    }
}
'''