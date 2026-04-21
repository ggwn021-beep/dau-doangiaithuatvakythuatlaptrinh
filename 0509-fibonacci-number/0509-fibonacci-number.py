class Solution(object):
    def fib(self, n):
        if n == 0: return 0
        if n == 1: return 1
        
        # Chỉ dùng 2 biến để nhớ 2 số liền trước
        a = 0 # F(0)
        b = 1 # F(1)
        
        # Bắt đầu cộng đuổi từ tháng thứ 2 cho đến n
        for _ in range(2, n + 1):
            so_moi = a + b
            a = b       # Số thứ 2 lùi xuống thành số thứ 1
            b = so_moi  # Số mới lùi xuống thành số thứ 2
            
        return b