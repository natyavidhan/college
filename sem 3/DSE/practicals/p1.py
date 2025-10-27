import pandas as pd
import json

with open('reviews.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

df = pd.json_normalize(
    data['paper'],
    record_path=['review'],
    meta=['id', 'preliminary_decision'],
    record_prefix='review_',
    meta_prefix='paper_'
)

print(df.head())

# ========= handling missing values =========

print(df.isnull().sum())

df['review_confidence'] = pd.to_numeric(df['review_confidence'], errors='coerce')
df['review_evaluation'] = pd.to_numeric(df['review_evaluation'], errors='coerce')

df.fillna({'review_confidence': df['review_confidence'].mean(), 'review_evaluation': df['review_evaluation'].mean()}, inplace=True)

# df['review_remarks'].fillna('No remarks', inplace=True)
# df['review_text'].fillna('No text provided', inplace=True)

df.fillna({'review_remarks': '', 'review_text': ''}, inplace=True)

# ========= handling inconsistent data =========

df['review_lan'] = df['review_lan'].str.strip().str.lower()
# df['review_lan'].replace({'spa': 'es', 'en-us': 'en'}, inplace=True)
df.replace({'review_lan': {'spa': 'es', 'en-us': 'en'}}, inplace=True)

df['paper_preliminary_decision'] = df['paper_preliminary_decision'].str.strip().str.lower().replace({'accepted': 'accept', 'rejected': 'reject'})
df.loc[~df['paper_preliminary_decision'].isin(['accept', 'reject']), 'paper_preliminary_decision'] = pd.NA

# ========= handling outliers =========

df.loc[df['review_confidence'] > 5, 'review_confidence'] = 5
df.loc[df['review_confidence'] < 1, 'review_confidence'] = 1

df.loc[df['review_evaluation'] > 2, 'review_evaluation'] = 2
df.loc[df['review_evaluation'] < -2, 'review_evaluation'] = -2

"""
Validation Rules:

| Rule | Field                      | Expected Range / Type     |
| ---- | -------------------------- | ------------------------- |
|  R1  | review_confidence          | 1–5                       |
|  R2  | review_evaluation          | -2–2                      |
|  R3  | review_lan                 | one of ['en', 'es', 'fr'] |
|  R4  | paper_preliminary_decision | ['accept', 'reject']      |
|  R5  | review_text                | not empty                 |


"""

# ========= applying validation rules =========

rule1 = df["review_confidence"].between(1, 5)
rule2 = df["review_evaluation"].between(-2, 2)
rule3 = df["review_lan"].isin(["en", "es", "fr"])
rule4 = df["paper_preliminary_decision"].isin(["accept", "reject"])
rule5 = df["review_text"].str.strip().ne("")

Rules = pd.DataFrame({
    "Rule 1 (Confidence 1–5)": rule1,
    "Rule 2 (Evaluation -2–2)": rule2,
    "Rule 3 (Language Valid)": rule3,
    "Rule 4 (Decision Valid)": rule4,
    "Rule 5 (Text Non-empty)": rule5
})

print("Rule Violation Summary:")
for col in Rules.columns:
    total = len(Rules)
    passed = Rules[col].sum()
    failed = total - passed
    print(f"{col}: {failed} violations out of {total}")

# ========= final cleaned data =========

print(df.describe(include='all'))

# Visualize numeric distributions
# import matplotlib.pyplot as plt
# df['review_confidence'].hist()
# plt.title('Distribution of Review Confidence')
# plt.show()

# df['review_evaluation'].hist()
# plt.title('Distribution of Review Evaluation')
# plt.show()

# save cleaned data
df.to_csv("cleaned_paper_reviews.csv", index=False)
