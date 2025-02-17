import sys
from collections import deque

def min_operations(S, T):
    queue = deque([(S, 0)])  # (Giá trị S, số bước)
    visited = set()

    while queue:
        value, steps = queue.popleft()

        if value == T:
            return steps  # Tìm thấy kết quả

        if value not in visited:
            visited.add(value)
            if value * 2 <= T * 2:  # Nếu phép nhân hợp lệ, thêm vào queue
                queue.append((value * 2, steps + 1))
            if value - 1 > 0:  # Nếu phép trừ hợp lệ, thêm vào queue
                queue.append((value - 1, steps + 1))

# Kiểm tra lỗi nhập số lượng test case
try:
    T = int(input("Nhập số lượng test case: ").strip())
except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")
    sys.exit(1)

# Xử lý từng test case
for _ in range(T):
    try:
        S, T = map(int, input("Nhập S và T: ").strip().split())
        print(min_operations(S, T))
    except Exception as e:
        print(f"Lỗi: {e}")