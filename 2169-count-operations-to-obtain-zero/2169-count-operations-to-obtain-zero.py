class Solution(object):
    def countOperations(self, num1, num2):
        so_buoc = 0
        
        # Dùng vòng lặp toán học thay vì trừ thủ công
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                # Chia lấy nguyên để đếm gộp số bước trừ
                so_buoc += num1 // num2
                # Chia lấy dư để ra kết quả sau khi trừ hàng loạt
                num1 = num1 % num2
            else:
                so_buoc += num2 // num1
                num2 = num2 % num1
                
        return so_buoc