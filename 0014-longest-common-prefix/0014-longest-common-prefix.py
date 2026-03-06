class Solution(object):
    def longestCommonPrefix(self, strs):
        # Nếu ds rỗng thì ko có điểm chung
        if len(strs) == 0:
            return ""
            
        # Lấy từ đầu tiên làm "Mẫu đo" (ví dụ: "flower")
        tu_mau = strs[0]
        
        # Duyệt qua từng vị trí chữ cái (0, 1, 2...) của từ Mẫu
        for i in range(len(tu_mau)):
            chu_cai_hien_tai = tu_mau[i]
            
            # Đối chiếu chữ cái này vs all các từ còn lại trong ds
            for j in range(1, len(strs)):
                tu_kiem_tra = strs[j]
                
                # Nếu từ kt quá ngắn (hết chữ) or chữ cái ko khớp
                # -> Cắt ngay phần đầu từ 0 đến i và trả về kq
                if i >= len(tu_kiem_tra) or tu_kiem_tra[i] != chu_cai_hien_tai:
                    return tu_mau[0:i]
                    
        # Nếu duyệt hết từ Mẫu mà không bị lỗi gì, tức là từ Mẫu chính là điểm chung
        return tu_mau