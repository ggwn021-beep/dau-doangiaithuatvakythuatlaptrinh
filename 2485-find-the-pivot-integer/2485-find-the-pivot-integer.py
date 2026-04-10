class Solution(object):
    def pivotInteger(self, n):
        # Tổng toàn bộ từ 1 đến n
        tong_toan_bo = n * (n + 1) // 2
        
        trai = 1
        phai = n
        
        while trai <= phai:
            x = trai + (phai - trai) // 2
            
            # Tổng từ 1 đến x
            tong_trai = x * (x + 1) // 2
            # Tổng từ x đến n (bao gồm cả x)
            tong_phai = tong_toan_bo - tong_trai + x
            
            if tong_trai == tong_phai:
                return x
            elif tong_trai < tong_phai:
                # Trọng tâm đang lệch phải, cần nhích x sang phải
                trai = x + 1
            else:
                # Trọng tâm đang lệch trái, lùi x về
                phai = x - 1
                
        return -1 # Không tìm thấy