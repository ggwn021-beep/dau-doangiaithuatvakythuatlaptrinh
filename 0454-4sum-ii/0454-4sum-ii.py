class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        # Bước 1: Ghép mảng 1 và 2, ghi kết quả vào sổ tay
        so_tay_tong = {}
        for a in nums1:
            for b in nums2:
                tong = a + b
                if tong in so_tay_tong:
                    so_tay_tong[tong] += 1
                else:
                    so_tay_tong[tong] = 1
                    
        # Bước 2: Ghép mảng 3 và 4, đem đối chiếu với sổ tay
        so_cach_ghep = 0
        for c in nums3:
            for d in nums4:
                muc_tieu = -(c + d) # Số tiền cần tìm để bù nợ cho C và D
                
                # Trong sổ tay có ghi lại cái "muc_tieu" này thì cộng dồn số cách ghép vào
                if muc_tieu in so_tay_tong:
                    so_cach_ghep += so_tay_tong[muc_tieu]
                    
        return so_cach_ghep