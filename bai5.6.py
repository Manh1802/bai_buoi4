import sys

def precedence(op):
    if op == '^':
        return 3
    elif op in "*/":
        return 2
    elif op in "+-":
        return 1
    return 0

def infix_to_postfix(expression):
    stack = []  # Stack để lưu trữ toán tử và dấu ngoặc mở
    result = []  # Danh sách để lưu trữ biểu thức hậu tố

    for char in expression:
        if char.isalpha() or char.isdigit():  # Nếu là toán hạng (chữ cái hoặc số)
            result.append(char)
        elif char == '(':  # Nếu là dấu mở ngoặc
            stack.append(char)
        elif char == ')':  # Nếu là dấu đóng ngoặc
            while stack and stack[-1] != '(':
                result.append(stack.pop()) # Chuyển toán tử từ stack sang output cho đến khi gặp '('
            stack.pop()  # Loại bỏ dấu '(' khỏi stack (không thêm vào output)
        else:  # Nếu là toán tử
            while (stack and stack[-1] != '(' and precedence(stack[-1]) >= precedence(char)):
                # Chuyển toán tử từ stack sang output nếu độ ưu tiên >= toán tử hiện tại
                result.append(stack.pop())
            stack.append(char) # Đẩy toán tử hiện tại vào stack

    while stack: # Chuyển tất cả toán tử còn lại trong stack sang output
        result.append(stack.pop())

    return ''.join(result) # Kết hợp danh sách hậu tố thành chuỗi

# Xử lý lỗi nhập số lượng test case
try:
    T = int(input("Nhập số lượng test case: ").strip())
except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")
    sys.exit(1)

# Xử lý từng test case
for _ in range(T):
    try:
        expr = input("Nhập biểu thức trung tố: ").strip() # Nhập biểu thức trung tố từ người dùng
        print(infix_to_postfix(expr)) # In ra biểu thức hậu tố tương ứng
    except Exception as e:
        print(f"Lỗi: {e}") # In ra thông báo lỗi nếu có lỗi xảy ra