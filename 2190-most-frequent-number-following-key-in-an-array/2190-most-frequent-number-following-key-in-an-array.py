class Solution(object):
    def mostFrequent(self, nums, key):
        so_tay_dem = {}
        
        # Duyệt đến áp chót (n-1) vì cần phải xem thằng đằng sau (i+1)
        for i in range(len(nums) - 1):
            if nums[i] == key:
                cai_duoi = nums[i + 1]
                # Đếm tần suất của cái đuôi
                so_tay_dem[cai_duoi] = so_tay_dem.get(cai_duoi, 0) + 1
                
        # Tìm cái đuôi có số lần đếm cao nhất
        cai_duoi_pho_bien_nhat = -1
        so_lan_cao_nhat = 0
        
        for so, so_lan in so_tay_dem.items():
            if so_lan > so_lan_cao_nhat:
                so_lan_cao_nhat = so_lan
                cai_duoi_pho_bien_nhat = so
                
        return cai_duoi_pho_bien_nhat