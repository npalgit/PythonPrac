__source__ = 'https://leetcode.com/problems/binary-tree-maximum-path-sum/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/binary-tree-maximum-path-sum.py
# Time:  O(n)
# Space: O(h), h is height of binary tree
# Divide and Conquer
#
# Given a binary tree, find the maximum path sum.
#
# The path may start and end at any node in the tree.
#
# For example:
# Given the below binary tree,
#
#        1
#       / \
#      2   3
# Return 6.
#
#
# Topics:
# Tree Depth-first Search
# You might like:
# (E) Path Sum (M) Sum Root to Leaf Numbers
# Company:
# Microsoft Baidu



# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    maxSum = float("-inf")
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        self.maxPathSumRecu(root)
        return self.maxSum

    def maxPathSumRecu(self, root):
        if root is None:
            return 0
        left = max(0, self.maxPathSumRecu(root.left))
        right = max(0, self.maxPathSumRecu(root.right))
        self.maxSum = max(self.maxSum, root.val + left + right)
        return root.val + max( left, right)


class SolutionOther:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        Solution.max = -10000000
        if root == None:
            return 0
        self.maxsum(root)
        return Solution.max

    def maxsum(self, root):
        if root == None:
            return 0
        sum = root.val
        lmax = 0 ; rmax = 0
        if root.left:
            lmax = self.maxsum(root.left)
            if lmax > 0:
                sum += lmax
        if root.right:
            rmax = self.maxsum(root.right)
            if rmax > 0:
                sum += rmax
        if sum > Solution.max:
            Solution.max = sum

        return max(root.val, max(root.val+lmax, root.val+rmax))

#test

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    result = Solution().maxPathSum(root)
    print result

# http://www.programcreek.com/2013/02/leetcode-binary-tree-maximum-path-sum-java/
# Analysis
# 1) Recursively solve this problem
# 2) Get largest left sum and right sum
# 3) Compare to the stored maximum
#java
java = '''
Thought: Here's my ideas:
A path from start to end, goes up on the tree for 0 or more steps,
then goes down for 0 or more steps. Once it goes down, it can't go up.
Each path has a highest node, which is also the lowest common ancestor of all other nodes on the path.
A recursive method maxPathDown(TreeNode node)
(1) computes the maximum path sum with highest node is the input node, update maximum if necessary
(2) returns the maximum sum of the path that can be extended to input node's parent.

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int maxPathSum(TreeNode root) {
        int[] res = new int[1];
        res[0] = Integer.MIN_VALUE;
        maxPathSum(root, res);
        return res[0];
    }
    private int maxPathSum(TreeNode root, int[] res){
        if( root == null) return 0;
        int leftMax = Math.max(0, maxPathSum(root.left, res));
        int rightMax = Math.max(0, maxPathSum(root.right, res));
        res[0] = Math.max(res[0], root.val + leftMax + rightMax);
        return root.val + Math.max(leftMax, rightMax);
    }
}

#with global var
public class Solution {
   int maxValue;

    public int maxPathSum(TreeNode root) {
        maxValue = Integer.MIN_VALUE;
        maxPathDown(root);
        return maxValue;
    }

    public int maxPathDown(TreeNode root) {
        if (root == null) return 0;
        int left = Math.max(maxPathDown(root.left), 0 );
        int right = Math.max(maxPathDown(root.right), 0);
        maxValue = Math.max(maxValue, left + right + root.val);
        return Math.max(left, right) + root.val;
    }
}
'''