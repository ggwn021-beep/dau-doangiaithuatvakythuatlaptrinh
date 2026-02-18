class Solution(object):
    def twoSum(self, nums, target):
        s = {}  # Tạo một cuốn sổ tay rỗng
        
        for i, num in enumerate(nums):
            can_tim = target - num  # Tính xem mình đang thiếu số mấy
            
            if can_tim in s:   # Tra sổ: Số cần tìm đã xuất hiện chưa?
                return [s[can_tim], i]  # Nếu có rồi -> Xong!
            
            s[num] = i  # Nếu chưa, ghi số hiện tại và vị trí vào sổ