class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            index = inorder.index(preorder.pop(0))

            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            print(node.left)
            node.right = self.buildTree(preorder, inorder[index + 1:])
            return node