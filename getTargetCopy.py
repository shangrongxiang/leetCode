#Definition for a binary tree node.
'''Given two binary trees original and cloned and given a reference 
to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or 
the target node and the answer must be a reference to a node in the cloned tree.
Input: tree = [1,2,null,3], target = 2
Output: 2
Follow up: Solve the problem if repeated values on the tree are allowed.'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def gettargetCopy(self,original,cloned,target):
        if original == None:
            return None
        if original == target:
            return cloned
        return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)
