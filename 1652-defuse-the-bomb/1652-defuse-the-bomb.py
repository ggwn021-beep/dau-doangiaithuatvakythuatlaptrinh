class Solution(object):
    def decrypt(self, code, k):
        n = len(code)
        ket_qua = [0] * n
        if k == 0: return ket_qua
        
        # Xác định khung cửa sổ trượt ban đầu
        # Nếu k > 0: Khung nằm từ ô số 1 đến ô số k
        # Nếu k < 0: Khung nằm từ ô (n - |k|) đến ô (n - 1)
        bat_dau = 1 if k > 0 else n - abs(k)
        ket_thuc = k if k > 0 else n - 1
        
        # Tính tổng của khung đầu tiên
        tong_khung = sum(code[i % n] for i in range(bat_dau, ket_thuc + 1))
        
        # Bắt đầu trượt khung đi từng bước quanh mảng
        for i in range(n):
            ket_qua[i] = tong_khung
            
            # Khung trượt đi 1 ô: Trừ đi người đứng chót, cộng thêm người đứng đầu mới
            tong_khung -= code[bat_dau % n]
            tong_khung += code[(ket_thuc + 1) % n]
            
            # Cập nhật tọa độ khung
            bat_dau += 1
            ket_thuc += 1
            
        return ket_qua