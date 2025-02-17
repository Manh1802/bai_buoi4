import sys
from collections import deque

def is_valid(x, y, N, grid, visited):
    """Kiểm tra xem vị trí (x, y) có hợp lệ không"""
    return 0 <= x < N and 0 <= y < N and grid[x][y] != 'X' and not visited[x][y]

def bfs_min_steps(grid, N, start, end):
    """Tìm số bước ít nhất từ start -> end bằng BFS"""
    a, b = start
    c, d = end
    
    # Nếu điểm xuất phát và đích trùng nhau
    if (a, b) == (c, d):
        return 0

    # Duyệt theo 4 hướng (trái, phải, lên, xuống)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(a, b, 0)])  # (x, y, số bước)
    visited = [[False] * N for _ in range(N)]
    visited[a][b] = True

    while queue:
        x, y, steps = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            while is_valid(nx, ny, N, grid, visited):
                if (nx, ny) == (c, d):
                    return steps + 1
                visited[nx][ny] = True
                queue.append((nx, ny, steps + 1))
                nx += dx
                ny += dy

    return -1  # Không tìm thấy đường đi

# Kiểm tra lỗi nhập số lượng test case
try:
    T = int(input("Nhập số lượng test case: ").strip())
except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")
    sys.exit(1)

# Xử lý từng test case
for _ in range(T):
    try:
        N = int(input("Nhập kích thước bảng N: ").strip())
        grid = [input().strip() for _ in range(N)]
        a, b, c, d = map(int, input("Nhập tọa độ điểm xuất phát và đích: ").strip().split())
        print(bfs_min_steps(grid, N, (a, b), (c, d)))
    except Exception as e:
        print(f"Lỗi: {e}")