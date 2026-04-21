class Solution(object):
    def addBinary(self, a, b):
        # Chuyển từ hệ nhị phân sang số nguyên, cộng lại, rồi chuyển ngược về nhị phân
        return bin(int(a, 2) + int(b, 2))[2:]