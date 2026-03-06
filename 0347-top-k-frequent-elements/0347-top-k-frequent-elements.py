import collections

class Solution(object):
    def topKFrequent(self, nums, k):
        # Counter sẽ đếm sl từng phần tử
        # most_common(k) sẽ lấy ra k phần tử xuất hiện nhiều nhất
        # Trả về ds chỉ chứa tên phần tử (ko lấy số lần đếm)
        return [phan_tu for phan_tu, so_lan in collections.Counter(nums).most_common(k)]