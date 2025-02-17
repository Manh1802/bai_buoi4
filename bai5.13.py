import sys

def evaluate_infix(expression):
    try:
        # Tính giá trị biểu thức, đảm bảo phép chia lấy phần nguyên
        result = eval(expression.replace("/", "//"))
        return result
    except Exception:
        print("Lỗi: Biểu thức không hợp lệ!")
        sys.exit(1)

# Kiểm tra lỗi nhập số lượng test case
try:
    T = int(input("Nhập số lượng test case: ").strip())
except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")
    sys.exit(1)

# Xử lý từng test case
for _ in range(T):
    try:
        expr = input("Nhập biểu thức trung tố: ").strip()
        print(evaluate_infix(expr))
    except Exception as e:
        print(f"Lỗi: {e}")