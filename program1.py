class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        
        def dfs(r, c):
            # Directions: up, down, left, right
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            stack = [(r, c)]
            visited[r][c] = True
            
            while stack:
                x, y = stack.pop()
                for dr, dc in directions:
                    new_r, new_c = x + dr, y + dc
                    if 0 <= new_r < rows and 0 <= new_c < cols:
                        if grid[new_r][new_c] == 'L' and not visited[new_r][new_c]:
                            visited[new_r][new_c] = True
                            stack.append((new_r, new_c))

        island_count = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'L' and not visited[i][j]:
                    # Found a new island
                    island_count += 1
                    dfs(i, j)  # Mark the entire island as visited
        
        return island_count
