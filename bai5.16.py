import sys

def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)  # Thêm 0 vào cuối để đảm bảo pop hết stack

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area

# Kiểm tra lỗi nhập số lượng test case
try:
    T = int(input("Nhập số lượng test case: ").strip())
except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")
    sys.exit(1)

# Xử lý từng test case
for _ in range(T):
    try:
        N = int(input("Nhập số cột: ").strip())
        heights = list(map(int, input("Nhập độ cao của các cột: ").strip().split()))
        if len(heights) != N:
            print("Lỗi: Số cột nhập vào không khớp!")
            sys.exit(1)
        print(largest_rectangle_area(heights))
    except Exception as e:
        print(f"Lỗi: {e}")