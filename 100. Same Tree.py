# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SameTree(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        pstack = []
        qstack = []
        pstack.append(p)
        qstack.append(q)
        while len(pstack) != 0 and len(qstack) != 0:
            t1 = pstack.pop()
            t2 = qstack.pop()
            if t1 == None and t2 == None:
                continue
            if (t1 == None and t2 != None) or (t1 != None and t2 == None) or t1.val != t2.val:
                return False
            if t1.left != None:
                pstack.append(t1.left)
            if t2.left != None:
                qstack.append(t2.left)
            if len(qstack) != len(pstack):
                return False
            if t1.right != None:
                pstack.append(t1.right)
            if t2.right != None:
                qstack.append(t2.right)
            if len(qstack) != len(pstack):
                return False

        if len(pstack) != 0 or len(qstack) != 0:
            return False
        return True


