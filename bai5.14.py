import sys

def smallest_number_from_pattern(S):
    stack = []
    result = []
    num = 1  # Bắt đầu từ số nhỏ nhất là 1

    for char in S:
        stack.append(num)
        num += 1

        if char == 'I':
            while stack:
                result.append(str(stack.pop()))

    stack.append(num)  # Thêm số cuối cùng
    while stack:
        result.append(str(stack.pop()))

    return ''.join(result)

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
        print(smallest_number_from_pattern(S))
    except Exception as e:
        print(f"Lỗi: {e}")