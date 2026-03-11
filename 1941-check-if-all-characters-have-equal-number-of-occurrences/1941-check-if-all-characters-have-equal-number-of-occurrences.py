class Solution(object):
    def areOccurrencesEqual(self, s):
        so_tay_dem = {}
        
        # 1. Đếm số lượng từng chữ cái
        for chu in s:
            if chu in so_tay_dem:
                so_tay_dem[chu] += 1
            else:
                so_tay_dem[chu] = 1
                
        # 2. Lấy số lượng của một chữ cái bất kỳ làm tiêu chuẩn
        mau_chuan = so_tay_dem[s[0]]
        
        # 3. Đi kiểm tra xem có ai khác với mẫu không
        for so_luong in so_tay_dem.values():
            if so_luong != mau_chuan:
                return False # Bắt quả tang nhé=))
                
        return True