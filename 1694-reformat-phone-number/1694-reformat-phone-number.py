class Solution(object):
    def reformatNumber(self, number):
        # Bước 1: Dọn dẹp số điện thoại
        so_sach = number.replace(" ", "").replace("-", "")
        
        ket_qua = []
        i = 0
        
        # Bước 2: Cắt từng khúc
        # Chạy vòng lặp cho đến khi số lượng chữ số còn lại <= 4
        while len(so_sach) - i > 4:
            # Lấy 3 chữ số bỏ vào mảng
            ket_qua.append(so_sach[i : i+3])
            i += 3
            
        # Bước 3: Xử lý đoạn đuôi còn sót lại (chỉ có thể là 2, 3 hoặc 4 số)
        phan_du = so_sach[i:]
        
        if len(phan_du) == 4:
            # Nếu dư 4 số thì bẻ đôi
            ket_qua.append(phan_du[0:2])
            ket_qua.append(phan_du[2:4])
        else:
            # Nếu dư 2 hoặc 3 số thì bỏ nguyên vào
            ket_qua.append(phan_du)
            
        # Nối các nhóm lại bằng dấu gạch ngang
        return "-".join(ket_qua)