class Solution(object):
    def checkTree(self, root):
        # Truy cập trực tiếp vào giá trị của 3 Node và so sánh
        tong_hai_con = root.left.val + root.right.val
        return root.val == tong_hai_con