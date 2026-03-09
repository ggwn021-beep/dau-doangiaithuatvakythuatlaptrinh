class Solution(object):
    def toLowerCase(self, s):
        ket_qua = ""
        
        for chu in s:
            # Kiểm tra xem chữ này có phải là in hoa không (Mã ASCII từ 'A' đến 'Z')
            if 'A' <= chu <= 'Z':
                # ord(): Lấy mã số của chữ
                # Cộng thêm 32 để biến thành chữ thường
                # chr(): Biến mã số ngược lại thành chữ
                chu_thuong = chr(ord(chu) + 32)
                ket_qua += chu_thuong
            else:
                ket_qua += chu # Giữ nguyên các chữ thường, số, ký tự đặc biệt...
                
        return ket_qua