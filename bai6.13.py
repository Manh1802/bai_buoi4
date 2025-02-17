import sys
from itertools import product

def generate_lucky_numbers(N):
    """Sinh tất cả các số có độ dài từ 1 đến N chỉ chứa 6 và 8"""
    result = []
    for length in range(1, N + 1):
        for num_tuple in product("68", repeat=length):
            result.append("".join(num_tuple))
    return sorted(result, key=int)  # Sắp xếp tăng dần

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
        lucky_numbers = generate_lucky_numbers(N)
        print(len(lucky_numbers))
        print(" ".join(lucky_numbers))
    except Exception as e:
        print(f"Lỗi: {e}")