class Solution(object):
    def isValid(self, s):
        ngan_xep = []
        # Từ điển ánh xạ nắp hộp (ngoặc đóng) với thân hộp (ngoặc mở)
        tu_dien = {')': '(', ']': '[', '}': '{'}
        
        for dau in s:
            if dau in tu_dien: # Nếu đây là ngoặc đóng
                # Lấy cái nắp trên cùng của ngăn xếp ra (nếu ngăn xếp rỗng thì gán ký tự ảo '#')
                nap_tren_cung = ngan_xep.pop() if ngan_xep else '#'
                
                # Nếu thân hộp không khớp với nắp hộp -> Sai
                if tu_dien[dau] != nap_tren_cung:
                    return False
            else:
                # Nếu là ngoặc mở, cứ cất vào ngăn xếp
                ngan_xep.append(dau)
                
        # Cuối cùng, nếu ngăn xếp trống trơn (đóng hết hộp) thì hợp lệ
        return not ngan_xep