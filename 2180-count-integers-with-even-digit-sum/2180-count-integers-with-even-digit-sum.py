class Solution(object):
    def countEven(self, num):
        tong_chu_so = 0
        tam = num
        while tam > 0:
            tong_chu_so += tam % 10
            tam //= 10
            
        # Nếu tổng chữ số là chẵn, kết quả luôn là num // 2
        # Nếu tổng chữ số là lẻ, kết quả là (num - 1) // 2
        if tong_chu_so % 2 == 0:
            return num // 2
        else:
            return (num - 1) // 2