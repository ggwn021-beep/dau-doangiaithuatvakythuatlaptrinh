class Solution(object):
    def checkValid(self, matrix):
        n = len(matrix)
        
        # 1. Kiểm tra từng hàng ngang
        for i in range(n):
            tap_hop_hang = set(matrix[i])
            if len(tap_hop_hang) != n:
                return False
                
        # 2. Kiểm tra từng cột dọc
        for j in range(n):
            tap_hop_cot = set()
            for i in range(n):
                tap_hop_cot.add(matrix[i][j])
            
            if len(tap_hop_cot) != n:
                return False
                
        return True