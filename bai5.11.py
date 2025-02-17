import sys

def evaluate_postfix_expression(expression):
    calculation_stack = []
    for char in expression:
        if char.isdigit():
            calculation_stack.append(int(char))
        else:
            try:
                operand_2 = calculation_stack.pop()
                operand_1 = calculation_stack.pop()
                if char == '+':
                    result = operand_1 + operand_2
                elif char == '-':
                    result = operand_1 - operand_2
                elif char == '*':
                    result = operand_1 * operand_2
                elif char == '/':
                    result = operand_1 // operand_2
                else:
                    raise ValueError()
                calculation_stack.append(result)
            except IndexError:
                print("Lỗi: Biểu thức hậu tố không hợp lệ!", file=sys.stderr)
                sys.exit(1)
            except ValueError:
                print("Lỗi: Toán tử không hợp lệ!", file=sys.stderr)
                sys.exit(1)
    if len(calculation_stack) != 1:
        print("Lỗi: Biểu thức hậu tố không hợp lệ!", file=sys.stderr)
        sys.exit(1)
    return calculation_stack[0]

if __name__ == "__main__":
    try:
        test_case_count = int(input().strip())
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ cho số lượng test case!", file=sys.stderr)
        sys.exit(1)
    for _ in range(test_case_count):
        try:
            postfix_expression = input().strip()
            evaluation_result = evaluate_postfix_expression(postfix_expression)
            print(evaluation_result)
        except Exception as e:
            print(f"Lỗi không xác định: {e}", file=sys.stderr) 