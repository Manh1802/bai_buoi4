import sys

def min_bracket_reversals(s):
    stack = []
    count = 0  # Số lần đổi dấu cần thiết

    for char in s:
        if char == '(':
            stack.append(char)
        else:  # char == ')'
            if stack and stack[-1] == '(':
                stack.pop()  # Loại bỏ cặp ngoặc hợp lệ
            else:
                stack.append(char)  # Dấu ')' dư thừa

    # Sau khi duyệt xong, stack chứa toàn bộ ngoặc chưa ghép cặp
    open_count = stack.count('(')
    close_count = stack.count(')')

    # Đổi chiều: Cứ 2 dấu ngoặc dư sẽ cần 1 lần đổi
    return (open_count // 2) + (close_count // 2)

# Đọc số lượng test case
try:
    T = int(input("Nhập số lượng test case: ").strip())
except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")
    sys.exit(1)

# Xử lý từng test case
print("\nKết quả kiểm tra:")
for _ in range(T):
    try:
        s = input("Nhập chuỗi ngoặc: ").strip()
        if any(c not in "() " for c in s):  # Kiểm tra ký tự không hợp lệ
            raise ValueError
        print(min_bracket_reversals(s))
    except ValueError:
        print("Lỗi: Chuỗi chỉ được chứa dấu '(' và ')'. Thử lại!")

# Chạy thử test case tự động
print("\nChạy test case tự động:")
test_cases = [")>(", "((((", "(()(", ")()()("]
for expression in test_cases:
    print(f"{expression} → {min_bracket_reversals(expression)}")