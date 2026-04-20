class Solution(object):
    def leafSimilar(self, root1, root2):
        
        # Hàm đệ quy thu thập lá của một cây
        def thu_thap_la(node, danh_sach_la):
            if not node:
                return
                
            # Nếu là Node lá (không có cành con) -> Ghi sổ
            if not node.left and not node.right:
                danh_sach_la.append(node.val)
                
            # Tiếp tục quét từ trái sang phải
            thu_thap_la(node.left, danh_sach_la)
            thu_thap_la(node.right, danh_sach_la)
            
        la_cay_1 = []
        thu_thap_la(root1, la_cay_1)
        
        la_cay_2 = []
        thu_thap_la(root2, la_cay_2)
        
        # so sánh nội dung 2 mảng
        return la_cay_1 == la_cay_2