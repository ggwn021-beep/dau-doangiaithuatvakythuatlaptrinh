class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        # 1. Xếp hàng từ thấp đến cao
        hang_da_xep = sorted(nums)
        
        # 2. Tạo sổ ghi chép (Hash map)
        so_tay_vi_tri = {}
        
        # enumerate giúp lấy cả vị trí (i) và giá trị (so)
        for i, so in enumerate(hang_da_xep):
            # Nếu con số này chưa có trong sổ thì mới ghi, để ưu tiên người đứng đầu tiên trong nhóm những người cao bằng nhau
            if so not in so_tay_vi_tri:
                so_tay_vi_tri[so] = i 
                
        # 3. Lấy đội hình ban đầu, tra sổ và trả về kết quả
        ket_qua = []
        for so in nums:
            ket_qua.append(so_tay_vi_tri[so])
            
        return ket_qua