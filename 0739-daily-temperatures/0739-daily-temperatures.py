class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        ket_qua = [0] * n # Ban đầu cho tất cả là 0 (nếu không tìm thấy)
        ngan_xep = []     # Chỉ lưu trữ "Vị trí (ngày)" đang chờ
        
        for ngay_hien_tai, nhiet_do_hom_nay in enumerate(temperatures):
            # Nếu ngăn xếp có người chờ, VÀ nhiệt độ hôm nay NÓNG HƠN nhiệt độ của người đang chờ trên đỉnh
            while ngan_xep and nhiet_do_hom_nay > temperatures[ngan_xep[-1]]:
                # Lấy người đó ra khỏi hàng chờ
                ngay_cho = ngan_xep.pop()
                # Tính số ngày họ phải đợi
                ket_qua[ngay_cho] = ngay_hien_tai - ngay_cho
                
            # Đưa ngày hôm nay vào danh sách chờ
            ngan_xep.append(ngay_hien_tai)
            
        return ket_qua