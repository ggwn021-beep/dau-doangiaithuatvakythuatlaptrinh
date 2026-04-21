class Solution(object):
    def majorityElement(self, nums):
        ung_cu_vien = None
        diem = 0
        
        for phieu_bau in nums:
            if diem == 0:
                # Điểm về 0 thì cập nhật ứng cử viên mới
                ung_cu_vien = phieu_bau
                
            # Nếu gặp đúng người mình đang ủng hộ thì +1, gặp người khác phe thì -1
            if phieu_bau == ung_cu_vien:
                diem += 1
            else:
                diem -= 1
                
        return ung_cu_vien