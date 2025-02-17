from itertools import combinations

def remove_brackets(expression):
    brackets = []  # Danh sách lưu vị trí của dấu ngoặc đơn
    stack = []  # Stack để tìm cặp dấu ngoặc
    
    # Xác định vị trí của các dấu ngoặc
    for i, char in enumerate(expression):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                brackets.append((stack.pop(), i))  # Lưu cặp (vị trí '(' , vị trí ')')

    results = set()  # Dùng set để tránh trùng lặp biểu thức
    
    # Tạo tất cả các tổ hợp có thể bỏ dấu ngoặc
    for i in range(1, len(brackets) + 1):  # Không bỏ hết, bỏ ít nhất 1 cặp
        for combination in combinations(brackets, i):
            to_remove = set(sum(combination, ()))  # Flatten list [(a, b), (c, d)] -> {a, b, c, d}
            new_expr = ''.join(expression[j] for j in range(len(expression)) if j not in to_remove)
            results.add(new_expr)

    # In ra tất cả biểu thức hợp lệ theo thứ tự từ điển
    for expr in sorted(results):
        print(expr)

# Đọc input
expression = input("Nhập biểu thức: ").strip()
remove_brackets(expression)