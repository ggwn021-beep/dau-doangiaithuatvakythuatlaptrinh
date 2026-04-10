# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        trai = 1
        phai = n
        
        while trai <= phai:
            giua = trai + (phai - trai) // 2
            ket_qua = guess(giua)
            
            if ket_qua == 0:
                return giua # Đoán đúng
            elif ket_qua == 1:
                # Đoán nhỏ quá, phải nhích sang khoảng bên phải
                trai = giua + 1
            else:
                # Đoán to quá, lùi về khoảng bên trái
                phai = giua - 1