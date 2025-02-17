
import sys

def decode_string(encoded_str):
    stack = []
    current_string = ""
    current_num = 0

    for char in encoded_str:
        if char.isdigit():
            current_num = current_num * 10 + int(char)  # Xử lý số nhiều chữ số
        elif char == '[':
            stack.append((current_string, current_num))  # Lưu chuỗi tạm và số lần lặp
            current_string = ""
            current_num = 0
        elif char == ']':
            last_string, repeat_times = stack.pop()
            current_string = last_string + current_string * repeat_times  # Giải mã
        else:
            current_string += char  # Thêm ký tự vào chuỗi hiện tại

    return current_string

# Kiểm tra lỗi nhập số lượng test case
try:
    T = int(input("Nhập số lượng test case: ").strip())
except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")
    sys.exit(1)

# Xử lý từng test case
for _ in range(T):
    try:
        encoded_str = input("Nhập xâu mã hóa: ").strip()
        print(decode_string(encoded_str))
    except Exception as e:
        print(f"Lỗi: {e}")
