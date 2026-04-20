# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        # 1. Nếu cả 2 đều rỗng -> Giống nhau
        if not p and not q:
            return True
        # 2. Nếu 1 bên có 1 bên không, HOẶC giá trị khác nhau -> Sai
        if not p or not q or p.val != q.val:
            return False
            
        # 3. Tiếp tục so sánh đồng thời cành bên trái và cành bên phải
        ben_trai_giong = self.isSameTree(p.left, q.left)
        ben_phai_giong = self.isSameTree(p.right, q.right)
        
        return ben_trai_giong and ben_phai_giong