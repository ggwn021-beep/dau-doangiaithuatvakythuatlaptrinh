class Solution(object):
    def maxDepth(self, root):
        # Nếu không có cây (hoặc ngõ cụt), độ sâu là 0
        if not root:
            return 0
            
        # Hỏi cành bên trái xem nó sâu bao nhiêu
        do_sau_trai = self.maxDepth(root.left)
        
        # Hỏi cành bên phải xem nó sâu bao nhiêu
        do_sau_phai = self.maxDepth(root.right)
        
        # Lấy nhánh sâu hơn, CỘNG THÊM 1 (chính là bản thân Node hiện tại)
        return max(do_sau_trai, do_sau_phai) + 1