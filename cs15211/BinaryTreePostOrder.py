__source__ = 'https://leetcode.com/problems/binary-tree-postorder-traversal/#/solutions'
# https://github.com/kamyu104/LeetCode/blob/master/Python/binary-tree-postorder-traversal.py
# Time:  O(n)
# Space: O(1)
# Tree
#
# Given a binary tree, return the postorder traversal of its nodes' values.
#
# For example:
# Given binary tree {1,#,2,3},
#   1
#    \
#     2
#    /
#   3
# return [3,2,1].
#
# Note: Recursive solution is trivial, could you do it iteratively?
#Topics:
# Tree Stack
# You might like:
# (M) Binary Tree Inorder Traversal
#

from collections import deque
# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

# Morris Traversal Solution
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        dummy = TreeNode(0)
        dummy.left = root
        result, cur = [] , dummy

        while cur:
            #1) no left child
            if cur.left is None:
                cur = cur.right
            else:
            #2) go the left child's right-most child
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right
            #3) no right child : node.right = cur and cur = cur.left
                if node.right == None:
                    node.right = cur
                    cur = cur.left
                else:
            #4) has right child : node.right = None and cur = cur.right
                    result += self.traceBack(cur.left, node)
                    node.right = None
                    cur =cur.right
        return result

    def traceBack(self, frm, to):
        result, cur = [], frm
        while cur != to:
            result.append(cur.val)
            cur = cur.right
        result.append(to.val)
        result.reverse()
        return result


# Time:  O(n)
# Space: O(n)
# Stack Solution
class Solution2:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        result, stack, current, last_traversed = [], [] ,root, None
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                parent = stack[-1]
                if parent.right in (None, last_traversed):
                    result.append(parent.val)
                    last_traversed = stack.pop()
                else:
                    current = parent.right
        return result

class SolutionOther(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        stack = [root]

        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        res.reverse()
        return res

class Solution3(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if not root:
            return
        self.dfs(root.left, res)
        self.dfs(root.right, res)
        res.append(root.val)

#create tree
root1=TreeNode(0)
root2=TreeNode(1)
root3=TreeNode(2)
root4=TreeNode(4)
root5=TreeNode(5)

tree2=TreeNode(2)
tree31=TreeNode(3)
tree32=TreeNode(3)
tree41=TreeNode(4)
tree411=TreeNode(4)
tree4111=TreeNode(4)
tree51=TreeNode(1)
tree52=TreeNode(2)
tree511=TreeNode(3)
tree522=TreeNode(4)
tree5221=TreeNode(5)
tree52212=TreeNode(6)

root2.left=tree2

root3.left=tree31
root3.right=tree32

root4.right =tree41
tree41.right=tree411
tree411.right=tree4111

root5.left=tree51
root5.right=tree52
tree51.left=tree511
tree52.right=tree522
tree522.left=tree5221
tree5221.right=tree52212

#my_test=SolutionOther()
#print my_test.postorderTraversal1(root2)
#print my_test.postorderTraversal3(root5)

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    result = Solution().postorderTraversal(root)
    print result
#Java
# http://www.programcreek.com/2012/12/leetcode-solution-of-iterative-binary-tree-postorder-traversal-in-java/
# The order of "Postorder" is: left child -> right child -> parent node.
# Find the relation between the previously visited node and the current node
# Use a stack to track nodes
# As we go down the tree, check the previously visited node.
# If it is the parent of the current node, we should add current node to stack.
# When there is no children for current node, pop it from stack.
# Then the previous node become to be under the current node for next loop.
java = '''
1. DFS: 51%
public class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        postorder(root, result);
        return result;
    }

    private void postorder(TreeNode root, List<Integer> result) {
        if (root == null) {
            return;
        }
        postorder(root.left, result);
        postorder(root.right, result);
        result.add(root.val);
    }
}

2. BFS 51%
public class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode cur = stack.pop();
            result.add(cur.val);
            if (cur.left != null) {
                stack.push(cur.left);
            }
            if (cur.right != null) {
                stack.push(cur.right);
            }
        }
        Collections.reverse(result);
        return result;
    }

     # PostOrder 5.82%
     public List<Integer> postorderBFS(TreeNode root) {
        LinkedList<Integer> result = new LinkedList<>();
        Deque<TreeNode> stack = new ArrayDeque<>();
        while(!stack.isEmpty() || root != null) {
            if (root != null) {
                stack.push(root);
                result.addFirst(root.val); // Reverse the process of preorder
                root = root.right; // Reverse the process of preorder
            } else {
                TreeNode node = stack.pop();
                root = node.left; // Reverse the process of preorder
            }
        }
        return result;
     }

    # In Order Traverse
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode p = root;
        while(!stack.isEmpty() || p != null) {
            if(p != null) {
                stack.push(p);
                p = p.left;
            } else {
                TreeNode node = stack.pop();
                result.add(node.val);  // Add after all left children
                p = node.right;
            }
        }
        return result;
    }

    # Pre Order Traverse
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode p = root;
        while(!stack.isEmpty() || p != null) {
            if(p != null) {
                stack.push(p);
                result.add(p.val);  // Add before going to children
                p = p.left;
            } else {
                TreeNode node = stack.pop();
                p = node.right;
            }
        }
        return result;
    }
}




'''