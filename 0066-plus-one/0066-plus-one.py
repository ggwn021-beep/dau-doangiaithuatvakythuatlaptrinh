class Solution(object):
    def plusOne(self, digits):
        # Đi ngược từ cuối mảng lên đầu mảng
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0 # Tràn số, biến thành 0 và tiếp tục vòng lặp để nhớ 1 sang trái
            else:
                digits[i] += 1
                return digits # Đã cộng xong mà không tràn, trả về luôn!
                
        # Nếu chạy hết vòng lặp mà chưa return (nghĩa là toàn số 9, ví dụ 99 -> 00)
        # Ta phải nhét thêm số 1 vào đầu hàng
        return [1] + digits