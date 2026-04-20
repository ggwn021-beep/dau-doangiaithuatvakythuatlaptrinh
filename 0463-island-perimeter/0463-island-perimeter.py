class Solution(object):
    def islandPerimeter(self, grid):
        hang = len(grid)
        cot = len(grid[0])
        
        dat = 0
        canh_ke = 0
        
        for r in range(hang):
            for c in range(cot):
                if grid[r][c] == 1:
                    dat += 1
                    
                    # Kiểm tra xem ô BÊN DƯỚI có phải là đất không (tạo thành 1 cạnh kề)
                    if r + 1 < hang and grid[r + 1][c] == 1:
                        canh_ke += 1
                        
                    # Kiểm tra xem ô BÊN PHẢI có phải là đất không (tạo thành 1 cạnh kề)
                    if c + 1 < cot and grid[r][c + 1] == 1:
                        canh_ke += 1
                        
        # Công thức: Tổng số cạnh độc lập - Những phần bị che khuất
        return dat * 4 - canh_ke * 2