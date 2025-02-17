import sys

def longest_valid_parentheses(s):
    stack = [-1]  # Stack để lưu chỉ số, bắt đầu bằng -1 để tính toán khoảng cách dễ dàng
    max_length = 0

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:  # char == ')'
            stack.pop()  # Bỏ phần tử gần nhất
            if stack:
                max_length = max(max_length, i - stack[-1])
            else:
                stack.append(i)  # Đánh dấu vị trí mới nếu không có '('

    return max_length

# Kiểm tra lỗi nhập số lượng test case
try:
    T = int(input("Nhập số lượng test case: ").strip())
except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")
    sys.exit(1)

# Xử lý từng test case
for _ in range(T):
    try:
        S = input("Nhập chuỗi S: ").strip()
        print(longest_valid_parentheses(S))
    except Exception as e:
        print(f"Lỗi: {e}")