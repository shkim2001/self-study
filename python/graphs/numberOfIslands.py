class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
#         res = 0
#         visited = set()
        
#         def bfs(i, j):
#             q = deque()
#             visited.add((i,j))
#             q.append((i,j))
            
#             while q:
#                 currentRow, currentCol = q.popleft()
#                 directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                
#                 for row, col in directions:
#                     r, c = row + currentRow, col + currentCol
                    
#                     if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1" and (r, c) not in visited:
#                         q.append((r,c))
#                         visited.add((r,c))
#                 # print(q, visited)
                    
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == "1" and (i, j) not in visited:
#                     bfs(i, j)
#                     res += 1
#         return res
        
        islands = 0 # variable to keep track of result
        for i in range(len(grid)):  #loop through the grid
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    islands += 1
                    self.part_of_island(i,j,grid)
        return islands
    
    def part_of_island(self, i:int, j:int, grid: List[List[str]]):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != '1':
            return
        else:
            grid[i][j] = '0'
        self.part_of_island(i,j+1,grid)
        self.part_of_island(i,j-1,grid)
        self.part_of_island(i+1,j,grid)
        self.part_of_island(i-1,j,grid)  