import sys
from collections import deque

# 6 hướng di chuyển trong không gian 3D
DIRECTIONS = [
    (1, 0, 0), (-1, 0, 0),  # Trục A (lên, xuống)
    (0, 1, 0), (0, -1, 0),  # Trục B (trái, phải)
    (0, 0, 1), (0, 0, -1)   # Trục C (trước, sau)
]

def is_valid(x, y, z, A, B, C, grid, visited):
    """Kiểm tra xem vị trí (x, y, z) có hợp lệ không"""
    return 0 <= x < A and 0 <= y < B and 0 <= z < C and grid[x][y][z] != '#' and not visited[x][y][z]

def bfs_min_steps(A, B, C, grid, start, end):
    """Tìm số bước ít nhất từ S -> E bằng BFS"""
    queue = deque([(start[0], start[1], start[2], 0)])  # (x, y, z, số bước)
    visited = [[[False] * C for _ in range(B)] for _ in range(A)]
    visited[start[0]][start[1]][start[2]] = True

    while queue:
        x, y, z, steps = queue.popleft()

        if (x, y, z) == end:
            return steps  # Tìm thấy E

        for dx, dy, dz in DIRECTIONS:
            nx, ny, nz = x + dx, y + dy, z + dz
            if is_valid(nx, ny, nz, A, B, C, grid, visited):
                visited[nx][ny][nz] = True
                queue.append((nx, ny, nz, steps + 1))

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
        A, B, C = map(int, input("Nhập A, B, C: ").strip().split())

        grid = []
        start = end = None

        # Đọc khối 3D
        for a in range(A):
            layer = []
            for b in range(B):
                row = list(input().strip())
                if 'S' in row:
                    start = (a, b, row.index('S'))
                if 'E' in row:
                    end = (a, b, row.index('E'))
                layer.append(row)
            grid.append(layer)

        if not start or not end:
            print("-1")  # Không có S hoặc E
        else:
            print(bfs_min_steps(A, B, C, grid, start, end))

    except Exception as e:
        print(f"Lỗi: {e}")