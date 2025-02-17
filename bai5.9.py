import sys

def postfix_to_prefix(expression):
    """
    Converts a postfix expression to prefix expression.

    Args:
        expression: The postfix expression string.

    Returns:
        The prefix expression string.
    """
    stack = []

    # Duyệt biểu thức hậu tố từ trái sang phải
    for char in expression:
        if char.isalpha() or char.isdigit():  # Nếu là toán hạng (chữ cái hoặc số)
            stack.append(char)
        else:  # Nếu là toán tử
            if not stack or len(stack) < 2:
                print("Lỗi: Biểu thức hậu tố không hợp lệ!")
                sys.exit(1)
            operand2 = stack.pop() # Pop operand2 first as it was pushed later
            operand1 = stack.pop() # Pop operand1 second
            # Tạo dạng tiền tố: operator + operand1 + operand2
            new_expr = char + operand1 + operand2
            stack.append(new_expr)

    if len(stack) != 1:
        print("Lỗi: Biểu thức hậu tố không hợp lệ!")
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
        print(postfix_to_prefix(expr))
    except Exception as e:
        print(f"Lỗi: {e}")