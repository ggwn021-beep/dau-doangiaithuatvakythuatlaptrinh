import collections

class Solution(object):
    def isAnagram(self, s, t):
        # Nếu độ dài 2 chữ khác nhau thì chắc chắn không thể là đảo chữ
        if len(s) != len(t):
            return False
            
        # Đếm và so sánh số lượng từng chữ cái của 2 bên
        return collections.Counter(s) == collections.Counter(t)