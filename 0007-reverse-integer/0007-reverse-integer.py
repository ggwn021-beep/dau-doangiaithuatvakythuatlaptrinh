class Solution(object):
    def reverse(self, x):
        # 1. Đặt mốc giới hạn 32-bit của máy tính
        GIOI_HAN_TREN = 2**31 - 1
        GIOI_HAN_DUOI = -2**31
        
        # 2. Lấy giá trị tuyệt đối, biến thành chuỗi, lật ngược chuỗi [::-1], rồi ép về số lại
        so_dao_nguoc = int(str(abs(x))[::-1])
        
        # 3. Trả lại dấu trừ (nếu số gốc là số âm)
        if x < 0:
            so_dao_nguoc = -so_dao_nguoc
            
        # 4. Kiểm tra xem có bị tràn qua số 32bit hay không
        if so_dao_nguoc < GIOI_HAN_DUOI or so_dao_nguoc > GIOI_HAN_TREN:
            return 0
            
        return so_dao_nguoc