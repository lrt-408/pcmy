from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd

# 自定义数据集
data = {
    'ID': [1, 2, 3, 4, 5, 6],
    'Onion': [1, 0, 0, 1, 1, 1],
    'Potato': [1, 1, 0, 1, 1, 1],
    'Burger': [1, 1, 0, 0, 1, 1],
    'Milk': [0, 1, 1, 1, 0, 1],
    'Beer': [0, 0, 1, 0, 1, 0],
}
df = pd.DataFrame(data)
#print(df)

# 利用mlxtend提供的apriori算法函数得到频繁项集，其中设置最小支持度为50%
frequent_item_sets = apriori(df[['Onion', 'Potato', 'Burger', 'Milk', 'Beer']], min_support=0.50, use_colnames=True)
#print(frequent_item_sets)

# 计算规则，并设置提升度阈值为 1 （返回的是各个指标的数值，可以按照按兴趣的指标排序观察，但具体解释还得参考实际数据的含义）
rules = association_rules(frequent_item_sets, metric='lift', min_threshold=1)
#print(rules)

print(rules[(rules['lift'] > 1.125) & (rules['confidence'] > 0.8)])

