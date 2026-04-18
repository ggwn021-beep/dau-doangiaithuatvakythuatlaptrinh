class Solution(object):
    def invertTree(self, root):
        # Nếu cây rỗng hoặc đã đi đến tận cùng -> Dừng lại
        if not root:
            return None
            
        # 1. Tráo đổi trực tiếp 2 cành trái và phải của Node hiện tại
        root.left, root.right = root.right, root.left
        
        # 2. Ra lệnh cho cành trái và cành phải cũng tự tráo đổi các con của chúng
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root