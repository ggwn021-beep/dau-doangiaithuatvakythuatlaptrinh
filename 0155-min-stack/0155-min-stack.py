class MinStack(object):

    def __init__(self):
        # Mảng lưu trữ Tuple: (Giá trị đưa vào, Giá trị Nhỏ nhất hiện tại)
        self.stack = []

    def push(self, val):
        if not self.stack:
            # Lần đầu tiên bỏ vào thì nó vừa là giá trị, vừa là Min
            self.stack.append((val, val))
        else:
            # Lấy Min hiện tại từ phần tử ngay dưới đỉnh
            min_hien_tai = self.stack[-1][1]
            # So sánh để tìm Min mới
            min_moi = min(val, min_hien_tai)
            self.stack.append((val, min_moi))

    def pop(self):
        self.stack.pop()

    def top(self):
        # Trả về giá trị thực (phần tử số 0 của Tuple)
        return self.stack[-1][0]

    def getMin(self):
        # Trả về giá trị Min (phần tử số 1 của Tuple)
        return self.stack[-1][1]