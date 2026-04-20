class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
            
        tong = 0
        
        # Kiểm tra xem cành TRÁI có tồn tại và CÓ PHẢI LÀ LÁ không
        if root.left and not root.left.left and not root.left.right:
            tong += root.left.val
        else:
            # Nếu không phải lá, tiếp tục đi sâu xuống cành trái tìm kiếm
            tong += self.sumOfLeftLeaves(root.left)
            
        # Dù thế nào cũng phải đi kiểm tra cành phải (vì cành phải có thể chứa lá trái ở bên dưới nó)
        tong += self.sumOfLeftLeaves(root.right)
        
        return tong