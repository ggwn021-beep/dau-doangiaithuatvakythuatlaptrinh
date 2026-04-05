class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
            
        # Con trỏ chậm (bắt đầu từ 1 vì phần tử 0 luôn là duy nhất)
        cham = 1
        
        # Con trỏ nhanh quét từ vị trí 1 đến hết mảng
        for nhanh in range(1, len(nums)):
            # Nếu phát hiện một con số mới (khác với số ngay trước nó)
            if nums[nhanh] != nums[nhanh - 1]:
                # Ghi đè con số mới vào vị trí của con trỏ chậm
                nums[cham] = nums[nhanh]
                cham += 1 # Nhích con trỏ chậm lên 1 bước để đón số mới tiếp theo
                
        # Trả về k (chính là vị trí của con trỏ chậm)
        return cham