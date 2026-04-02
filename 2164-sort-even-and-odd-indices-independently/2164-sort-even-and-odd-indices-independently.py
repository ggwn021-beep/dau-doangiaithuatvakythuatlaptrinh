class Solution(object):
    def sortEvenOdd(self, nums):
        # 1. Trích xuất phần tử ở vị trí chẵn và lẻ
        # [::2] nghĩa là bắt đầu từ 0, nhảy 2 bước (0, 2, 4...)
        # [1::2] nghĩa là bắt đầu từ 1, nhảy 2 bước (1, 3, 5...)
        chan = nums[::2]
        le = nums[1::2]
        
        # 2. Sắp xếp độc lập (Chẵn tăng dần, Lẻ giảm dần)
        chan.sort()
        le.sort(reverse=True)
        
        # 3. Ghi đè trực tiếp lên mảng gốc
        nums[::2] = chan
        nums[1::2] = le
        
        return nums