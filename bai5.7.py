import sys

def prefix_to_infix(expression):
    stack = []
    
    # Duyệt từ phải sang trái
    for char in reversed(expression):
        if char.isalpha():  # Nếu là toán hạng (A-Z)
            stack.append(char)
        else:  # Nếu là toán tử
            try:
                operand1 = stack.pop()
                operand2 = stack.pop()
                new_expr = f"({operand1}{char}{operand2})"
                stack.append(new_expr)
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
        print(prefix_to_infix(expr))
    except Exception as e:
        print(f"Lỗi: {e}")