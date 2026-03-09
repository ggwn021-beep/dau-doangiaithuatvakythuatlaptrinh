class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        # Biến danh sách đá quý thành một Tập hợp (Set) để tra cứu cực nhanh
        tap_hop_da_quy = set(jewels)
        
        so_luong = 0
        for da in stones:
            # Nếu cục đá này nằm trong tập hợp đá quý thì cộng 1
            if da in tap_hop_da_quy:
                so_luong += 1
                
        return so_luong