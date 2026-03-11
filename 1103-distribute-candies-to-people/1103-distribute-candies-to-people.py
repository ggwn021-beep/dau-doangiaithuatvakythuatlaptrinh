class Solution(object):
    def distributeCandies(self, candies, num_people):
        ket_qua = [0] * num_people # Ban đầu mỗi người có 0 kẹo
        so_keo_dinh_cho = 1        # Lần phát đầu tiên là 1 viên
        nguoi_hien_tai = 0         # Bắt đầu từ người đứng đầu tiên (vị trí 0)
        
        while candies > 0:
            # Phát kẹo: Nếu kẹo còn nhiều hơn mức định cho thì phát đủ, không thì vét sạch
            keo_phat_that_su = min(so_keo_dinh_cho, candies)
            
            # Đưa kẹo cho người hiện tại
            ket_qua[nguoi_hien_tai] += keo_phat_that_su
            
            # Trừ số kẹo trong rổ
            candies -= keo_phat_that_su
            
            # Chuẩn bị cho lượt sau
            so_keo_dinh_cho += 1
            
            # Chuyển sang người tiếp theo, nếu đến cuối hàng thì quay lại người đầu tiên
            nguoi_hien_tai = (nguoi_hien_tai + 1) % num_people
            
        return ket_qua