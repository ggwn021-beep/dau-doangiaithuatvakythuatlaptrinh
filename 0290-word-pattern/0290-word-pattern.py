class Solution(object):
    def wordPattern(self, pattern, s):
        danh_sach_tu = s.split() # Cắt câu thành từng từ rời nhau
        
        # Nếu số lượng thẻ và số lượng hình không bằng nhau -> Chắc chắn sai
        if len(pattern) != len(danh_sach_tu):
            return False
            
        anh_xa_chu_sang_tu = {}
        anh_xa_tu_sang_chu = {}
        
        for i in range(len(pattern)):
            chu = pattern[i]
            tu = danh_sach_tu[i]
            
            # Kiểm tra chiều xuôi: Chữ này đã gán cho từ nào chưa
            if chu in anh_xa_chu_sang_tu:
                if anh_xa_chu_sang_tu[chu] != tu: 
                    return False # Bị gán cho từ khác rồi -> Sai
            else:
                anh_xa_chu_sang_tu[chu] = tu
                
            # Kiểm tra chiều ngược: Từ này đã bị chữ nào khác chiếm chưa
            if tu in anh_xa_tu_sang_chu:
                if anh_xa_tu_sang_chu[tu] != chu: 
                    return False
            else:
                anh_xa_tu_sang_chu[tu] = chu
                
        return True