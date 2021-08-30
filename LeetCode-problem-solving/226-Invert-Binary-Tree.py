import collections
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)
        return root