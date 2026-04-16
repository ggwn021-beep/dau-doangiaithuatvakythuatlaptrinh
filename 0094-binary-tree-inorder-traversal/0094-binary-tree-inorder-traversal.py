# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        ket_qua = []
        
        def duyet_cay(node):
            if not node:
                return
            
            # 1. Đi tận cùng sang TRÁI
            duyet_cay(node.left)
            # 2. Xử lý phần tử ở GIỮA
            ket_qua.append(node.val)
            # 3. Đi sang PHẢI
            duyet_cay(node.right)
            
        duyet_cay(root)
        return ket_qua