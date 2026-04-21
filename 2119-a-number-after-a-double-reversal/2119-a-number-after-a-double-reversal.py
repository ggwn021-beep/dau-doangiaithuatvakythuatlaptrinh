class Solution(object):
    def isSameAfterReversals(self, num):
        # Số 0 thì luôn đúng. Các số khác thì chữ số tận cùng không được phép là số 0.
        return num == 0 or num % 10 != 0