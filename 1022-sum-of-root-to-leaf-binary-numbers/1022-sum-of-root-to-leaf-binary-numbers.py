class Solution(object):
    def sumRootToLeaf(self, root):
        def dfs(node, current):
            if not node:
                return 0
            
            # build binary number
            current = current * 2 + node.val
            
            # if leaf node → return value
            if not node.left and not node.right:
                return current
            
            # sum from left and right
            return dfs(node.left, current) + dfs(node.right, current)
        
        return dfs(root, 0)