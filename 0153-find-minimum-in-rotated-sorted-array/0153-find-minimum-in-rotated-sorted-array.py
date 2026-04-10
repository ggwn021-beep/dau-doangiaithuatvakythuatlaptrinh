class Solution(object):
    def findMin(self, nums):
        trai = 0
        phai = len(nums) - 1
        
        while trai < phai:
            giua = trai + (phai - trai) // 2
            
            # Nếu phần tử giữa CAO HƠN phần tử tận cùng bên phải
            # Nghĩa là điểm gãy khúc (nơi chứa Min) chắc chắn nằm bên MẢNG PHẢI
            if nums[giua] > nums[phai]:
                trai = giua + 1
            else:
                # Nếu phần tử giữa thấp hơn, đoạn từ giữa đến phải là đoạn tăng dần bình thường
                # Điểm Min có thể là chính phần tử giữa, hoặc nằm bên TRÁI
                phai = giua 
                
        return nums[trai]