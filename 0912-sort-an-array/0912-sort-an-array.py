class Solution(object):
    def sortArray(self, nums):
        # Nếu mảng chỉ có 1 phần tử (or rỗng) thì ko cần xếp nữa
        if len(nums) <= 1:
            return nums
            
        # 1. CHIA ĐÔI MẢNG
        giua = len(nums) // 2
        trai = self.sortArray(nums[:giua])  # Nhờ đệ quy xếp nửa trái
        phai = self.sortArray(nums[giua:])  # Nhờ đệ quy xếp nửa phải
        
        # 2. GỘP LẠI (TRỘN)
        mang_da_xep = []
        i = 0  # Ngón tay trỏ vào nửa trái
        j = 0  # Ngón tay trỏ vào nửa phải
        
        # So sánh từng phần tử của 2 nửa, ai nhỏ hơn thì nhặt vào mảng mới
        while i < len(trai) and j < len(phai):
            if trai[i] < phai[j]:
                mang_da_xep.append(trai[i])
                i += 1
            else:
                mang_da_xep.append(phai[j])
                j += 1
                
        # Nhặt nốt những phần tử còn sót lại (nếu có)
        mang_da_xep.extend(trai[i:])
        mang_da_xep.extend(phai[j:])
        
        return mang_da_xep