# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue=[root]
        res=[]
        level=0

        while queue:
            levelnodes=[]
            
            for i in range(len(queue)):
                node=queue.pop(0)
                levelnodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level%2==1:
                levelnodes.reverse()
            res.append(levelnodes)
            
            level+=1
        
        return res
