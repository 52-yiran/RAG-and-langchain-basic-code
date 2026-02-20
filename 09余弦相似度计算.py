import math

def cosine_similarity(vec1, vec2):
    # 点积
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    # 模长
    norm1 = math.sqrt(sum(a ** 2 for a in vec1))
    norm2 = math.sqrt(sum(b ** 2 for b in vec2))
    # 余弦相似度
    return dot_product / (norm1 * norm2) if norm1 * norm2 != 0 else 0

# 测试
A = [1, 2, 3]
B = [2, 4, 6]
print(cosine_similarity(A, B))  # 输出: 1.0