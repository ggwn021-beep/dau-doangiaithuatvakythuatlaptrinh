class Solution(object):
    def lengthOfLastWord(self, s):
        # s.split() chia câu thành ds các từ
        # [-1] lấy từ cuối cùng trong ds
        # len() đếm số chữ cái của từ đó
        return len(s.split()[-1])