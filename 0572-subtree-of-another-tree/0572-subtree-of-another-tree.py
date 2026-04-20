class Solution(object):
    def isSubtree(self, root, subRoot):
        # Nếu cây nhỏ rỗng -> Luôn là cây con của mọi cây
        if not subRoot: return True
        # Nếu cây to rỗng mà cây nhỏ có -> Không thể nào
        if not root: return False
        
        # Nếu 2 cây hiện tại giống hệt nhau -> Trúng mánh!
        if self.isSameTree(root, subRoot):
            return True
            
        # Nếu không giống, tiếp tục chia ra tìm ở bên trái HOẶC bên phải cây to
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # Copy lại nguyên hàm isSameTree ở bài 120 làm "vũ khí phụ"
    def isSameTree(self, p, q):
        if not p and not q: return True
        if not p or not q or p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)