class Solution(object):
    def __init__(self):
        self.gia_tri_hien_tai = None
        self.dem_hien_tai = 0
        self.ky_luc = 0
        self.ket_qua = []

    def findMode(self, root):
        def duyet_inorder(node):
            if not node: return
            
            # 1. Đi sang trái
            duyet_inorder(node.left)
            
            # 2. Xử lý phần tử hiện tại
            if node.val == self.gia_tri_hien_tai:
                self.dem_hien_tai += 1
            else:
                self.gia_tri_hien_tai = node.val
                self.dem_hien_tai = 1
                
            # Cập nhật kỷ lục
            if self.dem_hien_tai > self.ky_luc:
                self.ky_luc = self.dem_hien_tai
                self.ket_qua = [node.val] # Xóa kết quả cũ, lập mảng mới
            elif self.dem_hien_tai == self.ky_luc:
                self.ket_qua.append(node.val) # Ngang bằng kỷ lục thì cho đứng chung
                
            # 3. Đi sang phải
            duyet_inorder(node.right)
            
        duyet_inorder(root)
        return self.ket_qua