class Solution(object):
    def search(self, nums, target):
        trai = 0
        phai = len(nums) - 1
        
        while trai <= phai:
            giua = trai + (phai - trai) // 2
            
            if nums[giua] == target:
                return giua
                
            # Kiểm tra xem Nửa Bên Trái có phải là mảng được sắp xếp hoàn hảo không
            if nums[trai] <= nums[giua]:
                # Nếu Target nằm lọt thỏm trong nửa hoàn hảo này
                if nums[trai] <= target < nums[giua]:
                    phai = giua - 1 # Bỏ nửa phải, chui vào nửa trái
                else:
                    trai = giua + 1 # Bỏ nửa trái, chui sang nửa phải
            
            # Nếu Nửa Trái không hoàn hảo, vậy Nửa Bên Phải chắc chắn hoàn hảo
            else:
                if nums[giua] < target <= nums[phai]:
                    trai = giua + 1
                else:
                    phai = giua - 1
                    
        return -1