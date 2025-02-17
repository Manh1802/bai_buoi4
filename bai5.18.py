import sys
from collections import Counter

def find_next_greater_frequency(arr):
    n = len(arr)
    freq = Counter(arr)  # Tính số lần xuất hiện của mỗi phần tử
    stack = []
    result = [-1] * n  # Mặc định gán -1

    for i in range(n - 1, -1, -1):  # Duyệt từ phải sang trái
        while stack and freq[stack[-1]] <= freq[arr[i]]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])

    return result

# Kiểm tra lỗi nhập số lượng test case
try:
    T = int(input("Nhập số lượng test case: ").strip())
except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")
    sys.exit(1)

# Xử lý từng test case
for _ in range(T):
    try:
        n = int(input("Nhập số phần tử của mảng: ").strip())
        arr = list(map(int, input("Nhập mảng: ").strip().split()))
        if len(arr) != n:
            print("Lỗi: Số phần tử không khớp!")
            sys.exit(1)
        print(*find_next_greater_frequency(arr))
    except Exception as e:
        print(f"Lỗi: {e}")