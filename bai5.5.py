import sys

def normalize_expression(expression):
   
    stack = [False]  # Stack để theo dõi trạng thái đảo dấu bên trong ngoặc.
                      # False: không đảo dấu, True: cần đảo dấu.
    result = []
    # sign = 1  # Không dùng trong phiên bản này, trạng thái dấu được theo dõi bởi stack

    for i, char in enumerate(expression):
        if char == '(':
            # Nếu trước dấu '(' là '-', thì cần đảo dấu cho biểu thức bên trong
            if i > 0 and expression[i - 1] == '-':
                stack.append(not stack[-1])  # Đẩy trạng thái đảo ngược lên stack
            else:
                stack.append(stack[-1])  # Đẩy trạng thái hiện tại (không đảo dấu)
        elif char == ')':
            stack.pop()  # Thoát khỏi mức ngoặc hiện tại, trở về trạng thái trước đó
        elif char == '+' or char == '-':
            # Nếu đang ở trạng thái đảo dấu (đỉnh stack là True), thì đổi dấu hiện tại
            if stack[-1]:
                result.append('-' if char == '+' else '+')
            else:
                result.append(char)
        else:
            result.append(char)  # Thêm toán hạng và các toán tử khác như bình thường

    return ''.join(result)

# Xử lý lỗi khi đọc số lượng test case
try:
    T = int(input("Nhập số lượng test case: ").strip())
    if T < 1: # Kiểm tra số lượng test case phải là số nguyên dương
        raise ValueError("Số lượng test case phải là số nguyên dương.")
except ValueError as e:
    print(f"Lỗi nhập số lượng test case: {e}")
    sys.exit(1)

# Xử lý từng test case
for _ in range(T):
    try:
        P1 = input("Nhập biểu thức P1: ").strip()
        P2 = input("Nhập biểu thức P2: ").strip()

        norm_P1 = normalize_expression(P1) # Chuẩn hóa biểu thức P1
        norm_P2 = normalize_expression(P2) # Chuẩn hóa biểu thức P2

        # So sánh biểu thức đã chuẩn hóa và in kết quả
        print("YES" if norm_P1 == norm_P2 else "NO")

    except Exception as e:
        print(f"Lỗi xử lý biểu thức: {e}") # Thông báo lỗi tổng quát hơn