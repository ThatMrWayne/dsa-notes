# 94
# TC : O(n)
# SC : O(n)



def inorderTraversal(root):
        record = []
        def dfs_inorder(node, record):
            if node is None:
                return

            if node.left:
                dfs_inorder(node.left, record)
            record.append(node.val)
            if node.right:
                dfs_inorder(node.right,record)

            return

        dfs_inorder(root, record)
        return record
