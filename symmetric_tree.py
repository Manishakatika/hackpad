
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(left, right):
            if not left and not right:
                return True 
            if not left or not right:
                return False 
            left_sub = helper(left.left, right.right)
            right_sub = helper(left.right, right.left)
            return left.val == right.val and left_sub and right_sub 
        return helper(root.left, root.right)
