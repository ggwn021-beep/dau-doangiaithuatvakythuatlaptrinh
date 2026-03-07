class Solution(object):
    def firstUniqChar(self, s):
        # 1. Tạo sổ tay ghi chép số lần xuất hiện của từng chữ cái
        so_tay = {}
        for chu_cai in s:
            if chu_cai in so_tay:
                so_tay[chu_cai] += 1
            else:
                so_tay[chu_cai] = 1
                
        # 2. Quay lại đầu hàng để tìm chữ cái đầu tiên xuất hiện
        for i in range(len(s)):
            chu_cai = s[i]
            if so_tay[chu_cai] == 1:
                return i
                
        return -1 # Ko có chữ cái tm