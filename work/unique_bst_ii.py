# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        def generate_trees(start, end):
            if start > end:
                return [None]
            trees = []
            for val in range(start, end+1):
                left_trees = generate_trees(start, val-1)
                right_trees = generate_trees(val + 1, end)
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        root = TreeNode(val)
                        root.left = left_tree
                        root.right = right_tree
                        trees.append(root)
            return trees
        return generate_trees(1, n)
