import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler, MinMaxScaler, Binarizer

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

print(df.head())
print("\nDataset shape:", df.shape)
print("\nSummary statistics:\n", df.describe())


X = df.drop(columns=['species'])

scaler = StandardScaler()
df_standardized = scaler.fit_transform(X)
df_standardized = pd.DataFrame(df_standardized, columns=X.columns)

print("\nStandardized Data (first 5 rows):\n", df_standardized.head())


normalizer = MinMaxScaler()
df_normalized = normalizer.fit_transform(X)
df_normalized = pd.DataFrame(df_normalized, columns=X.columns)

print("\nNormalized Data (first 5 rows):\n", df_normalized.head())


df_transformed = df.copy()
df_transformed["sepal width (cm)"] = np.log1p(df_transformed["sepal width (cm)"])

print("\nTransformed (log) Data (first 5 rows):\n", df_transformed.head())


agg_df = df.groupby("species", observed=False).mean()
print("\nAggregated Mean by Species:\n", agg_df)



bins = [0, 2.5, 5, 7.5]
labels = ['Small', 'Medium', 'Large']

df_discrete = df.copy()
df_discrete['custom_petal_length'] = pd.cut(df['petal length (cm)'], bins=bins, labels=labels)

print("\nDiscretized Data (Petal Length into 3 bins):\n", df_discrete.head())



binarizer = Binarizer(threshold=1.0)
df_binarized = df.copy()
df_binarized["wide_petal"] = binarizer.fit_transform(df[["petal width (cm)"]])

print("\nBinarized Data (Petal width >= 1.0 -> 1):\n", df_binarized.head())


sample_df = df.sample(frac=0.2, random_state=42)
print("\nSampled 20% of the Data:\n", sample_df)
