class Solution(object):
    def duplicateZeros(self, arr):
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                # Chèn thêm 1 số 0 vào ngay sau vị trí hiện tại
                arr.insert(i + 1, 0)
                # Vì mảng bị dài ra, ta vứt phần tử cuối đi để giữ nguyên độ dài
                arr.pop()
                # Phải nhảy cóc 2 bước để bỏ qua số 0 vừa chèn, nếu không sẽ bị lặp vô tận
                i += 2
            else:
                # Nếu không phải số 0 thì bước 1 bước như bình thường
                i += 1