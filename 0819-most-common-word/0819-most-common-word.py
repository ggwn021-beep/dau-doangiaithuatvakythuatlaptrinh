class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        # 1. Dọn dẹp câu văn: Thay thế các dấu câu bằng khoảng trắng
        dau_cau = "!?',;."
        for dau in dau_cau:
            paragraph = paragraph.replace(dau, " ")
            
        # 2. Chữ thường và cắt thành danh sách từ
        cac_tu = paragraph.lower().split()
        
        # 3. Tạo set từ cấm để tra cứu cho lẹ
        tap_hop_cam = set(banned)
        
        # 4. Lập sổ tay đếm (Hash Map)
        so_tay = {}
        tu_nhieu_nhat = ""
        so_lan_nhieu_nhat = 0
        
        for tu in cac_tu:
            if tu not in tap_hop_cam:
                if tu in so_tay:
                    so_tay[tu] += 1
                else:
                    so_tay[tu] = 1
                    
                # Liên tục cập nhật từ nhiều nhất
                if so_tay[tu] > so_lan_nhieu_nhat:
                    so_lan_nhieu_nhat = so_tay[tu]
                    tu_nhieu_nhat = tu
                    
        return tu_nhieu_nhat