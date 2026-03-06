class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        # 1. Tạo sổ tay kiểm kê số lượng chữ cái có trong Tạp chí (magazine)
        so_tay_tap_chi = {}
        
        for chu in magazine:
            if chu in so_tay_tap_chi:
                so_tay_tap_chi[chu] += 1
            else:
                so_tay_tap_chi[chu] = 1
                
        # 2. Bắt đầu viết thư
        for chu in ransomNote:
            # Tra sổ: Tạp chí có chữ này không? Và số lượng còn dư để xài không?
            if chu in so_tay_tap_chi and so_tay_tap_chi[chu] > 0:
                so_tay_tap_chi[chu] -= 1  # Lấy xài 1 chữ thì bớt đi 1
            else:
                # Nếu tạp chí không có chữ này or đã bị xài hết sạch
                return False
        return True