class Solution(object):
    def plusOne(self, digits):
        # Đi từ cuối mảng (hàng đon vị) ngược lên đầu
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits # Cộng xong mà không bị tràn (nhớ 1) thì kết thúc
            else:
                # Nếu là số 9 thì thành 0 và nhường quyền cộng (nhớ 1) cho vòng lặp tiếp theo
                digits[i] = 0
                
        # Nếu vòng lặp chạy hết sạch mà vẫn không return (ví dụ mảng ban đầu là [9, 9, 9] thành [0, 0, 0])
        # Thì ta phải nhét thêm số 1 vào đầu mảng (thành [1, 0, 0, 0])
        return [1] + digits