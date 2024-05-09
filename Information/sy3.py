import math
from scipy.stats import entropy
import zlib

def calculate_entropy(data):
    # 统计词频
    frequencies = {}
    total_count = 0
    for char in data:
        frequencies[char] = frequencies.get(char, 0) + 1
        total_count += 1

    # 计算概率
    probabilities = [count / total_count for count in frequencies.values()]

    # 计算信息熵
    entropy_value = entropy(probabilities, base=2)
    return entropy_value

# 读取原始文档
filename = "Information/text.txt"
with open(filename, "r") as f:
    original_text = f.read()

# 压缩文档
compressed_text = zlib.compress(original_text.encode())

# 计算原始文档的信息熵
original_entropy = calculate_entropy(original_text)
print("原始文档的信息熵：", original_entropy)

# 计算压缩文档的信息熵
compressed_entropy = calculate_entropy(compressed_text)
print("压缩文档的信息熵：", compressed_entropy)

# 解压缩文档
decompressed_text = zlib.decompress(compressed_text).decode()

print("原始文档内容：")
print(original_text)

print("压缩文档内容：")
print(compressed_text)

print("解压缩文档内容：")
print(decompressed_text)