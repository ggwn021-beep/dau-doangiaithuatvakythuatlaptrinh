class Solution(object):
    def toGoatLatin(self, sentence):
        danh_sach_tu = sentence.split() # Cắt câu thành các từ rời nhau
        nguyen_am = set('aeiouAEIOU')   # Bộ nhớ các nguyên âm
        ket_qua = []
        
        for i, tu in enumerate(danh_sach_tu):
            # i bắt đầu từ 0, nên vị trí thực tế của từ là i + 1
            
            if tu[0] in nguyen_am:
                tu_moi = tu + "ma"
            else:
                # Cắt chữ đầu (tu[0]) ghép ra sau, rồi thêm "ma"
                tu_moi = tu[1:] + tu[0] + "ma"
                
            # Thêm tiếng dê kêu "a" nhân với vị trí của từ
            tu_moi += "a" * (i + 1)
            ket_qua.append(tu_moi)
            
        # Nối các từ lại thành một câu, cách nhau bởi khoảng trắng
        return " ".join(ket_qua)