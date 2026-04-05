class Solution(object):
    def removeElement(self, nums, val):
        k = 0 # Con trỏ k chỉ vào vị trí sẽ được giữ lại
        
        for i in range(len(nums)):
            # Nếu phần tử hiện tại KHÔNG PHẢI là đồ bỏ đi
            if nums[i] != val:
                # Ghi đè nó vào vị trí an toàn k
                nums[k] = nums[i]
                k += 1 # Nhích vị trí an toàn lên
                
        return k