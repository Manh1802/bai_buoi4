import sys
from collections import deque

def generate_binary_numbers(n):
    queue = deque(["1"])  # Hàng đợi bắt đầu từ "1"
    result = []

    for _ in range(n):
        binary = queue.popleft()  # Lấy số đầu tiên ra khỏi queue
        result.append(binary)  # Thêm vào danh sách kết quả
        queue.append(binary + "0")  # Thêm số mới vào queue
        queue.append(binary + "1")

    return " ".join(result)

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
        print(generate_binary_numbers(N))
    except Exception as e:
        print(f"Lỗi: {e}")