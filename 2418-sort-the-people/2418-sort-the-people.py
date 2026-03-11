class Solution(object):
    def sortPeople(self, names, heights):
        # Tạo danh sách các cặp (h,n), để chiều cao lên trước để biết mà lấy ra so sánh
        danh_sach_ghim = []
        for i in range(len(names)):
            danh_sach_ghim.append((heights[i], names[i]))
            
        # Sắp xếp danh sách giảm dần từ cao xuống thấp
        danh_sach_ghim.sort(reverse=True)
        
        # Gỡ ghim, chỉ lấy lại cái tên cất vào mảng kết quả
        ket_qua = []
        for cap in danh_sach_ghim:
            ket_qua.append(cap[1]) # cap[1] chính là phần tên
            
        return ket_qua