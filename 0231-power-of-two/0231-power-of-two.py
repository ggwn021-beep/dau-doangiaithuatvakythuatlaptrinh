class Solution(object):
    def isPowerOfTwo(self, n):
        # Số phải lớn hơn 0 VÀ thỏa mãn tính chất triệt tiêu Bit
        return n > 0 and (n & (n - 1)) == 0