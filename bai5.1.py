def check_redundant_brackets(expression):
    stack = []
    for char in expression:
        if char == ')':
            top = stack.pop()
            elements_inside = 0

            while top != '(':
                elements_inside += 1
                top = stack.pop()
            
            if elements_inside == 0:  # Không có gì giữa dấu ngoặc, tức là dư thừa
                return "No"
        else:
            stack.append(char)
    
    return "Yes"

# Đọc số lượng test case từ người dùng
T = int(input("Nhập số lượng test case: ").strip())

# Xử lý từng test case từ bàn phím
print("\nKết quả kiểm tra:")
for _ in range(T):
    expression = input("Nhập biểu thức: ").strip()
    print(f"{expression} → {check_redundant_brackets(expression)}")

# Thêm các test case tự động
print("\nChạy test case tự động:")
test_cases = ["((a+b))", "(a+(b)/c)", "(a+b*(c-d))"]
for expression in test_cases:
    print(f"{expression} → {check_redundant_brackets(expression)}")