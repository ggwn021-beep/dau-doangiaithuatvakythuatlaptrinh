class Solution(object):
    def buildTree(self, preorder, inorder):
        # Tạo bản đồ từ điển tra cứu nhanh vị trí trong mảng Inorder
        vi_tri_inorder = {gia_tri: chi_so for chi_so, gia_tri in enumerate(inorder)}
        
        # Biến đếm con trỏ đang ở đâu trong mảng Preorder
        self.pre_idx = 0 
        
        def dung_cay(trai, phai):
            # Nếu vượt quá ranh giới -> Không có phần tử nào
            if trai > phai:
                return None
                
            # Lấy Root (Gốc) hiện tại từ Preorder
            gia_tri_goc = preorder[self.pre_idx]
            goc = TreeNode(gia_tri_goc)
            self.pre_idx += 1
            
            # Tìm vị trí của cái Gốc này để chẻ ranh giới (Trái / Phải)
            vi_tri_chinh_giua = vi_tri_inorder[gia_tri_goc]
            
            # Xây dựng cành trái từ vùng ranh giới bên trái
            goc.left = dung_cay(trai, vi_tri_chinh_giua - 1)
            # Xây dựng cành phải từ vùng ranh giới bên phải
            goc.right = dung_cay(vi_tri_chinh_giua + 1, phai)
            
            return goc
            
        return dung_cay(0, len(inorder) - 1)