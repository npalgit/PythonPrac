__source__ = 'https://leetcode.com/problems/inorder-successor-in-bst/#/description'
# Time:  O(h)
# Space: O(1)
#
# Description:
#
# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
#
# Note: If the given node has no in-order successor in the tree, return null.
#
# Hide Company Tags Pocket Gems Microsoft Facebook
# Hide Tags Tree
# Hide Similar Problems (M) Binary Tree Inorder Traversal (M) Binary Search Tree Iterator
#

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ

    def inorderSuccessor2(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        # If it has right subtree.
        if p and p.right:
            p = p.right
            while p.left:
                p = p.left
            return p

        # Search from root.
        successor = None
        while root and root != p:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right

        return successor

#java
java = '''
Thought:
The idea is to compare root's value with p's value if root is not null, and consider the following two cases:

root.val > p.val. In this case, root can be a possible answer, so we store the root node first and call it res.
However, we don't know if there is anymore node on root's left that is larger than p.val.
So we move root to its left and check again.

root.val <= p.val. In this case, root cannot be p's inorder successor, neither can root's left child.
So we only need to consider root's right child, thus we move root to its right and check again.

We continuously move root until exhausted. To this point, we only need to return the res in case 1.


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

Successor
public class Solution {
     public TreeNode inorderSuccessorBFS(TreeNode root, TreeNode p) {
        TreeNode res = null;
        while (root != null) {
            if (root.val > p.val) {
                res = root;
                root = root.left;
            }else {
                root = root.right;
            }
        }
        return res;
     }
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        if (root == null) return null;
        if (root.val <= p.val) {
            return inorderSuccessor(root.right, p);
        } else {
            TreeNode left = inorderSuccessor(root.left, p);
            return left != null?left: root;
        }
    }
}

Predecessor

public TreeNode predecessor(TreeNode root, TreeNode p) {
  if (root == null)
    return null;

  if (root.val >= p.val) {
    return predecessor(root.left, p);
  } else {
    TreeNode right = predecessor(root.right, p);
    return (right != null) ? right : root;
  }
}
'''