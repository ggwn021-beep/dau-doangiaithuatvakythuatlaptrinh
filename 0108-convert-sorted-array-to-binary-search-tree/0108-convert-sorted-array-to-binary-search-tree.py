class Solution(object):
    def sortedArrayToBST(self, nums):
        
        def xay_thap(trai, phai):
            if trai > phai:
                return None
                
            # Lấy phần tử chính giữa làm gốc
            giua = (trai + phai) // 2
            goc = TreeNode(nums[giua])
            
            # Đệ quy xây cành trái và cành phải
            goc.left = xay_thap(trai, giua - 1)
            goc.right = xay_thap(giua + 1, phai)
            
            return goc
            
        return xay_thap(0, len(nums) - 1)