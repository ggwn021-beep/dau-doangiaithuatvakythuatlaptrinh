class Solution(object):
    def sumZero(self, n):
        ket_qua = []
        
        # Tìm số lượng cặp cần tạo (n chia nguyên cho 2)
        so_cap = n // 2
        
        for i in range(1, so_cap + 1):
            ket_qua.append(i)   # Nhét số dương
            ket_qua.append(-i)  # Nhét số âm đối nghịch
            
        # Nếu n là số lẻ, nhét thêm số 0 vào mảng
        if n % 2 != 0:
            ket_qua.append(0)
            
        return ket_qua