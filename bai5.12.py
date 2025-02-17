import sys

def evaluate_prefix(expression):
    stack = []

    # Duyệt từ phải sang trái
    for char in reversed(expression):
        if char.isdigit():  # Nếu là số (0-9)
            stack.append(int(char))
        else:  # Nếu là toán tử
            try:
                operand1 = stack.pop()
                operand2 = stack.pop()
                if char == '+':
                    stack.append(operand1 + operand2)
                elif char == '-':
                    stack.append(operand1 - operand2)
                elif char == '*':
                    stack.append(operand1 * operand2)
                elif char == '/':
                    stack.append(operand1 // operand2)  # Chia lấy phần nguyên
            except IndexError:
                print("Lỗi: Biểu thức tiền tố không hợp lệ!")
                sys.exit(1)

    return stack[0]  # Kết quả cuối cùng

# Kiểm tra lỗi nhập số lượng test case
try:
    T = int(input("Nhập số lượng test case: ").strip())
except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")
    sys.exit(1)

# Xử lý từng test case
for _ in range(T):
    try:
        expr = input("Nhập biểu thức tiền tố: ").strip()
        print(evaluate_prefix(expr))
    except Exception as e:
        print(f"Lỗi: {e}")