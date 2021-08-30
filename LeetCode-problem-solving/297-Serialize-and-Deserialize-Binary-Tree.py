import collections
class Codec:
    def serialize(self, root) -> str:
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        queue = collections.deque([root])
        result = ['#']

        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if data == '# #':
            return None

        nodes = data.split()
        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2

        while queue:
            node = queue.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root