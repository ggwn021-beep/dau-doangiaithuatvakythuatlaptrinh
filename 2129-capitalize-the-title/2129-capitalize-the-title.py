class Solution(object):
    def capitalizeTitle(self, title):
        # Cắt thành danh sách các từ
        danh_sach_tu = title.split()
        ket_qua = []
        
        for tu in danh_sach_tu:
            if len(tu) <= 2:
                # Từ ngắn: Viết thường toàn bộ
                ket_qua.append(tu.lower())
            else:
                # Từ dài: Viết hoa chữ đầu, còn lại viết thường
                ket_qua.append(tu.capitalize())
                
        # Nối lại thành chuỗi, cách nhau bởi khoảng trắng
        return " ".join(ket_qua)