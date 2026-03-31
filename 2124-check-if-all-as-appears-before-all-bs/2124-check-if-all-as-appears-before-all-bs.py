class Solution(object):
    def checkString(self, s):
        # Nếu có chữ 'a' đứng sau chữ 'b' (tức là cụm "ba" xuất hiện) thì trả về False
        # Tối ưu bằng toán tử 'in' của Python được viết bằng C
        return "ba" not in s