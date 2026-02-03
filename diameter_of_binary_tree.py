
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, diameter = self.height(root)
        return diameter

    def height(self, node: Optional[TreeNode]) -> tuple[int, int]:
        if not node:
            return 0, 0

        lh, ld = self.height(node.left)
        rh, rd = self.height(node.right)

        height = 1 + max(lh, rh)
        diameter = max(ld, rd, lh + rh)

        return height, diameter
