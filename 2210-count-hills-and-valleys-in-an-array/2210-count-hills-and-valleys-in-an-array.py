class Solution(object):
    def countHillValley(self, nums):
        # 1. Khử trùng lặp: Nén các điểm bằng phẳng đứng cạnh nhau thành 1 điểm
        mang_nen = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                mang_nen.append(nums[i])
                
        dem = 0
        # 2. Quét mảng nén (bỏ qua vị trí đầu và cuối vì chúng không thể là đồi/thung lũng)
        for i in range(1, len(mang_nen) - 1):
            trai = mang_nen[i - 1]
            giua = mang_nen[i]
            phai = mang_nen[i + 1]
            
            # Đồi: Lớn hơn cả bên trái lẫn bên phải
            if giua > trai and giua > phai:
                dem += 1
            # Thung lũng: Nhỏ hơn cả bên trái lẫn bên phải
            elif giua < trai and giua < phai:
                dem += 1
                
        return dem