import sys
from collections import deque

def count_bdn(n):
    queue = deque(["1"])  # Hàng đợi BFS bắt đầu từ "1"
    count = 0  # Đếm số BDN

    while queue:
        num = int(queue.popleft())  # Chuyển về số nguyên
        if num > n:
            break
        count += 1
        queue.append(str(num) + "0")
        queue.append(str(num) + "1")

    return count

# Kiểm tra lỗi nhập số lượng test case
try:
    T = int(input("Nhập số lượng test case: ").strip())
except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")
    sys.exit(1)

# Xử lý từng test case
for _ in range(T):
    try:
        N = int(input("Nhập số N: ").strip())
        print(count_bdn(N))
    except Exception as e:
        print(f"Lỗi: {e}")