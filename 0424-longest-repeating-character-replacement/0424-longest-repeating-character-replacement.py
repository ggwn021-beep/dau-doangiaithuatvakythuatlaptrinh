class Solution(object):
    def characterReplacement(self, s, k):
        dem_chu = {}
        trai = 0
        ky_luc = 0
        so_luong_chu_nhieu_nhat = 0
        
        for phai in range(len(s)):
            chu_hien_tai = s[phai]
            # Tăng biến đếm cho chữ cái hiện tại
            dem_chu[chu_hien_tai] = dem_chu.get(chu_hien_tai, 0) + 1
            
            # Cập nhật số lượng của chữ cái thuộc "phe đông nhất"
            so_luong_chu_nhieu_nhat = max(so_luong_chu_nhieu_nhat, dem_chu[chu_hien_tai])
            
            # Kích thước khung hiện tại: phai - trai + 1
            # Số chữ "cần thay thế" = Kích thước khung - phe đông nhất
            # Nếu không đủ đũa phép k -> Đẩy mép trái lên để duy trì khung hợp lệ
            if (phai - trai + 1) - so_luong_chu_nhieu_nhat > k:
                chu_ben_trai = s[trai]
                dem_chu[chu_ben_trai] -= 1
                trai += 1
                
            # Cập nhật kỷ lục độ dài cửa sổ
            ky_luc = max(ky_luc, phai - trai + 1)
            
        return ky_luc