import sys
from collections import deque

def is_prime(n):
    """Hàm kiểm tra số nguyên tố"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime_set():
    """Sinh tất cả các số nguyên tố 4 chữ số"""
    return {num for num in range(1000, 10000) if is_prime(num)}

def bfs_min_steps(S, T, prime_set):
    """Tìm số bước ít nhất để biến đổi S -> T"""
    queue = deque([(S, 0)])  # (Số hiện tại, số bước)
    visited = set([S])

    while queue:
        num, steps = queue.popleft()

        if num == T:
            return steps  # Tìm thấy T

        num_str = str(num)
        for i in range(4):  # Duyệt từng chữ số
            for digit in "0123456789":
                if num_str[i] != digit:
                    new_num = int(num_str[:i] + digit + num_str[i+1:])
                    if new_num in prime_set and new_num not in visited:
                        visited.add(new_num)
                        queue.append((new_num, steps + 1))

    return -1  # Không tìm thấy đường đi

# Tiền xử lý tập hợp số nguyên tố
prime_set = generate_prime_set()

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
        print(bfs_min_steps(S, T, prime_set))
    except Exception as e:
        print(f"Lỗi: {e}")