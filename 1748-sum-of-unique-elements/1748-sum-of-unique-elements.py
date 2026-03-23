class Solution(object):
    def sumOfUnique(self, nums):
        so_tay_dem = {}
        
        # Vòng 1: Ghi sổ (Nạp vào Hash Map)
        for so in nums:
            so_tay_dem[so] = so_tay_dem.get(so, 0) + 1
            
        tong = 0
        # Vòng 2: Truy vấn sổ
        for so, so_lan in so_tay_dem.items():
            if so_lan == 1:
                tong += so
                
        return tong