from itertools import combinations

# 定义函数实现 Apriori 算法
def generate_candidates(itemset, length):
    candidates = []
    for i in range(len(itemset)):
        for j in range(i+1, len(itemset)):
            union_set = list(set(itemset[i]) | set(itemset[j]))
            if len(union_set) == length:
                candidates.append(union_set)
    return candidates

def calculate_support(transactions, candidate):
    count = 0
    for transaction in transactions:
        if set(candidate).issubset(set(transaction)):
            count += 1
    return count / len(transactions)

# 准备数据
transactions = [
    ['apple', 'banana', 'orange'],
    ['banana', 'grapes'],
    ['apple', 'banana', 'grapes'],
    ['apple', 'orange'],
    ['banana', 'orange']
]

# Apriori 算法
min_support = 0.2
min_confidence = 0.7

itemset = [[item] for sublist in transactions for item in sublist]
frequent_itemsets = []
length = 1

while itemset:
    candidates = generate_candidates(itemset, length)
    itemset = []
    for candidate in candidates:
        support = calculate_support(transactions, candidate)
        if support >= min_support:
            frequent_itemsets.append((candidate, support))
            itemset.append(candidate)
    length += 1

# 生成关联规则
rules = []
for itemset, support in frequent_itemsets:
    if len(itemset) > 1:
        for i in range(1, len(itemset)):
            for antecedent in combinations(itemset, i):
                antecedent = list(antecedent)
                consequent = list(set(itemset) - set(antecedent))
                antecedent_support = calculate_support(transactions, antecedent)
                confidence = support / antecedent_support
                if confidence >= min_confidence:
                    rules.append((antecedent, consequent, confidence))

# 展示关联规则
for rule in rules:
    print(rule)