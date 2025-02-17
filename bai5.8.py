import sys

def prefix_to_postfix(expression):
    """
    Converts a prefix expression to postfix expression.

    Args:
        expression: The prefix expression string.

    Returns:
        The postfix expression string.
    """
    stack = []

    # Duyệt biểu thức tiền tố từ phải sang trái (reversed)
    for char in reversed(expression):
        if char.isalpha() or char.isdigit():  # Nếu là toán hạng (chữ cái hoặc số)
            stack.append(char)
        else:  # Nếu là toán tử
            if not stack or len(stack) < 2:
                print("Lỗi: Biểu thức tiền tố không hợp lệ!")
                sys.exit(1)
            operand1 = stack.pop()
            operand2 = stack.pop()
            # Tạo dạng hậu tố: operand1 + operand2 + operator
            new_expr = operand1 + operand2 + char
            stack.append(new_expr)

    if len(stack) != 1:
        print("Lỗi: Biểu thức tiền tố không hợp lệ!")
        sys.exit(1)

    return stack[0]

# Kiểm tra lỗi nhập số lượng test case
try:
    T = int(input().strip())
except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")
    sys.exit(1)

# Xử lý từng test case
for _ in range(T):
    try:
        expr = input().strip()
        print(prefix_to_postfix(expr))
    except Exception as e:
        print(f"Lỗi: {e}")