#https://leetcode.com/problems/boundary-of-binary-tree/#/solutions
#Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root.
# Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.
#
# Left boundary is defined as the path from root to the left-most node.
# Right boundary is defined as the path from root to the right-most node.
# If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary.
# Note this definition only applies to the input binary tree, and not applies to any subtrees.
#
# The left-most node is defined as a leaf node you could reach when you always firstly travel
# to the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.
#
# The right-most node is also defined by the same way with left and right exchanged.
#
# Example 1
# Input:
#   1
#    \
#     2
#    / \
#   3   4
#
# Ouput:
# [1, 3, 4, 2]
#
# Explanation:
# The root doesn't have left subtree, so the root itself is left boundary.
# The leaves are node 3 and 4.
# The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
# So order them in anti-clockwise without duplicates and we have [1,3,4,2].
# Example 2
# Input:
#     ____1_____
#     /          \
#   2            3
#  / \          /
# 4   5        6
#    / \      / \
#   7   8    9  10
#
# Ouput:
# [1,2,4,7,8,9,10,6,3]
#
# Explanation:
# The left boundary are node 1,2,4. (4 is the left-most node according to definition)
# The leaves are node 4,7,8,9,10.
# The right boundary are node 1,3,6,10. (10 is the right-most node).
# So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].
# Hide Company Tags Amazon Google
# Hide Tags Tree
# Hide Similar Problems (M) Binary Tree Right Side View
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs_leftmost(node):
            if not node or not node.left and not node.right:
                return
            boundary.append(node.val)
            if node.left:
                dfs_leftmost(node.left)
            else:
                dfs_leftmost(node.right)

        def dfs_leaves(node):
            if not node:
                return
            dfs_leaves(node.left)
            if node != root and not node.left and not node.right:
                boundary.append(node.val)
            dfs_leaves(node.right)

        def dfs_rightmost(node):
            if not node or not node.left and not node.right:
                return
            if node.right:
                dfs_rightmost(node.right)
            else:
                dfs_rightmost(node.left)
            boundary.append(node.val)

        if not root:
            return []
        boundary = [root.val]
        dfs_leftmost(root.left)
        dfs_leaves(root)
        dfs_rightmost(root.right)
        return boundary

Java = '''
1. Java Preorder Single Pass O(n) Solution
We perform a single preorder traversal of the tree, keeping tracking of the left boundary and middle leaf nodes and
the right boundary nodes in the process. A single flag is used to designate the type of node during the preorder traversal.
Its values are:
0 - root, 1 - left boundary node, 2 - right boundary node, 3 - middle node.

public List<Integer> boundaryOfBinaryTree(TreeNode root) {
    List<Integer> left = new LinkedList<>(), right = new LinkedList<>();
    preorder(root, left, right, 0);
    left.addAll(right);
    return left;
}

public void preorder(TreeNode cur, List<Integer> left, List<Integer> right, int flag) {
    if (cur == null) return;
    if (flag == 2) right.add(0, cur.val);
    else if (flag <= 1 || cur.left == null && cur.right == null) left.add(cur.val);
    preorder(cur.left, left, right, flag <= 1 ? 1 : (flag == 2 && cur.right == null) ? 2 : 3);
    preorder(cur.right, left, right, flag % 2 == 0 ? 2 : (flag == 1 && cur.left == null) ? 1 : 3);
}


2. Same w/ enum
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
    public enum Flag{
        ROOT(0),
        LB_NODE(1),
        RB_NODE(2),
        MID_NODE(3);
        private int idx;
        Flag(int idx){
            this.idx = idx;
        }

        public int getIdx() {
            return idx;
        }
    }

    public List<Integer> boundaryOfBinaryTree(TreeNode root) {
        List<Integer> left = new LinkedList<>(), right = new LinkedList<>();
        preOrder(root, left, right, Flag.ROOT);
        left.addAll(right);
        return left;
    }

    public void preOrder(TreeNode cur, List<Integer> left, List<Integer> right, Flag f) {
        if (cur == null) return;
        if (f.getIdx() == 2) {
            right.add(0, cur.val);
        } else if (f.getIdx() <= 1 || cur.left == null && cur.right == null) {
            left.add(cur.val);
        }
        preOrder(cur.left, left, right,
        f.getIdx() <= 1 ? Flag.LB_NODE : (f.getIdx() == 2 && cur.right == null) ? Flag.RB_NODE : Flag.MID_NODE);
        preOrder(cur.right, left, right,
        f.getIdx() % 2 == 0 ? Flag.RB_NODE : (f.getIdx() == 1 && cur.left == null) ? Flag.LB_NODE : Flag.MID_NODE);
    }
}

3. Java(12ms) - left boundary, left leaves, right leaves, right boundary
List<Integer> nodes = new ArrayList<>(1000);
public List<Integer> boundaryOfBinaryTree(TreeNode root) {

    if(root == null) return nodes;

    nodes.add(root.val);
    leftBoundary(root.left);
    leaves(root.left);
    leaves(root.right);
    rightBoundary(root.right);

    return nodes;
}
public void leftBoundary(TreeNode root) {
    if(root == null || (root.left == null && root.right == null)) return;
    nodes.add(root.val);
    if(root.left == null) leftBoundary(root.right);
    else leftBoundary(root.left);
}
public void rightBoundary(TreeNode root) {
    if(root == null || (root.right == null && root.left == null)) return;
    if(root.right == null)rightBoundary(root.left);
    else rightBoundary(root.right);
    nodes.add(root.val); // add after child visit(reverse)
}
public void leaves(TreeNode root) {
    if(root == null) return;
    if(root.left == null && root.right == null) {
        nodes.add(root.val);
        return;
    }
    leaves(root.left);
    leaves(root.right);
}
'''