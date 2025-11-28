from efficient_apriori import apriori
import pandas as pd
import numpy as np

groceries = pd.read_csv("groceries.csv", header=0)
print(groceries.head())
print(groceries.shape)

bakery = pd.read_csv("bakery.csv")
bakery.columns = bakery.columns.str.strip()
print(bakery.head())
print(bakery.shape)

transactions = []
for i in range(len(groceries)):
    row = groceries.iloc[i, 1:].dropna().astype(str).tolist()
    transactions.append(row)

print(len(transactions), transactions[:5])

transactions_b = []
item_columns = bakery.columns[1:]
for i in range(len(bakery)):
    items = item_columns[bakery.iloc[i, 1:] == 1].tolist()
    if items:
        transactions_b.append(items)

print(len(transactions_b), transactions_b[:5])

itemsets, rules = apriori(
    transactions, 
    min_support=0.05, 
    min_confidence=0.25
)

print("Frequent Itemsets (Groceries):")
print(itemsets)
print("\nRules (Groceries):")
print(rules)

b_item, b_rules = apriori(
    transactions_b,
    min_support=0.05,
    min_confidence=0.25
)

print("\nFrequent Itemsets (Bakery):")
print(b_item)
print("\nRules (Bakery):")
print(b_rules)

