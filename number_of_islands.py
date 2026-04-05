def count_islands(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    islands_count = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def bfs(start_r, start_c):
        queue = [(start_r, start_c)]
        visited[start_r][start_c] = True
        
        while queue:
            curr_r, curr_c = queue.pop(0) 
            
            for dr, dc in directions:
                nr, nc = curr_r + dr, curr_c + dc
                if (0 <= nr < rows and 0 <= nc < cols and 
                    grid[nr][nc] == 1 and not visited[nr][nc]):
                    visited[nr][nc] = True
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                bfs(r, c)
                islands_count += 1
                
    return islands_count