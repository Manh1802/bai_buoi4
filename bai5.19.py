import sys

def stock_span(prices):
    n = len(prices)
    stack = []
    result = [0] * n  # Lưu kết quả

    for i in range(n):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        result[i] = i - stack[-1] if stack else i + 1
        stack.append(i)

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
        N = int(input("Nhập số ngày: ").strip())
        prices = list(map(int, input("Nhập giá chứng khoán: ").strip().split()))
        if len(prices) != N:
            print("Lỗi: Số ngày nhập vào không khớp!")
            sys.exit(1)
        print(*stock_span(prices))
    except Exception as e:
        print(f"Lỗi: {e}")