class Solution(object):
    def findJudge(self, n, trust):
        # Nếu thị trấn chỉ có 1 người và không có ai tin tưởng ai -> Người đó tự làm Thẩm phán
        if n == 1 and not trust:
            return 1
            
        # Tạo mảng điểm số cho N người (cộng 1 để index trùng với tên người từ 1 đến N)
        diem_tin_nhiem = [0] * (n + 1)
        
        for a, b in trust:
            diem_tin_nhiem[a] -= 1 # 'a' đi tin tưởng người khác -> Trừ điểm
            diem_tin_nhiem[b] += 1 # 'b' được tin tưởng -> Cộng điểm
            
        # Tìm xem ai có điểm tuyệt đối là (N - 1)
        for nguoi in range(1, n + 1):
            if diem_tin_nhiem[nguoi] == n - 1:
                return nguoi
                
        return -1