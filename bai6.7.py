import sys
from collections import deque

def is_adjacent(word1, word2):
    """Kiểm tra xem hai từ có khác nhau đúng một ký tự không"""
    if len(word1) != len(word2):
        return False
    diff_count = sum(1 for a, b in zip(word1, word2) if a != b)
    return diff_count == 1

def shortest_transformation_path(words, s, t):
    if s == t:
        return 0  # Nếu s đã là t, không cần bước nào

    word_set = set(words)  # Để tra cứu nhanh hơn
    queue = deque([(s, 1)])  # (Từ hiện tại, số bước)
    visited = set()

    while queue:
        current_word, steps = queue.popleft()

        if current_word == t:
            return steps

        if current_word not in visited:
            visited.add(current_word)
            for word in words:
                if word not in visited and is_adjacent(current_word, word):
                    queue.append((word, steps + 1))

    return -1  # Không tìm thấy đường đi

# Kiểm tra lỗi nhập số lượng test case
try:
    T = int(input("Nhập số lượng test case: ").strip())
except ValueError:
    print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")
    sys.exit(1)

# Xử lý từng test case
for _ in range(T):
    try:
        data = input().strip().split()
        N = int(data[0])
        s, t = data[1], data[2]
        words = input().strip().split()
        
        if len(words) != N:
            print("Lỗi: Số lượng xâu nhập vào không khớp!")
            sys.exit(1)

        print(shortest_transformation_path(words, s, t))
    except Exception as e:
        print(f"Lỗi: {e}")