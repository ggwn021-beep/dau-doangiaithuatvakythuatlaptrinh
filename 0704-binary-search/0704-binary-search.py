class Solution(object):
    def search(self, nums, target):
        trai = 0
        phai = len(nums) - 1
        
        while trai <= phai:
            # Tính điểm ở giữa an toàn, chống tràn bộ nhớ
            giua = trai + (phai - trai) // 2
            
            if nums[giua] == target:
                return giua # Tìm thấy!
            elif nums[giua] < target:
                # Bỏ nửa bên trái, tập trung nửa bên phải
                trai = giua + 1
            else:
                # Bỏ nửa bên phải, tập trung nửa bên trái
                phai = giua - 1
                
        return -1 # Không tìm thấy