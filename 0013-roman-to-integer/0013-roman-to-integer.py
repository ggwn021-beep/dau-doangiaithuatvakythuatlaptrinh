class Solution(object):
    def romanToInt(self, s):
        # Bảng quy đổi giá trị
        tu_dien = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        tong = 0
        
        # Đi ngược từ cuối chuỗi về đầu chuỗi
        for i in range(len(s) - 1, -1, -1):
            so_hien_tai = tu_dien[s[i]]
            
            # Nếu không phải là số cuối cùng VÀ số hiện tại nhỏ hơn số đứng sau nó -> trừ
            if i < len(s) - 1 and so_hien_tai < tu_dien[s[i+1]]:
                tong -= so_hien_tai
            else:
                # Ngược lại thì + dồn
                tong += so_hien_tai
                
        return tong