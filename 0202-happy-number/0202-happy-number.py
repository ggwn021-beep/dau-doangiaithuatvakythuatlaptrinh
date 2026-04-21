class Solution(object):
    def isHappy(self, n):
        so_da_thay = set()
        
        while n != 1 and n not in so_da_thay:
            # Lưu lại con số này để sau này nếu gặp lại thì biết là bị kẹt
            so_da_thay.add(n)
            
            # Tính tổng bình phương các chữ số 
            tong_binh_phuong = 0
            for chu_so in str(n):
                tong_binh_phuong += int(chu_so) ** 2
            
            # Cập nhật n bằng tổng mới
            n = tong_binh_phuong
            
        return n == 1