class Solution(object):
    def findNumbers(self, nums):
        so_luong_thoa_man = 0
        
        for so in nums:
            so_chu_so = 0
            so_tam = so
            
            # Đếm số lượng chữ số bằng cách chia cho 10
            while so_tam > 0:
                so_tam = so_tam // 10  # Cắt bỏ đi 1 chữ số ở đuôi
                so_chu_so += 1
                
            # Kiểm tra xem số lượng chữ số có phải là chẵn không
            if so_chu_so % 2 == 0:
                so_luong_thoa_man += 1
                
        return so_luong_thoa_man