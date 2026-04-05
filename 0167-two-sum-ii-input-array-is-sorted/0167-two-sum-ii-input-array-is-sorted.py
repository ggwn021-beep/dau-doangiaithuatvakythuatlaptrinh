class Solution(object):
    def twoSum(self, numbers, target):
        trai = 0
        phai = len(numbers) - 1
        
        while trai < phai:
            tong = numbers[trai] + numbers[phai]
            
            if tong == target:
                # Đề bài yêu cầu trả về vị trí tính từ 1 (1-indexed) nên ta cộng thêm 1
                return [trai + 1, phai + 1]
            elif tong < target:
                trai += 1 # Cần tổng to hơn -> Dịch sang phải (nơi có số to hơn)
            else:
                phai -= 1 # Cần tổng nhỏ hơn -> Dịch sang trái (nơi có số nhỏ hơn)