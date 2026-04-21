class Solution(object):
    def singleNumber(self, nums):
        ket_qua = 0
        for so in nums:
            # Phép XOR sẽ tự động ghép cặp và triệt tiêu các con số giống nhau
            ket_qua ^= so
            
        return ket_qua