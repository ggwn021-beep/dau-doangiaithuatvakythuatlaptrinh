class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # 3 con trỏ cùng xuất phát từ cuối mảng
        p1 = m - 1          # Trỏ vào số lớn nhất của phần thực trong nums1
        p2 = n - 1          # Trỏ vào số lớn nhất của nums2
        p_chot = m + n - 1  # Trỏ vào ô trống tận cùng của nums1
        
        # Bắt đầu so sánh từ đuôi lên đầu
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p_chot] = nums1[p1]
                p1 -= 1
            else:
                nums1[p_chot] = nums2[p2]
                p2 -= 1
            p_chot -= 1
            
        # Nếu nums2 vẫn còn người (nums1 đã hết), chuyển nốt nums2 sang
        # Không cần làm ngược lại vì nếu nums1 còn thì nó đã nằm đúng chỗ rồi
        while p2 >= 0:
            nums1[p_chot] = nums2[p2]
            p2 -= 1
            p_chot -= 1