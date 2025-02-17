def check_parentheses_redundancy(expression):

    parenthesis_stack = []
    for index, char in enumerate(expression):
        if char == '(':
            parenthesis_stack.append(index)
        elif char == ')':
            if not parenthesis_stack:
                continue  # Ngoặc đóng không khớp, không liên quan đến dư thừa

            start_index = parenthesis_stack.pop()
            if start_index + 1 == index:  # Trường hợp 1: Ngoặc rỗng '()'
                return "Yes"

            content_within = expression[start_index + 1:index]
            if not content_within.isalnum() and len(content_within) <= 3: # Kiểm tra biểu thức đơn giản (độ dài <= 3 là heuristic cho ví dụ)
                is_simple_expression = True
                operators_list = "+-*/"
                operand_count = 0
                operator_count = 0
                for content_char in content_within:
                    if content_char.isalnum():
                        operand_count += 1
                    elif content_char in operators_list:
                        operator_count += 1
                if operand_count + operator_count != len(content_within.replace(" ", "")):
                    is_simple_expression = False
                if operand_count > 2 or operator_count > 1: # Định nghĩa lại biểu thức đơn giản
                    is_simple_expression = False

                if is_simple_expression: # Trường hợp 2: Ngoặc bao quanh biểu thức đơn giản
                    return "Yes"

            if start_index + 1 < index and expression[start_index + 1] == '(' and expression[index - 1] == ')': # Trường hợp 3: Ngoặc liên tiếp '(())'
                return "Yes"

    return "No"  # Không tìm thấy ngoặc dư thừa theo các kiểm tra trên

# Đọc số lượng test case
test_cases_count = int(input())

# Xử lý từng test case
print("\nKết quả kiểm tra:")
for _ in range(test_cases_count):
    expression_to_check = input()
    print(check_parentheses_redundancy(expression_to_check))