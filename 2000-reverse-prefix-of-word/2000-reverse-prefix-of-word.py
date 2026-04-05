class Solution(object):
    def reversePrefix(self, word, ch):
        # Tìm vị trí xuất hiện đầu tiên của ký tự
        vi_tri = word.find(ch)
        
        # Nếu không tìm thấy thì trả về y nguyên
        if vi_tri == -1:
            return word
            
        # Cắt khúc đầu: word[:vi_tri+1]
        # Lật ngược khúc đầu: [::-1]
        # Nối với khúc đuôi: word[vi_tri+1:]
        return word[:vi_tri + 1][::-1] + word[vi_tri + 1:]