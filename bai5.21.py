import sys

def total_valid_parentheses_length(s):
    stack = []
    valid_segments = [0] * len(s)  # Đánh dấu các phần hợp lệ
    total_length = 0

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                start_index = stack.pop()
                valid_segments[start_index] = 1
                valid_segments[i] = 1

    return sum(valid_segments)

# Kiểm tra lỗi nhập số lượng test case
try:
    T = int(input("Nhập số lượng test case: ").strip())
except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")
    sys.exit(1)

# Xử lý từng test case
for _ in range(T):
    try:
        P = input("Nhập biểu thức P: ").strip()
        print(total_valid_parentheses_length(P))
    except Exception as e:
        print(f"Lỗi: {e}")